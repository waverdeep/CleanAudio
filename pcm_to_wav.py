import os
import glob
import multiprocessing
from multiprocessing import Process
from tqdm import tqdm
import wave


# The parameters are prerequisite information. More specifically,
# channels, bit_depth, sampling_rate must be known to use this function.
def pcm2wav(pcm_file, wav_file, channels=1, bit_depth=16, sampling_rate=16000):
    # Check if the options are valid.
    if bit_depth % 8 != 0:
        raise ValueError("bit_depth " + str(bit_depth) + " must be a multiple of 8.")

    # Read the .pcm file as a binary file and store the data to pcm_data
    with open(pcm_file, 'rb') as opened_pcm_file:
        pcm_data = opened_pcm_file.read();

        obj2write = wave.open(wav_file, 'wb')
        obj2write.setnchannels(channels)
        obj2write.setsampwidth(bit_depth // 8)
        obj2write.setframerate(sampling_rate)
        obj2write.writeframes(pcm_data)
        obj2write.close()


def converting(filelist, id):
    cc = 0
    for file in filelist:
        origin_path = file
        new_path = file.replace('pcm', 'wav')
        pcm2wav(origin_path, new_path, 1, 16, 16000)
        cc = cc + 1
        if cc % 1000 == 0:
            print('running {} : {}'.format(id, new_path))
    print('{} : finish'.format(id))


def split_list_by_count(filelist, count):
    makeup_list = []
    size = int(len(filelist) / count)

    for i in range(count - 1):
        start = i * size
        end = (i + 1) * size
        makeup_list.append(filelist[start:end])

    start = (count - 1) * size
    makeup_list.append(filelist[start:])
    return makeup_list


def run_convert_data(input_dir='./'):
    wav_files = glob.glob(os.path.join(input_dir, '**', '*.pcm'), recursive=True)
    print("data count : {}".format(len(wav_files)))
    cpu_count = multiprocessing.cpu_count()
    print("cpu count : {}".format(cpu_count))
    datapack = split_list_by_count(wav_files, cpu_count)

    procs = []
    for id, filelist in enumerate(datapack):
        proc = Process(target=converting, args=(filelist, id))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()


run_convert_data(input_dir='./sample_dataset')
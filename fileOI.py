import errno
import os
import glob
import soundfile as sf
import librosa


# find all dataset filepath
def get_all_file_path(input_dir, file_extension):
    temp = glob.glob(os.path.join(input_dir, '**', '*.{}'.format(file_extension)), recursive=True)
    return temp


def save_audio_file(filename,  data, extension='', sample_rate=16000, subtype='PCM_16'):
    pure_filepath = get_pure_filepath(filename)
    try:
        if not (os.path.isdir(pure_filepath)):
            os.makedirs(os.path.join(pure_filepath))
    except OSError as e:
        if e.errno != errno.EEXIST:
            print("Failed to create directory!!!!!")
            raise

    if extension is not '':
        sf.write('{}.{}'.format(filename, extension), data, samplerate=sample_rate, subtype=subtype)
    else:
        sf.write(filename, data, samplerate=sample_rate, subtype=subtype)


def create_file(filepath):
    f = open(filepath, 'w', encoding='utf8')
    return f


def read_audio_file(filename, extension, sample_rate=16000):
    if extension is not '':
        y, sr = librosa.load('{}.{}'.format(filename, extension), sr=sample_rate)
        return y, sr
    else:
        y, sr = librosa.load(filename, sr=sample_rate)
        return y, sr


def get_pure_filename(filename):
    temp = filename.split('.')
    del temp[-1]
    temp = ' '.join(temp)
    temp = temp.split('/')
    temp = temp[-1]
    return temp


def get_pure_filepath(filename):
    temp = filename.split('/')
    del temp[-1]
    temp = '/'.join(temp)
    return temp


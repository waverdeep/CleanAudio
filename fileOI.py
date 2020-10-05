import os
import glob
import soundfile as sf
import librosa


# find all dataset filepath
def get_all_file_path(input_dir, file_extension):
    temp = glob.glob(os.path.join(input_dir, '**', '*.{}'.format(file_extension)), recursive=True)
    return temp


def save_audio_file(filename,  data, extension='', sample_rate=16000, subtype='PCM_24'):
    if extension is not '':
        sf.write('{}.{}'.format(filename, extension), data, samplerate=sample_rate, subtype=subtype)
    else:
        sf.write(filename, data, samplerate=sample_rate, subtype=subtype)


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


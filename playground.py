import clean_noise
import fileOI


dataset = fileOI.get_all_file_path('./sample_dataset', 'wav')

data, _ = fileOI.read_audio_file(dataset[1], '')

filename = fileOI.get_pure_filename(dataset[1])
filepath = fileOI.get_pure_filepath(dataset[1])

fileOI.save_audio_file('{}/{}-{}'.format(filepath, filename, 'nr'), data, 'wav')
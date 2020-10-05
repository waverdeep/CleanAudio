import clean_noise
import fileOI


dataset = fileOI.get_all_file_path('./sample_dataset', 'wav')

data, _ = fileOI.read_audio_file(dataset[0], '')

filename = fileOI.get_pure_filename(dataset[0])
filepath = fileOI.get_pure_filepath(dataset[0])

fileOI.save_audio_file('{}/{}-{}'.format(filepath, filename, 'nr'), data, 'wav')
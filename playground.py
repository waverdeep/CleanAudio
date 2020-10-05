import clean_noise
import fileOI


dataset = fileOI.get_all_file_path('./sample_dataset', 'wav')

for i in range(10):
    data, _ = fileOI.read_audio_file(dataset[i], '')

    filename = fileOI.get_pure_filename(dataset[i])
    filepath = fileOI.get_pure_filepath(dataset[i])

    clean_data = clean_noise.noise_reduction(data)
    trim_data = clean_noise.trim_silence(clean_data)

    fileOI.save_audio_file('{}/{}-{}'.format(filepath, filename, 'tr'), clean_data, 'wav')
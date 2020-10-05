from scipy import signal
import scipy.io.wavfile
import scipy.io
import librosa


def noise_reduction(signals):
    return scipy.signal.wiener(signals)


def trim_silence(samples, top_db=25):
    signals, index = librosa.effects.trim(samples, top_db=top_db)
    return signals, index



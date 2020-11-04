from scipy import signal
import scipy.io.wavfile
import scipy.io
import librosa


# 성능이 별로 좋지 않은듯 하다.
# https://docs.scipy.org/doc/scipy/reference/generated/scipy.signal.wiener.html
# 이것을 적용해보아도 좋을 듯 함
# https://github.com/dodiku/noise_reduction
def noise_reduction(signals):
    return scipy.signal.wiener(signals)


def trim_silence(samples, top_db=25):
    signals, index = librosa.effects.trim(samples, top_db=top_db)
    return signals, index



# CleanAudio
오디오 샘플에서 불필요한 부분을 삭제하거나, silence 부분을 제거 혹은 noise reduction을 진행하는 프로젝트

## clean_noise.py
음원에 존재하는 노이즈를 제거하는 기능들이 들어있는 파이썬 스크립트 파일

### noise_reduction(signals):
numpy 형태의 음원 데이터를 wiener filter를 통해 noise 를 제거
- signal :  np.ndarray, shape=(n,) or (2, n)

### trim_silence(samples, top_db=25):
음원 앞뒤에 있는 불필요한 silence 부분을 제거하는 함수
- samples :  np.ndarray, shape=(n,) or (2, n)
- top_db : 25

### get_all_file_path(input_dir, file_extension):
특정 디렉토리와 확장자를 파라미터레 작성하면 디렉토리를 기준으로 하위에 있는 모든 디렉토리까지 방문하여 작성한 확장자에 따른 파일들을 모두 찾아 리스트로 반환하는 함수
- input_dir : 대상 디렉토리
- file_extension : 검색할 확장자

## fileOI.py
파일 입출력게 관련된 기능들과 file base 작업들에 대한 파이썬 스크립트 파일

### save_audio_file(filename,  data, extension='', sample_rate=16000, subtype='PCM_16'):
numpy형태의 데이터를 음원 파일로 저장해주는 함수. 기본적으로 16000/16 으로 샘플링을 진행
- filename : 해당 음원의 파일이름(확장자 포함해도 되고 안해도 됨)
- data :  np.ndarray, shape=(n,) or (2, n)
- extension : filename에서 확장자를 적었다면 '', 확장자가 없다면 여기서 필수로 명시해주어야 함
- sampling_rate : 16000
- subtpye : sampling bit(PCM_16)

## pcm_to_wav.py
pcm 형식으로 되어있는 음원을 wav 형태로 변경할 수 있는 기능을 담고 있는 파이썬 스크립트 파일

### run_convert_data(input_dir):
특정 디렉토리 하위에 있는 모든 pcm파일들을 모두 wav 형식으로 변경해주는 함수
멀티프로세싱으로 이루어져 있으며 동작하는 컴퓨터의 CPU 최대 개수에 맞춰서 프로세스가 
- input_dir : pcm파일이 위치한 디렉토리 경로

## audio_manipulate.py
오디오를 자르거나 분석하는 기능을 담고 있는 파이썬 스크립트 파일

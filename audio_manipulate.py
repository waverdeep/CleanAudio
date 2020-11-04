import librosa
import itertools


# top_db를 기준으로 음원을 여러 구간으로 자르는 함수
def split_audio(source, top_db=15, sr=16000):
    sections = [0]
    while True:
        partition = librosa.effects.split(source, top_db=top_db)
        if 10 <= len(partition) <= 20:
            break
        else:
            top_db = top_db + 1
    temp = list(itertools.chain(*partition))
    for i in temp:
        if 10 <= i/16000:
            sections.append(i)
            break
    for i in temp:
        if 20 <= i/16000:
            sections.append(i)
            break
    for i in temp:
        if 30 <= i/16000:
            sections.append(i)
            break
    sections.append(len(source))
    for i in sections:
        print("section : ", i/16000)
    return sections


def get_2gram(sections):
    temp = []
    for i in range(len(sections)-1):
        temp.append([sections[i],sections[i+1]])
    print(temp)


def split_source_to_wav(source, sections, sr=16000):
    get_2gram(sections)





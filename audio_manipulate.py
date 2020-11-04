import librosa
import itertools
import fileOI


# top_db를 기준으로 음원을 여러 구간으로 자르는 함수
def split_audio(source, top_db=15, sr=16000):
    sections = [0]
    while True:
        partition = librosa.effects.split(source, top_db=top_db)
        if 10 <= len(partition) <= 25:
            break
        else:
            top_db = top_db + 1
    temp = list(itertools.chain(*partition))
    for i in temp:
        if 5 <= i/16000:
            sections.append(i)
            break
    for i in temp:
        if 10 <= i/16000:
            sections.append(i)
            break
    for i in temp:
        if 15 <= i / 16000:
            sections.append(i)
            break
    for i in temp:
        if 20 <= i/16000:
            sections.append(i)
            break
    for i in temp:
        if 25 <= i/16000:
            sections.append(i)
            break
    for i in temp:
        if 30 <= i/16000:
            sections.append(i)
            break
    for i in temp:
        if 35 <= i/16000:
            sections.append(i)
            break
    sections.append(len(source))
    for i in sections:
        print("section : ", i/16000)
    return sections


def get_2gram(sections):
    temp = []
    for i in range(len(sections)-1):
        temp.append([sections[i], sections[i+1]])
    return temp


def merge_short_part(sections):
    remove_list_idx = []
    for i in range(len(sections)-1):
        if sections[i+1] - sections[i] <= 32000:
            remove_list_idx.append(i)
    remove_list_idx = sorted(remove_list_idx, reverse=True)
    for i in remove_list_idx:
        del sections[i]
    return sections


def split_source_to_wav(source, sections, root_filepath, split_filepath, sr=16000):
    sections = remove_overlap_items(sections)
    sections = merge_short_part(sections)
    partition = get_2gram(sections)
    pure_filename = fileOI.get_pure_filename(root_filepath)
    for idx, data in enumerate(partition):
        part = source[data[0]:data[1]]
        filepath = '{}/{}-{}.wav'.format(split_filepath, pure_filename, idx)
        fileOI.save_audio_file(filepath, part, '')


def remove_overlap_items(sections):
    new_list = []
    for v in sections:
        if v not in new_list:
            new_list.append(v)
    return new_list




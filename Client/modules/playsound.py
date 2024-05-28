from pygame import mixer


def play_mp3(file_path):
    mixer.init()
    mixer.music.load(file_path)
    mixer.music.play()
    mixer.get_busy()
    return mixer

import os
import pyscreenshot


def screenshot():
    file_name = "screen.png"
    folder_path = ".files"
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, file_name)
    image = pyscreenshot.grab()
    image.save(file_path)
    return file_path

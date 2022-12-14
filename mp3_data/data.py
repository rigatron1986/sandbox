# import eyeD3
import os
import eyed3
import shutil

search_path = '//RIGADISK/Music/Tamil'
all_files = os.listdir(search_path)
all_mp3 = [x for x in all_files if x.endswith('.mp3')]
print(all_mp3)
result = {}
failed = []
for mp3 in all_mp3:
    full_path = os.path.join(search_path, mp3)
    audiofile = eyed3.load(full_path)
    album_name = audiofile.tag.album
    # print(album_name)
    if not album_name:
        continue
    if album_name not in result:
        result[album_name] = []
    new_path = os.path.join(search_path, album_name, mp3)
    if not os.path.exists(os.path.dirname(new_path)):
        os.makedirs(os.path.dirname(new_path))
    print('Old Path: ', full_path)
    print('New Path: ', new_path)
    shutil.move(full_path, new_path)
    # result[album_name].append(new_path)

import os
import json
import re

folder_path = "data/lyrics_json/"


# def clean_description(desc):
#     if isinstance(desc, dict) and 'plain' in desc and desc['plain']:
#         raw_text = desc['plain']
#         cleaned_text = re.sub(r'\\(.)', lambda m: m.group(1) if m.group(1) in ['\'', '"'] else m.group(0), raw_text)
#         cleaned_text = cleaned_text.replace('\n', ' ')
#         return cleaned_text

# def clean_lyrics(text):
#     text =  text.split('\xa0', 1)[-1]
#     cleaned_text = re.sub(r'\\(.)', lambda m: m.group(1) if m.group(1) in ['\'', '"'] else m.group(0), text)
#     cleaned_text = cleaned_text.replace('\n', ' ')
#     return text

def createLyricsList(folder_path):
    lyrics_list = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".json"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as f:
                artist_songs = json.load(f)
                for song in artist_songs['songs']:
                    song_dict = {}
                    song_dict['rapper'] = artist_songs['name']
                    song_dict['title'] = song['title']

                    song_dict['year'] = song['release_date_components'].get('year') if song.get('release_date_components') else "unknown"

                    song_dict['description'] = song['description']
                    song_dict['lyrics'] =  song['lyrics']
                    lyrics_list.append(song_dict)
    return lyrics_list

l = createLyricsList(folder_path)
print(l)
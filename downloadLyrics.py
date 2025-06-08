from fetchNameList import fetchNamesFromRanker, readNamesFromLocal
from lyricsgenius import Genius
import os
import json
import requests

# url = "https://www.ranker.com/crowdranked-list/the-greatest-rappers-of-all-time"
# names = fetchNamesFromRanker(url)

# instead of scraping everytime, just load the txt file.
genius_timeout = 999
genius_max_songs = 5
num_rappers = 3  # any number from 1 to 150 (150 rappers in  rapper_names.txt)
genius_sleeptime = 1

genius_token = 'tokens'
genius = Genius(genius_token,  timeout=genius_timeout, sleep_time=genius_sleeptime,  skip_non_songs=True)

file_name = 'data/rapper_names/rapper_names.txt'
rappers  = readNamesFromLocal(file_name)

for i, rapper in enumerate(rappers[100:102]):
    print('==============')
    print(f'rapper number {i}')
    try:
        rapper_result = genius.search_artist(rapper, max_songs=genius_max_songs)
    except requests.exceptions.HTTPError as e:
        print(f"HTTP error occurred: {e}")

    save_dir = 'data/lyrics_json/'
    os.makedirs(save_dir, exist_ok=True)
    filepath = os.path.join(save_dir, f'lyrics_{rapper}.json')
    rapper_dict = rapper_result.to_dict()
    with open(filepath, "w") as f:
        json.dump(rapper_dict, f, indent=2)
    
    print(f"Saved to {filepath}")
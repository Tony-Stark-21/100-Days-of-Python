import os
import requests
from bs4 import BeautifulSoup

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
TXT_FILE_PATH = os.path.join(CURRENT_DIR, "songs.txt")

target_date = "2000-08-12"
URL = f"https://www.billboard.com/charts/hot-100/{target_date}/"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
}

print(f"🔄 Extracting Billboard Hot 100 for date: {target_date}...")
all_songs = []

try:
    response = requests.get(URL, headers=headers)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    song_elements = soup.select("li.o-chart-results-list__item h3.c-title")

    for song in song_elements:
        title = song.get_text(strip=True)
        all_songs.append(title)

except Exception as e:
    print(f"❌ Scraper barrier: {e}")

all_songs = all_songs[:100]

with open(TXT_FILE_PATH, mode="w", encoding="utf-8") as file:
    for song in all_songs:
        file.write(f"{song}\n")

print("\n🎉 PHASE 1 COMPLETE: The chart data has been harvested!")
print("-" * 50)
print(f"📁 Local file written: {os.path.basename(TXT_FILE_PATH)}")
print(f"🔢 Total tracks captured: {len(all_songs)}")
if all_songs:
    print(f"🔝 Current Number 1: {all_songs[0]}")
else:
    print("🔝 Current Number 1: N/A (List is still empty)")
print("-" * 50)

from ytmusicapi import YTMusic
print(f"🔎 Python is looking inside this directory: {CURRENT_DIR}")
print(f"📂 Files actually inside this directory: {os.listdir(CURRENT_DIR)}")


yt = YTMusic(os.path.join(CURRENT_DIR, "browser.json"))

print("\n🔍 Reading harvested tracks out of songs.txt...")
search_queries = []
with open(TXT_FILE_PATH, mode="r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            search_queries.append(line.strip())

video_ids = []
print("⚡ Searching YouTube Music... (This might take a minute)")
for index, query in enumerate(search_queries, start=1):
    try:
        search_results = yt.search(query=query, filter="songs", limit=1)
        if search_results:
            v_id = search_results[0]['videoId']
            video_ids.append(v_id)
            print(f"✅ [{index}/100] Found: {query}")
        else:
            print(f"⚠️ Track missing on YT Music: {query}")
    except Exception as e:
        print(f"❌ Error searching for '{query}': {e}")

if video_ids:
    print("\n🎵 Spawning your Year 2000 Billboard Hits Playlist...")
    playlist_id = yt.create_playlist(
        title="Billboard Hot 100 (2000-08-12)",
        description="Harvested and compiled flawlessly using Python web scraping utilities."
    )

    yt.add_playlist_items(playlistId=playlist_id, videoIds=video_ids)
    print(f"🎉 SUCCESS! Added {len(video_ids)} tracks onto your music library!")



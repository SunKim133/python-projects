'''
This project scrapes Billboard Top 100 of a certain date that the user want, and make a Spotify playlist with them.
For making the authentication easier, I used Spotipy library.
'''

# Importing relevant libraries
import requests
import re
import os
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Authentication using Spotipy library
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope='playlist-modify-private',
        redirect_uri='http://example.com',
        client_id = os.environ.get('SPOTIPY_CLIENT_ID'),
        client_secret = os.environ.get('SPOTIPY_CLIENT_SECRET'),
        show_dialog = True,
        cache_path = 'token.txt',
        username = os.environ.get('SPOTIPY_USER_NAME')
    )
)
user_id = sp.current_user()['id']

def is_valid_date(date_str):
    date_pattern = r"^(?:19|20)\d\d-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$"

    if re.match(date_pattern, date_str):
        return True
    else:
        return False

while True:
    date_input = input('Which year do you want to know about? Type the date in this format YYYY-MM-DD: ')

    if is_valid_date(date_input):
        playlist = sp.user_playlist_create(user=user_id, name=f"{date_input} Billboard 100", public=False)
        url = f"https://www.billboard.com/charts/hot-100/{date_input}/"
        response = requests.get(url=url)
        website_html = response.text
        soup = BeautifulSoup(website_html, 'html.parser')
        first_song = soup.find(name='h3', id='title-of-a-story',
                               class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 u-font-size-23@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-245 u-max-width-230@tablet-only u-letter-spacing-0028@tablet')
        rest_of_songs = soup.find_all(name='h3', id='title-of-a-story',
                                      class_='c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis u-max-width-330 u-max-width-230@tablet-only')
        song_titles = []
        song_titles.append(first_song.getText())
        for song in rest_of_songs:
            song_titles.append(song.getText())

        titles = []
        song_uris = []
        for song in song_titles:
            titles.append(song.replace('\t', '').replace('\n', ''))
        year = date_input.split('-')[0]
        for song in titles:
            result = sp.search(q=f'track:{song} year:{year}', type='track')
            try:
                uri = result['tracks']['items'][0]['uri']
                song_uris.append(uri)
            except IndexError:
                print(f"{song} doesn't exist in Spotify. Skipped.")
        sp.playlist_add_items(playlist_id=playlist['id'], items=song_uris)
        break

    else:
        print("Invalid date format. Please try again.")
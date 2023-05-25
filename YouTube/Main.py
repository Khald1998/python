import time
import requests
from whatsapp_api import WhatsappAPI  # Pseudocode

# The channel ID of the YouTube channel
channel_id = 'UCGardgJO7knZfeoroFDAeow' #'YOUR_CHANNEL_ID'
# Your YouTube Data API key
youtube_api_key = 'AIzaSyBEeWUn_Q8LTz84NqcaL8_ZsSL3eg9yeWc'#'YOUR_YOUTUBE_API_KEY'
# Your WhatsApp Business API key
whatsapp_api_key = 'YOUR_WHATSAPP_API_KEY'

# The ID of the last video
last_video_id = None

while True:
    # Get the list of videos from the YouTube channel
    # response = requests.get(
    #     'https://www.googleapis.com/youtube/v3/search',
    #     params={
    #         'key': youtube_api_key,
    #         'channelId': channel_id,
    #         'part': 'snippet',
    #         'order': 'date',
    #         'maxResults': 1
    #     }
    # )
    # response_json = response.json()
    
    # Check if a new video has been uploaded
    # video_id = response_json['items'][0]['id']['videoId']
    # if video_id != last_video_id:
    #     last_video_id = video_id

    # Send a WhatsApp message
    WhatsappAPI.send_message(
        api_key=whatsapp_api_key,
        phone_number='PHONE_NUMBER',
        message='A new video has been uploaded. https://www.youtube.com/watch?v=' #+ video_id
    )

    # Wait for a while before checking again
    time.sleep(60)

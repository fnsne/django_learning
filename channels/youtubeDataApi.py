import requests
import json
from channels.models import Channel
from apiclient.discovery import build

key='AIzaSyAKT1F_tqa8yWFXD70S9dhHpvz9GPGH9kI'
URL = "https://www.googleapis.com/youtube/v3/channels"

class ChannelInfo:
    def __init__(self, title, country, subscriberCount):
        self.title = title
        self.country = country
        self.subscriberCount = subscriberCount

    def getTitle(self):
        return self.title

    def getCountry(self):
        return self.country

    def getSubscriberCount(self):
        return self.subscriberCount

    def writeToDataBase(self):
        ch = Channel(name=self.title, country=self.country, subscriberCount=self.subscriberCount)
        ch.save()

def getChannelById(id):
    params = {'key':key,'part':'snippet,statistics', 'id':id}
    response = requests.get(URL, params=params)
    body = json.loads(response.text)
    title = body['items'][0]['snippet']['title']
    country = body['items'][0]['snippet']['country']
    subscriberCount = body['items'][0]['statistics']['subscriberCount']

    return ChannelInfo(title, country, subscriberCount)


def get_youtubeApiService():
    return build('youtube', 'v3', developerKey='AIzaSyAKT1F_tqa8yWFXD70S9dhHpvz9GPGH9kI')

def getChannelById(client, channelId):
    response = client.channels().list(part='snippet,statistics', id=channelId).execute()
    title = response['items'][0]['snippet']['title']
    country = response['items'][0]['snippet']['country']
    subscriberCount = response['items'][0]['statistics']['subscriberCount']

    return  ChannelInfo(title, country, subscriberCount)

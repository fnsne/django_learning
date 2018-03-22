from django.test import TestCase
import channels.youtubeDataApi as youtube
import json
from channels.models import Channel
# Create your tests here.

class youtubeDataApiTestCase(TestCase):
    def setUp(self):
        channelInfo = youtube.getChannelById("UCnJEWsS5agXCkqIpyHC9Grg")
        self.channelInfo = channelInfo

    def test_channelInfo_got_the_Info(self):
        self.assertEqual(self.channelInfo.getTitle(), '阿神')
        self.assertEqual(self.channelInfo.getCountry(), 'TW')

    def test_channelInfo_write_to_database(self):
        self.channelInfo.writeToDataBase()
        length = len(Channel.objects.all())
        ch = Channel.objects.get(id=length)
        self.assertEqual(ch.name, '阿神')
        self.assertEqual(ch.country, 'TW')
#test the api of google client
class youtubeDataApi2TestCase(TestCase):
    def setUp(self):
        client = youtube.get_youtubeApiService()
        self.channelInfo = youtube.getChannelByIdWithClient(client, "UCnJEWsS5agXCkqIpyHC9Grg")

    def test_channelInfo_got_the_Info(self):
        self.assertEqual(self.channelInfo.getTitle(), '阿神')
        self.assertEqual(self.channelInfo.getCountry(), 'TW')

    def test_channelInfo_write_to_database(self):
        self.channelInfo.writeToDataBase()
        length = len(Channel.objects.all())
        ch = Channel.objects.get(id=length)
        self.assertEqual(ch.name, '阿神')
        self.assertEqual(ch.country, 'TW')

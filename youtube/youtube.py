import fire
from pytube import YouTube


class YoutubeService(object):

  def download(self, url):
    YouTube(url).streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().last().download()


if __name__ == '__main__':
  fire.Fire(YoutubeService())

# Audio Cutter

* pip install pydub

###### **Linux**

**use any of the below method to install ffmpeg**
`sudo apt install ffmpeg`
`sudo snap install ffmpeg`

###### **Mac**

`brew install ffmpeg`
**If not worked use the below method**
**1\. Find the path of the binary file like**
    `usr/local/Cellar/ffmpeg/4.2.1_2/bin/ffmpeg`
**2\. add the path to the python script**
    `from pydub import AudioSegment `
    `AudioSegment.converter = '/usr/local/Cellar/ffmpeg/4.2.1_2/bin/ffmpeg'`
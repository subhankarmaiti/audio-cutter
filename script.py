from pydub import AudioSegment

audio_file_root_path = './abc.mp3'
fullAudio = AudioSegment.from_mp3(audio_file_root_path)
# Read the times.txt
with open('times.txt') as f: 
    times = f.readlines()
    times = [x.replace(u'\u200b', '').replace('\n', '').split(' ',1) for x in times]

for index in range(len(times)):
    time = times[index][0].split(':')
    title = times[index][1].strip()
    time = 3600*int(time[0]) + 60*int(time[1]) + int(time[2])
    # convert to miliseconds
    time *= 1000
    times[index] = [time,title]

for index in range(len(times)):
    if(index < len(times)-1):
        starttime = times[index][0]
        endtime = times[index+1][0]
        title = times[index][1]
        if(len(str(index))<2) :
            title = '0'+str(index)+' '+title
        else :
            title = str(index)+' '+title
        print(title)
        # extracting segment
        extract = fullAudio[starttime:endtime]
        # saving
        extract.export(title+'.mp3', format='mp3')
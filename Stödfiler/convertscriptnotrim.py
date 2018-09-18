from subprocess import call
import os

#Convert pcm to wav without trimming silence.

#sox inputfile.mp3 outputfile.mp3 silence 1 0.1 0.1% reverse silence 1 0.1 0.1% reverse
directory = "" #""#
resdirectory = "" #directory + "result/"#
concall1 = "ffmpeg -f s16be -ar 44.1k -ac 2 -i "
concall2 = " -map_channel 0.0.1 -ar 22.05k "
soxcall = " silence 1 0.1 0.1% reverse silence 1 0.1 0.1% reverse"
#iter = 0


for filename in os.listdir(directory):
    if filename.endswith(".pcm"):
        #call("ffmpeg -version", shell=True)
        call(concall1 + directory + filename +  concall2 + resdirectory + filename[0:-4] + ".wav", shell=True)
        #call("sox " + resdirectory + "tmp.wav " + resdirectory + filename[0:-4] + ".wav" + soxcall, shell=True)
        #call("rm " + resdirectory + "tmp.wav", shell=True)
        #iter += 1
        #if(iter == 10):
        #    break;
        continue
    else:
        continue

import subprocess
#from subprocess import call

#Script for listing short files and/or plotting distribution of durations

import os
import matplotlib.pyplot as plt

directory = "" #"/#
resdirectory = "" #directory + "result/"#

#iter = 0

durs = []
tot = 0
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        #call("ffmpeg -version", shell=True)
        #call(concall1 + directory + filename +  concall2 + resdirectory + "tmp.wav", shell=True)
        #call("sox " + resdirectory + "tmp.wav " + resdirectory + filename[0:-4] + ".wav" + soxcall, shell=True)
        #call("rm " + resdirectory + "tmp.wav", shell=True)
        #iter += 1
        #if(iter == 10):
        firstdur = subprocess.check_output(["soxi", "-d", directory + filename])
        dur = int(firstdur[6:-4].decode('UTF-8'))
        if(dur < 4):
            print(filename + "DURATION: " + str(dur))
        durs.append(dur)
        tot += dur


        #    break;
        continue
    else:
        continue

print(tot)
plt.hist(durs, color = 'blue', edgecolor = 'black',
         bins = int(18/1))
plt.title('Histogram of durations')
plt.xlabel('Duration')
plt.ylabel('No of utterances')
#print(durs[15])
#plt.tight_layout()
plt.show()

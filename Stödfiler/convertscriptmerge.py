from subprocess import call
import os

 #This was used to merge short files together

#sox inputfile.mp3 outputfile.mp3 silence 1 0.1 0.1% reverse silence 1 0.1 0.1% reverse
directory = "" #""#
#directory + "result/"#
concall1 = "ffmpeg -f s16be -ar 44.1k -ac 2 -i "
concall2 = " -map_channel 0.0.1 -ar 22.05k "
soxcall = " silence 1 0.1 0.3% reverse silence 1 0.1 0.3% reverse"
soxsilence = " silence -l 1 0.1 1% -1 1.0 1%"
f = open("swetranscripts", "r")
batch = "6"
out = open("" + batch + ".txt", "w")
resdirectory = " + batch + "/"
#iter = 0
transcripts = {}
lines = f.readlines()
#print(lines[2011])
"""
cnt = 1
while line:
    if(cnt >= 2012 or cnt <= 2014 ):
        transcripts[cnt] = line
    cnt += 1
"""

iter = 1
filenumber = 1
for filename in os.listdir(directory):
    if filename.endswith(".wav"):
        fno = int(filename[13:-4])
        if(fno >= 3232 and fno <= 3269):
            print(int(filename[13:-4]))
            print(filename + "|" + lines[fno-1])
            if(iter%2 != 0):
                previous = filename
            else:
                previousfno = int(previous[13:-4])
                call("sox " + directory + previous + " " + directory + filename
                + " " +resdirectory + "mergedbatch" + batch + "-" +str(filenumber) + ".wav" + soxsilence , shell=True)


                transline =  ("mergedbatch" + batch + "-" +str(filenumber) + "|" + lines[previousfno-1].strip("\n") +
                ". " + lines[fno-1].strip("\n") + ".|" + lines[previousfno-1].strip("\n") + ". " + lines[fno-1].strip("\n"))+ "."
                out.write(transline)
                out.write("\n")
                filenumber += 1
            iter += 1

        #print(filename)
        #call("ffmpeg -version", shell=True)
        #call(concall1 + directory + filename +  concall2 + resdirectory + "tmp.wav", shell=True)
        #call("sox " + directory + filename + " " + resdirectory + filename + soxcall, shell=True)
        #call("rm " + resdirectory + "tmp.wav", shell=True)

        #if(iter == 10):
        #    break;
        continue
    else:
        continue

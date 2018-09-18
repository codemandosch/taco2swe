
#Script to convert norweigan speech dataset transcripts to the form of LJspeech dataset.


f = open("swetranscripts", "r")
out = open("result.txt", "w")
wavdirectory = ""

basestring = ""


line = f.readline()
cnt = 1
while line:
    #print(cnt)
    if(cnt<10):
        tmp = "000"
    elif(cnt<100):
        tmp = "00"
    elif(cnt < 1000):
        tmp = "0"
    else:
        tmp = ""
    tmpline = line.strip("\n")
    result = "sw_all_mf_01_" + tmp + str(cnt) + "|" + tmpline + "|" + tmpline
    #res = result.strip('\n')

    #if(hasNumbers(line)):
    #    print(line)
    out.write(result)
    out.write("\n")
    line = f.readline()
    cnt += 1
print(cnt)
out.close()

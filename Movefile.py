import os
import sys
import re

FILEPATH = "/mnt/ProductPicture/pictest"

def GetFilesList():
    filelist = os.popen('ls '+FILEPATH)
    filelist = filelist.read()
    filelist = filelist.split("\n")
    #for i in range(len(filelist)):
    #    filelist[i] = FILEPATH + "/" + filelist[i]
    return filelist[:-1]

'''def FindDir(targetname):
    targetpath = os.popen('find /mnt/ProductPicture/ -name '+targetname)
    targetpath = targetpath.read()
    return targetpath
'''

def FindDir(targetname):
     targetpath = os.popen('find /mnt/ProductPicture/ProductPicture/ -name '+targetname)
     targetpath = targetpath.read()
     targetpath=targetpath.split("\n")
     #for i in targetpath[:-1]:
     #    checkedpath = i
     #    if re.search("recycle",i):
     #        continue
     #    else:
     #        checkedpath = i
     checkedpath=targetpath[0]
     print("targetpath: "+checkedpath)

     return checkedpath

'''def MoveFile(filelist):
    for filename in filelist:
        targetpath=FindDir(filename[:5])
        filelist = os.popen('mv '+FILEPATH+'/'+filename+' '+targetpath)
    return "done"
'''

def MoveFile(filelist):
    for filename in filelist:
        targetpath=FindDir(filename[:5])
        filelist = os.popen('cp '+FILEPATH+'/'+filename+' '+targetpath)
        print('cp '+FILEPATH+'/'+filename+' '+targetpath)
    return "done"


def main():

    print(MoveFile(GetFilesList()))
    return 0


if __name__ == "__main__":
    main()

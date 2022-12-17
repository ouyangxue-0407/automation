import os
import sys
import pandas as pd
from PIL import Image
import threading

def ReadItemNum(filename):
    f = pd.read_csv(filename, encoding="ISO-8859-1")
    values = f.iloc[:, 5]
    values = list(values)
    return values

def ReadLotsNum(filename):
    f = pd.read_csv(filename, encoding="ISO-8859-1")
    keys = f.iloc[:, 0]
    keys = list(keys)
    return keys

def CheckString(values):
    for i in range(len(values)):
        values[i] = str(values[i])
        if values[i][0]==" ":
            values[i]=values[i][1:]
        if values[i][-1]==" ":
            values[i]=values[i][:-1]
        if values[i][-1]==",":
            values[i]=values[i][:-1]
    return values

def ToDictionary(keys, values):
    dictlots = {}
    for i in range(len(keys)):
        dictlots[keys[i]] = values[i]
    return dictlots

def ReformatImage(values):
    for i in values:
        img = Image.open(i+".jpeg")
        rgb_img = img.convert('RGB')
        rgb_img.save(i+".jpg")

def GetThread1List():
    FileList = os.popen('find /mnt/ProductPicture/ProductPicture/AutoDir/ -name *.jpeg')
    FileList = FileList.read()
    FileList = FileList.split("\n")
    for i in range(len(FileList)):
        FileList[i] = FileList[i][:-5]
    numberoffile=len(FileList)
    thread1=numberoffile//3
    thread2=numberoffile//3*2
    thread1list=FileList[:thread1]
    thread2list=FileList[thread1:thread2]
    thread3list=FileList[thread2:-1]
    for i in thread1list:
        try:
            img = Image.open(i+".jpeg")
            rgb_img = img.convert('RGB')
            rgb_img.save(i+".jpg")
        except:
            errormessage=os.popen("file "+i+".jpeg")
            errormessage=errormessage.read()
            print(errormessage)

def GetThread2List():
    FileList = os.popen('find /mnt/ProductPicture/ProductPicture/AutoDir/ -name *.jpeg')
    FileList = FileList.read()
    FileList = FileList.split("\n")
    for i in range(len(FileList)):
        FileList[i] = FileList[i][:-5]
    numberoffile=len(FileList)
    thread1=numberoffile//3
    thread2=numberoffile//3*2
    thread1list=FileList[:thread1]
    thread2list=FileList[thread1:thread2]
    thread3list=FileList[thread2:-1]
    for i in thread2list:
        try:
            img = Image.open(i+".jpeg")
            rgb_img = img.convert('RGB')
            rgb_img.save(i+".jpg")
        except:
            errormessage=os.popen("file "+i+".jpeg")
            errormessage=errormessage.read()
            print(errormessage)

def GetThread3List():
    FileList = os.popen('find /mnt/ProductPicture/ProductPicture/AutoDir/ -name *.jpeg')
    FileList = FileList.read()
    FileList = FileList.split("\n")
    for i in range(len(FileList)):
        FileList[i] = FileList[i][:-5]
    numberoffile=len(FileList)
    thread1=numberoffile//3
    thread2=numberoffile//3*2
    thread1list=FileList[:thread1]
    thread2list=FileList[thread1:thread2]
    thread3list=FileList[thread2:-1]
    for i in thread3list:
        try:
            img = Image.open(i+".jpeg")
            rgb_img = img.convert('RGB')
            rgb_img.save(i+".jpg")
        except:
            errormessage=os.popen("file "+i+".jpeg")
            errormessage=errormessage.read()
            print(errormessage)

def MoveFile(dictlots):
    dictforcsv={}
    space=""
    namelist=[]
    for key in dictlots.keys():
        path = os.popen('find /mnt/ProductPicture/ProductPicture -name ' + str(dictlots[key]))
        path = path.read()
        path = path.split("\n")
        path = path[0]
        print("path: "+path)
        numberofpicture = os.popen('ls ' + str(path))
        numberofpicture = numberofpicture.read()
        numberofpicture = numberofpicture.split("\n")
        numberofpicture = len(numberofpicture) - 1
        print("numberofpicture: "+str(numberofpicture))
        filenames = os.popen('ls ' + str(path))
        filenames = filenames.read()
        filenames = filenames.split("\n")
        filenames = filenames[: -1]
        for index in range(30):
            namelist.append(space)
        dictforcsv[key]=[]
        for num in range(numberofpicture):
            os.system("cp " + str(path) + "/" + str(filenames[num]) + " " + "/mnt/ProductPicture/ProductPicture/AutoDir/" + str(key) + "_" + str(num+1) + ".jpeg")
            namelist[num]= str(key)+"_"+str(num+1)+".jpg"
        for index in range(30):
            dictforcsv[key].append(namelist[index])
        namelist=[]
    tocsv = pd.DataFrame(dictforcsv)
    data = tocsv.values
    data = list(map(list,zip(*data)))
    data = pd.DataFrame(data)
    data.to_csv("/mnt/ProductPicture/ProductPicture/AutoDir/Auto.csv",header=0,index=0)
def main():
    lots = ReadLotsNum(sys.argv[1])
    items = CheckString(ReadItemNum(sys.argv[1]))
    dictionay = {}
    dictionay = ToDictionary(lots, items)
    print(MoveFile(dictionay))
    #thread1list, thread2list, thread3list = GetThreadList()
    t1 = threading.Thread(target=GetThread1List)
    t2 = threading.Thread(target=GetThread2List)
    t3 = threading.Thread(target=GetThread3List)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
if __name__ == '__main__':
    main()

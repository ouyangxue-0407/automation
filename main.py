import os
import sys
import pandas as pd

#抓货号输出list[str]格式的货号
def ReadItemNum(filename):
    f = pd.read_csv(filename, encoding="ISO-8859-1")
    values = f.iloc[:, 4]
    values = list(values)
    return values

#抓lots号输出list[int]格式的lots
def ReadLotsNum(filename):
    f = pd.read_csv(filename, encoding="ISO-8859-1")
    keys = f.iloc[:, 0]
    keys = list(keys)
    return keys

#货号的str格式转int
def ToInt(values):
    for i in range(len(values)):
        #取前五个characters转Int
        values[i] = values[i][0:5]
        values[i] = int(values[i])
    return values

#dictionary用的舒服,转一下
def ToDictionary(keys, values):
    dictlots = {}
    for i in range(len(keys)):
        dictlots[keys[i]] = values[i]
    return dictlots

#连复制带改名字一步到位
def MoveFile(dictlots):
    for key in dictlots.keys():
        #跟据lots号定位货号用find命令定位文件夹的绝对路径
        path = os.system('find /mnt/md0/public/ProductPicture/ -name' + str(dictlots[key]))
        #检测该文件夹里有多少张图
        numberofpicture = os.system('ls ' + str(path) + ' | wc -l')
        numberofpicture = int(numberofpicture)
        #获取该文件夹所有图片的名字（输出list）
        filenames = os.system('ls ' + str(path))
        #用cp命令复制图片到指定文件夹（TARGET_DIR_PATH/）并根据lots号重新命名（cp （find找到的绝对路径）/（图片名字） （指定文件夹/）（lots号_第几张图.jpeg)
        for num in range(1, numberofpicture+1):
            os.system('cp ' + str(path) + '/' + str(filenames[num]) + ' ' + 'TARGET_DIR_PATH/' + str(key) + '_' + str(num) + '.jpeg')
        return "Finish"


if __name__ == '__main__':
    lots = ReadLotsNum(sys.argv(1))
    items = ToInt(ReadItemNum(sys.argv(1)))
    dictionay = {}
    dictionay = ToDictionary(lots, items)
    print(MoveFile(dictionay))

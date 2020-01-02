from sklearn.model_selection import train_test_split

import numpy as np
import random
import pandas as pd
import os
from shutil import copy


def getfileFromfilter(rootdir):
    import os
    list = os.listdir(rootdir)
    ReturnList=[]
    for i in range(0, len(list)):
        if list[i]!='.DS_Store':

            path = os.path.join(rootdir, list[i])
            ReturnList.append(path)
    return (ReturnList)

counter=0
imagedata=[]
Oneshotdata=[]
traindata=[]
list=getfileFromfilter("Omniglot Dataset/images_background")
characternumber=0
for eachlanguage in list:
    character=getfileFromfilter(eachlanguage)
    for eachcharacter in character:
        imagelist=getfileFromfilter(eachcharacter)
        characternumber+=1
        a_train, a_test = train_test_split(imagelist, test_size=0.05)

        Oneshotdata.append(a_test[0].split('/')[-1])
        copy(a_test[0],'oneShot_Data/'+a_test[0].split('/')[-1])
        for eachtest in a_train:
            traindata.append(eachtest.split('/')[-1])
            copy(eachtest, 'testdata/' + eachtest.split('/')[-1])
        #for eachImage in imagelist:
            #split=eachImage.split('/')
            #imagedata.append([split[-1].split('.')[0],split[-1], split[-3], split[-2],characternumber])



        counter+=1


list=getfileFromfilter("Omniglot Dataset/images_evaluation")

for eachlanguage in list:
    character = getfileFromfilter(eachlanguage)
    for eachcharacter in character:
        imagelist = getfileFromfilter(eachcharacter)
        characternumber += 1
        a_train, a_test = train_test_split(imagelist, test_size=0.05)
        Oneshotdata.append(a_test[0].split('/')[-1])
        copy(a_test[0], 'oneShot_Data/' + a_test[0].split('/')[-1])
        for eachtest in a_train:
            traindata.append(eachtest.split('/')[-1])
            copy(eachtest, 'testdata/' + eachtest.split('/')[-1])
        #for eachImage in imagelist:
            #split = eachImage.split('/')
            #imagedata.append([split[-1].split('.')[0],split[-1], split[-3], split[-2],characternumber])

        counter += 1
print(Oneshotdata)
print(traindata)

df = pd.DataFrame(Oneshotdata, columns=['image_path'])
df.to_csv("oneshot.csv")
df = pd.DataFrame(traindata, columns=['image_path'])
df.to_csv("onshotTest.csv")
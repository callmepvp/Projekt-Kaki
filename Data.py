import os
import json

defaultCacheBody = {
    "programmiInfo" : {
        "font" : "Gogh-ExtraBold.ttf",
        "primaryColor" : 0,
        "secondaryColor" : 0
    },

    "sündmused" : {
    
    }
}

indent = 4 #json indent formatting

indexDirectory = os.path.dirname(__file__) #Python scripti relatiivne path
dataDirectory = os.path.join(indexDirectory, 'Data/data.json')
cacheDirectory = os.path.join(indexDirectory, 'Data/cache.json')

testingMode = False

#Salvestamiseks
def SalvestaFaili():
    #salvestab alati cache faili data faili
    with open(cacheDirectory, encoding="utf-8") as cache:
        tempData = json.load(cache)

    tempData = json.dumps(tempData, indent=indent, ensure_ascii=False)
    with open(dataDirectory, "w", encoding="utf-8") as f:
        f.write(tempData)

    os.remove(cacheDirectory) #removes the cache fail

def SalvestaCache(cacheObject: str):
    cacheObject = json.dumps(cacheObject, indent=indent, ensure_ascii=False)
    with open(cacheDirectory, "w", encoding="utf-8") as f:
        f.write(cacheObject)



#Laadimiseks
def VõtaCache(andmeteTüüp: str):
    with open(cacheDirectory, encoding="utf-8") as f:
        info = json.load(f)

    return info[andmeteTüüp]

def VõtaData(andmeteTüüp: str):
    with open(dataDirectory, encoding="utf-8") as f:
        info = json.load(f)

    return info[andmeteTüüp]



#Teatud infojuppide võtmiseks data failist
def VõtaProgrammiInfo():
    if os.path.isfile(dataDirectory):
        #Data fail on olemas
        SalvestaCache(defaultCacheBody)
        info = VõtaData("programmiInfo")

    else:
        #Pole data faili
        SalvestaCache(defaultCacheBody)
        info = VõtaCache("programmiInfo")

    return info
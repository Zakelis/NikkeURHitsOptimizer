from datetime import datetime, timezone


def writeCurrentUTCTime():
    utc_now = datetime.now(timezone.utc)  # Récupère l'heure actuelle en UTC
    formatted_time = utc_now.strftime("%Y-%m-%d %H:%M:%S UTC+0")  # Formate la date
    print(f"Runtime Date : {formatted_time}")

def getReversedList(l):
    return l[::-1]

def filterSubList(ref, toKeep):
    refSet = set(ref)
    setToKeep = set(toKeep)
    return [elem for elem in refSet if elem not in setToKeep]

def getLastListItem(listData):
    return listData[-1] if listData else None

def getFirstListItem(listData):
    return listData[0] if listData else None

def getNthListItem(listData, n):
    return listData[n] if listData else None

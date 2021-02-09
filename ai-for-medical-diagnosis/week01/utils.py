import os

def csv_load(link):
    os.system('!wget ' + "'" + link + "'")
    
    return None
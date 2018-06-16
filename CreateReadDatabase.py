# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 22:48:03 2018

Taken from Python Projects

@author: SIDHARTH
"""

def createDB(data, dbName):
    try:
        db = dbm.open(dbName,'c')
        for datum in data:
            db[datum[0]] = ','.join(datum)
    finally:
        db.close()
        print(dbName,'created')
        
def readDB(dbName):
    try:
        db = dbm.open(dbName,'r')
        print('Reading',dbName)
        return [db[datum] for datum in db]
    finally:
        db.close()
        
def main():
    print('Creating files')
    createDB(items,'itemdb')
    createDB(members,'memberdb')
    print('reading files')
    print(readDB('itemdb'))
    print(readDB('memberdb'))
    
if __name__ == "__main__":
    main()
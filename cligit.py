import sys
import json
import argparse
import requests
# Creating List for Dictionary from file json


def appendData(datalama, username, commands) : 
    dataBaru = {"username" : username, "commands" : commands}
    print(dataBaru)
    datalama["Users"].append(dataBaru)
    
    print(datalama)
    return datalama

 
# Initial Creating File
def createfileJson(username, commands):
    try:
        with open('data.json', 'r') as json_file:
            datalama = json.load(json_file)
            print(f"ini adalah data lama : {datalama}")
            
    except:
        with open('data.json', 'w') as json_file:
            datalama = {
                "Users": [
                    {

                    }
                ]
            }
            json.dump(datalama, json_file, indent=4)

    return datalama

               
# Write File into Json
def writeFileJson(deData):
    # createList(deData, datalama)
    with open('data.json', 'w') as json_file:
        json.dump(deData,json_file, indent=4 )

    
    
#Insert Data Checker
def insertData(datalama, username, command):
    print(f" Memproses informasi dengan username {username} dan command {command} pada github ")
    if datalama : 
        user_json = appendData(datalama , username, command)
        return user_json

    else : 
        print("data kosong")


def fetch(username):
    url = f"https://api.github.com/users/{username}"
    responses = requests.get(url)

    if responses.status_code == 200 :
        data = responses.json()
        print(data)
    else :
        print(f"Error  : {responses.status_code}")

        
def main():
    # Showing args 
    if len(sys.argv) < 3 :
        print("Usage : python cliapp.py <username> <command> ")
        sys.exit(1)

    # Checking and Load saved file data
    username = sys.argv[1]
    commands = sys.argv[2]
    # datalama = createfileJson(username, commands)                 # Dinyalakan kembali setelah update 2.0.0 API Git
    # # Output sys.argv
    # updatedData = insertData(datalama, sys.argv[1], sys.argv[2])  # Dinyalakan kembali setelah update 2.0.0 API Git
    # writeFileJson(updatedData)


if __name__ == "__main__" :
    main()
    

    


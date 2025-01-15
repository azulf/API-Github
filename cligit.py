import sys
import json
import argparse
import requests
# Creating List for Dictionary from file json

aart = r""" ______                       _______                _     _               
(______)         _           (_______)      _       | |   (_)              
 _     _ _____ _| |_ _____    _____ _____ _| |_ ____| |__  _ ____   ____   
| |   | (____ (_   _|____ |  |  ___) ___ (_   _) ___)  _ \| |  _ \ / _  |  
| |__/ // ___ | | |_/ ___ |  | |   | ____| | |( (___| | | | | | | ( (_| |  
|_____/ \_____|  \__)_____|  |_|   |_____)  \__)____)_| |_|_|_| |_|\___ |  
                     _              _______             _         (_____|  
                    | |            (_______)           | |                 
                    | |__  _   _    _______  ____ _____| |__  _____  ___   
                    |  _ \| | | |  |  ___  |/ ___|___  )  _ \| ___ |/___)   
                    | |_) ) |_| |  | |   | | |    / __/| | | | ____|___ |  
                    |____/ \__  |  |_|   |_|_|   (_____)_| |_|_____|___/   
                          (____/                                           """


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
    headers = {'Authorization' : 'token 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'}
    url = f"https://api.github.com/users/{username}/events"
    try :
        responses = requests.get(url, headers = headers)
        print(f"Status Code: {responses.status_code}")
        # print(f"Response Content: {responses.text}")  # Untuk debug
        responses.raise_for_status()

        # Parsing hasil JSON
        events = responses.json()
        for event in events[:10]:
            event_type = event.get("type", "Unknown")
            repo_name = event["repo"]["name"] if "repo" in event else "Unknown repo"
            print(f"- {event_type} on {repo_name}")

        
        
    except requests.exceptions.HTTPError as http_err :
        print(f"HTTP error : {http_err}")

    except Exception as err:
        print(f"an Error occured : {err}")
    
def optionCommand() :
    print("")

        
def main():
    # Showing args 
    if len(sys.argv) < 3 :
        print(aart)
        print("Usage    : python cliapp.py <username> <command> ")
        print("Help     : python cliapp.py <help>")
 
        sys.exit(1)

    # Checking and Load saved file data
    username = sys.argv[1]
    commands = sys.argv[2]
    # datalama = createfileJson(username, commands)                 # Dinyalakan kembali setelah update 2.0.0 API Git
    # # Output sys.argv
    # updatedData = insertData(datalama, sys.argv[1], sys.argv[2])  # Dinyalakan kembali setelah update 2.0.0 API Git
    # writeFileJson(updatedData)                                    # Dinyalakan kembali setelah update 2.0.0 API Git
    fetch(username)


if __name__ == "__main__" :
    main()
    

    


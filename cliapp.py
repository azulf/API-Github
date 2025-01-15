import sys
import json
import argparse
# Creating List for Dictionary from file json

# def createList(username, commands):
    # json_string = '{"Users":  [{"username": "' + username + '", "commands":"' + commands + '"}]}'
    # return json_string

def cli_parser():
    parser = argparse.ArgumentParser(description="Process username and commands into JSON")
    parser.add_argument("Username", type=str, help="Username of the Users")
    parser.add_argument("Commands", type=str, help="Command issued by Users")
    return parser


# Initial Creating File
def createfileJson():
    try:
        with open('data.json', 'r') as json_file:
            datalama = json.load(json_file)
            print(f"ini adalah data lama : {datalama}")

    except:
        with open('data.json', 'w') as json_file:
            datalama = [{}]
            json.dump(datalama, json_file, indent=4)
    return datalama

               
# Write File into Json
def writeFileJson(deData):
    # createList(deData, datalama)
    with open('data.json', 'w') as json_file:
        json.dump(deData,json_file, indent=4 )

    
    
# Insert Data Checker
# def insertData(datalama,username, command):
#     print(f" Memproses informasi dengan username {username} dan command {command} pada github ")
#     user_json = createList(username, command)
#     data = f'"Users" = [{ "Username" : {username}}]'
#     print(data)
#     # writeFileJson(data)
    
        
def main():
    # Showing args 
    if len(sys.argv) < 3 :
        print("Usage : python cliapp.py <username> <command> ")
        sys.exit(1)
    parser = cli_parser()
    args = parser.parse_args()
    # args = parser.parse_args()
    user_data = { 
        "Users": [ 
            {"username": args.Username, "commands": args.Commands} ] 
        } 

    writeFileJson(user_data)
    print(user_data)
    # Output sys.argv
    # insertData(datalama, sys.argv[1], sys.argv[2])
    


if __name__ == "__main__" :
    # datalama = createfileJson() 
    # createList(data)
    main()
    

    


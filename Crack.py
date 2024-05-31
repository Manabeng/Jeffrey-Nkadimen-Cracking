import requests
import json
import os

BASE_URL = "https://graph.facebook.com/"
token = ""

def show_menu():
    print("\nJ E F F R E Y -- N K A D I M E N G.")
    print("--------------------------------------------------")
    print("➤ Author   : Jeffrey-Nkadimeng")
    print("➤ Github   : https://github.com/Manabeng")
    print("➤ Whatsapp : +27737093460")
    print("➤ Facebook : Jeffrey Nkadimeng")
    print("--------------------------------------------------")
    print("[1]-⋄- Clone from public friends")
    print("[2]-⋄- Crack from public followers")
    print("[3]-⋄- Multi cracking from public Id [Pro]")
    print("[4]-⋄- Check crack results")
    print("[5]-⋄- User-agent settings [PRO]")
    print("[6]-⋄- Exit [ remove-token]")

def handle_public(scanner):
    target_id = input("Enter Target ID: ")
    try:
        response = requests.get(BASE_URL + target_id + "/friends?access_token=" + token)
        json_response = response.json()
        data = json_response["data"]
        for friend in data:
            id.append(friend["id"] + "<=>" + friend["name"].split(" ")[0])
        print("Total ID:", len(id))
    except Exception as e:
        print("Error:", e)

def handle_followers(scanner):
    target_id = input("Enter Target ID: ")
    try:
        response = requests.get(BASE_URL + target_id + "/subscribers?limit=5000&access_token=" + token)
        json_response = response.json()
        data = json_response["data"]
        for follower in data:
            id.append(follower["id"] + "<=>" + follower["name"].split(" ")[0])
        print("Total ID:", len(id))
    except Exception as e:
        print("Error:", e)

def handle_massal(scanner):
    number_of_ids = int(input("Enter number of IDs: "))
    for i in range(1, number_of_ids + 1):
        target_id = input("Enter Target ID {}: ".format(i))
        try:
            response = requests.get(BASE_URL + target_id + "/friends?access_token=" + token)
            json_response = response.json()
            data = json_response["data"]
            for friend in data:
                id.append(friend["id"] + "<=>" + friend["name"].split(" ")[0])
        except Exception as e:
            print("Error:", e)
    print("Total ID:", len(id))

def check_results(scanner):
    print("[1]-⋄- Check results OK")
    print("[2]-⋄- Check results CP")
    choice = int(input("[+] Option: "))
    if choice == 1:
        check_ok_results(scanner)
    elif choice == 2:
        check_cp_results(scanner)
    else:
        print("Invalid choice")

def check_ok_results(scanner):
    ok_dir = "OK"
    if os.path.exists(ok_dir) and os.path.isdir(ok_dir):
        print("Copy file name and paste into input:")
        files = os.listdir(ok_dir)
        if files:
            for file in files:
                print("[•]", file)
            file_name = input("[+] File name: ")
            file_path = os.path.join(ok_dir, file_name)
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    for line in f:
                        print(line.strip())
            else:
                print("File does not exist")
    else:
        print("OK directory does not exist")

def check_cp_results(scanner):
    cp_dir = "CP"
    if os.path.exists(cp_dir) and os.path.isdir(cp_dir):
        print("Copy file name and paste into input:")
        files = os.listdir(cp_dir)
        if files:
            for file in files:
                print("[•]", file)
            file_name = input("[+] File name: ")
            file_path = os.path.join(cp_dir, file_name)
            if os.path.exists(file_path):
                with open(file_path, "r") as f:
                    for line in f:
                        print(line.strip())
            else:
                print("File does not exist")
    else:
        print("CP directory does not exist")

def set_user_agent(scanner):
    user_agent = input("Enter user-agent: ")
    try:
        with open(".ua", "w") as f:
            f.write(user_agent)
    except Exception as e:
        print("Error saving user-agent:", e)

def load_token():
    global token
    try:
        with open("login.txt", "r") as f:
            token = f.readline().strip()
    except Exception as e:
        print("Token Error:", e)

if __name__ == "__main__":
    load_token()
    while True:
        show_menu()
        choice = int(input("[+] Option: "))
        if choice == 1:
            handle_public(None)
        elif choice == 2:
            handle_followers(None)
        elif choice == 3:
            handle_massal(None)
        elif choice == 4:
            check_results(None)
        elif choice == 5:
            set_user_agent(None)
        elif choice == 6:
            break
        else:
            print("Invalid choice")
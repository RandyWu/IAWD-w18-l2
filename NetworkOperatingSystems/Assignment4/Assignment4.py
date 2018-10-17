import os, crypt

def create_user(user_name, password):

    os.system("sudo useradd -p " + password + " -d /home/" + user_name + " -m -c '" + user_name + "' " + user_name)
    os.system("sudo chown " + user_name + ":" + user_name + " /home/" + user_name)
    os.system("sudo usermod -a -G cst8254 " + user_name)

def print_groups(user_name):
    os.system("groups " + user_name)

def remove_user(user_name):
    os.system("sudo userdel -r " + user_name)

def generate_user_dict(file_name):
    with open(file_name,"r") as user_accounts:
        user_list = user_accounts.read().splitlines()

    password_list = list()

    for element in user_list:
        password_list.append(crypt.crypt(element))
        user_dict = dict(zip(user_list,password_list))

    return user_dict

def main():
    user_dict = generate_user_dict("listAccounts.txt")
    while (True):
        choice = input("""What would you like to do?

        D or d to delete previous entries
        C or c to create users
        X or x to exit
        """).upper()
        if (choice == "D"):
            for key in user_dict:
                remove_user(key)
        elif (choice == "C"):
            for key in user_dict:
                create_user(key,user_dict[key])

            print("\nHere are the groups each user belongs too\n")
            for key in user_dict:
                    print_groups(key)
        else:
            break

main()

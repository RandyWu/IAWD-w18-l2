import os

def check_directory(directory_name):
    directory_list = os.listdir()
    if directory_name in directory_list:
        return true
    else:
        return false

def create_hierachy(path):

    os.chdir(os.getcwd() + "/" + path)
    os.system("mkdir labs")
    os.chdir(os.getcwd() + "/" + "labs")
    os.system("mkdir Lab1 Lab2 Lab3")

    os.chdir(os.getcwd() + "/../..")

    os.chdir(os.getcwd() + "/" + path)
    os.system("mkdir lectures")
    os.chdir(os.getcwd() + "/" + "lectures")
    os.system("mkdir Week1 Week2 Week3")

while (True):
    user_directory = input ("Please enter the name of the directory you creat the hierachy in: \n")
    if os.path.isdir(user_directory):
        create_hierachy(user_directory)
        os.system('cp ~/cst8254/linux/labs/Lab3/lab3-1.txt ~/cst8254/python/labs/Lab3')
        os.system('cp ~/cst8254/linux/labs/Lab3/lab3-2.txt ~/cst8254/python/labs/Lab3')
        break
    else:
        print("Please enter a valid directory\n")


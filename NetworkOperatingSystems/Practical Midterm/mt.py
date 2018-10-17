with open("mt2.txt","r") as netstat_file:
    netstat_list = netstat_file.read().splitlines()

with open("mt3.txt","w") as mt3:
    mt3.write(netstat_list[1])
    mt3.write("\n")
    for element in netstat_list[1:]:
        if element[:4] == 'tcp ':
            mt3.write(element)
            mt3.write("\n")

from ipaddress import IPv4Address, IPv4Network

CLASS_DICT = {
    "10.0.0.0/8" : "Class A",
    "172.16.0.0/12" : "Class B",
    "192.168.0.0/16" : "Class C"
}

SUBNET_DICT = {
    "10.0.0.0/8" : "255.0.0.0",
    "172.16.0.0/12" : "255.255.0.0",
    "192.168.0.0/16" : "255.255.255.0"
}

def ip_validate (ip):
    try:
       ip = IPv4Address(ip)
       return True
    except ValueError:
       return False

def get_class_of_ip (ip):
    compare_ip = IPv4Address(ip)

    for network, class_type in CLASS_DICT.items():
        if compare_ip in IPv4Network(network):
            return class_type

def get_default_mask (ip):
    compare_ip = IPv4Address(ip)

    for network, subnet_mask in SUBNET_DICT.items():
        if compare_ip in IPv4Network(network):
            return subnet_mask

def get_network_number (ip, mask):
    ip_split = ip.split(".")
    mask_split = mask.split(".")

    # Fills the list with the result of the IP and the MASK
    result_list = [str(int(ip_split[x]) & int(mask_split[x])) for x in range(0, len(ip_split))]

    return ".".join(x for x in result_list)

def get_host_id (ip, mask):
    ip_split = ip.split(".")
    mask_split = mask.split(".")

    # Fills the list with 0 if the AND between the IP and MASK is true, else fills with the IP
    result_list = ["0" if int(ip_split[x]) & int(mask_split[x]) else ip_split[x] for x in range(0, len(ip_split))]

    return ".".join(x for x in result_list)

def main ():
    while True:
        user_input = input("Please type in a IPv4 address: ")

        if (ip_validate(user_input)):
            user_class = get_class_of_ip(user_input)
            user_subnet = get_default_mask(user_input)
            user_network_id = get_network_number(user_input, user_subnet)
            user_host_id = get_host_id(user_input, user_subnet)

            print ("\n{} is a {} address with a default subnet mask of {}".format(user_input, user_class, user_subnet))
            print ("The Network ID is {} and Host ID is {}\n".format(user_network_id, user_host_id))

            choice = input("Would you like to continue (Y or N)? ").upper()
            if choice != 'Y' :
                break

        else:
            print ("Please input a valid IPv4 address!")

main()

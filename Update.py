# Update a list of allowed IP addresses:

from colorama import Fore, Style


def load_ips(import_file):
    try:
        with open(import_file, "r") as f:

            ip_addresses = []

            for line in f:
                cleaned_line = line.strip()

                if cleaned_line:
                    ip_addresses.append(cleaned_line)

            return ip_addresses

    except FileNotFoundError:
        return []

def save_ips(import_file, ip_addresses):
    with open(import_file, "w") as f:
        f.write("\n".join(ip_addresses) + "\n")

def update_list(import_file, input_addresses, mode):
    ip_addresses = load_ips(import_file)

    if mode == "add":
        for ip in input_addresses:
            if ip and ip not in ip_addresses:
                ip_addresses.append(ip)

    elif mode == "remove":
        ip_addresses = [ip for ip in ip_addresses if ip not in input_addresses]

    save_ips(import_file, ip_addresses)

def main():

    hub = str(input(
                    "Type any of these letters to select a mode to update the list of IP addresses:\n " +
                    "'A' or 'a' --> Add an IP address\n " +
                    "'B' or 'b' --> Remove an IP address\n " +
                    "'Quit or 'quit' --> Quit\n " +
                    "Enter: "
                    ))

    while hub.lower() != "quit":

        if hub == "A" or hub == "a":
            # A
            nav = "go"
            while nav == "go" or nav == "Go":
                lst = input("Enter a list of IP addresses to add separated by spaces: ")
                lst = list(map(str.strip, lst.split(" ")))
                update_list("ip_addresses.txt", lst, "add")

                nav = str(input("Run again? Type 'Go' or 'go' to run again. Type anything else to continue: "))

            hub = str(input(
                "Type any of these letters to select a mode to update the list of IP addresses:\n " +
                "'A' or 'a' --> Add an IP address\n " +
                "'B' or 'b' --> Remove an IP address\n " +
                "'Quit or 'quit' --> Quit\n " +
                "Enter: "
            ))

        elif hub == "B" or hub == "b":
            nav = "go"
            while nav == "go" or nav == "Go":
                lst = input("Enter a list of IP addresses to delete separated by spaces: ")
                lst = list(map(str.strip, lst.split(" ")))
                update_list("ip_addresses.txt", lst, "remove")

                nav = str(input("Run again? Type 'Go' or 'go' to run again. Type anything else to continue: "))

            hub = str(input(
                "Type any of these letters to select a mode to update the list of IP addresses:\n " +
                "'A' or 'a' --> Add an IP address\n " +
                "'B' or 'b' --> Remove an IP address\n " +
                "'Quit or 'quit' --> Quit\n " +
                "Enter: "
            ))

        elif hub == "Quit" or hub == "quit":
            break

        else:
            print(Fore.RED + "----- Error: Invalid input. Try again. -----" + Style.RESET_ALL)

            hub = str(input(
                "Type any of these letters to select a mode to update the list of IP addresses:\n " +
                "'A' or 'a' --> Add an IP address\n " +
                "'B' or 'b' --> Remove an IP address\n " +
                "'Quit or 'quit' --> Quit\n " +
                "Enter: "
            ))

if __name__ == '__main__':
    main()

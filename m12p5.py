
def load_data(filename, names, averages):
    infile = open(filename, "r")
    for line in infile:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            names.append(parts[0])
            averages.append(float(parts[1]))
    infile.close()

def display_players(names, averages):
    print("Player      Average")
    for i in range(len(names)):
        print(f"{names[i]:<12}{averages[i]:.3f}")

def search_player(names, averages, search_name):
    found = False
    for i in range(len(names)):
        if names[i] == search_name:
            print(f"{names[i]} - {averages[i]:.3f}")
            found = True
    if found == False:
        print("Name not found")

def main():
    names = []
    averages = []
    load_data("players.txt", names, averages)
    display_players(names, averages)
    print()

    search_name = input("Enter a last name to search (or 'quit' to stop): ")
    while search_name != "quit":
        search_player(names, averages, search_name)
        search_name = input("Enter a last name to search (or 'quit' to stop): ")

main()
def load_data(filename, names, averages):
    infile = open(filename, "r")
    for line in infile:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            names.append(parts[0])
            averages.append(float(parts[1]))
    infile.close()

def display_players(names, averages):
    print("Player      Average")
    for i in range(len(names)):
        print(f"{names[i]:<12}{averages[i]:.3f}")

def search_player(names, averages, search_name):
    found = False
    for i in range(len(names)):
        if names[i] == search_name:
            print(f"{names[i]} - {averages[i]:.3f}")
            found = True
    if found == False:
        print("Name not found")

def main():
    names = []
    averages = []
    load_data("players.txt", names, averages)
    display_players(names, averages)
    print()

    search_name = input("Enter a last name to search (or 'quit' to stop): ")
    while search_name != "quit":
        search_player(names, averages, search_name)
        search_name = input("Enter a last name to search (or 'quit' to stop): ")

main()
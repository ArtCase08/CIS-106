
def display_names(names):
    print("Names:")
    for i in range(len(names)):
        print(names[i])

def display_reverse(names):
    print("Names in reverse order:")
    i = len(names) - 1
    while i >= 0:
        print(names[i])
        i = i - 1

def main():
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
                  "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    display_names(last_names)
    print()
    display_reverse(last_names)

main()

def display_names(names, scores):
    print("Name        Score")
    for i in range(len(names)):
        print(f"{names[i]:<12}{scores[i]}")

def display_reverse(names, scores):
    print("Reverse order:")
    print("Name        Score")
    i = len(names) - 1
    while i >= 0:
        print(f"{names[i]:<12}{scores[i]}")
        i = i - 1

def main():
    last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones",
                  "Garcia", "Miller", "Davis", "Rodriguez", "Martinez"]
    scores = [88, 92, 75, 64, 99, 81, 70, 95, 58, 86]
    display_names(last_names, scores)
    print()
    display_reverse(last_names, scores)

main()
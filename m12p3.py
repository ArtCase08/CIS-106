
def load_data(filename, names, scores):
    infile = open(filename, "r")
    for line in infile:
        line = line.strip()
        if line != "":
            parts = line.split(",")
            names.append(parts[0])
            scores.append(int(parts[1]))
    infile.close()

def display_names(names, scores):
    print("Name        Score")
    for i in range(len(names)):
        print(f"{names[i]:<12}{scores[i]}")

def display_high_low(names, scores):
    high_var = 0
    high_index = 0
    low_var = 999
    low_index = 0
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
    print(f"Highest score: {names[high_index]} - {high_var}")
    print(f"Lowest score:  {names[low_index]} - {low_var}")

def main():
    last_names = []
    scores = []
    load_data("scores.txt", last_names, scores)
    display_names(last_names, scores)
    print()
    display_high_low(last_names, scores)

main()
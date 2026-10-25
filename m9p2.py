
def compute_batting_avg(hits, at_bats):
    if at_bats == 0:
        return 0
    return hits / at_bats

player_count = 0

response = input("Do you want to enter a player? (Yes/No): ")

while response.lower() == "yes":
    last_name = input("Enter player's last name: ")
    hits = int(input("Enter number of hits: "))
    at_bats = int(input("Enter number of at bats: "))

    avg = compute_batting_avg(hits, at_bats)
    player_count = player_count + 1

    print("Last Name:", last_name)
    print("Batting Average:", format(avg, ".3f"))
    print()

    response = input("Do you want to enter another player? (Yes/No): ")

print()
print("Number of players entered:", player_count)
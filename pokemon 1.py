from itertools import combinations
Pokedex = {
"‘Pikachu": ("Electric",),
"Charizard": ("Fire", "Flying"),
"Lapras": ("Water", "Ice"),
"Machamp": ("Fighting",),
"Mewtwo": ("Psychic", "Fighting"),
"Hoopa": ("Psychic", "Ghost", "Dark"),
"Lugia": ("Psychic", "Flying", "Water"),
"Squirtle": ("Water",),
"Gengar": ("Ghost", "Poison"),
"Onix": ("Rock", "Ground")
}
def strongest_team(Pokedex,k):
    max_count = 0
    best_team = []

    for team in combinations(Pokedex.keys(),k):
        combined_types = set()
        for pokemon in team:
            combined_types.update(Pokedex[pokemon])
    
        if len(combined_types) > max_count:
          max_count = len(combined_types)
          best_team = [(team,combined_types)]
        elif len(combined_types) == max_count :
         best_team.append([team,combined_types])   
    return best_team,max_count


k = 3
best_team,max_count = strongest_team(Pokedex,k)
print(f"The combination with max no.of {max_count} is:") 
for team, types in best_team:
    print("Team:", team, "→ Types:", types)


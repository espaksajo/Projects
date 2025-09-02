from itertools import combinations

# Pokedex given
pokedex = {
    "Pikachu": ("Electric",),
    "Charizard": ("Fire", "Flying"),
    "Lapras": ("Water", "Ice"),
    "Machamp": ("Fighting",),
    "Mewtwo": ("Psychic", "Fighting"),
    "Hoopa": ("Psychic", "Ghost", "Dark"),
    "Lugia": ("Psychic", "Flying", "Water"),
    "Squirtle": ("Water",),
    "Gengar": ("Ghost", "Poison"),
    "Onix": ("Rock", "Ground"),
}
max_types_count = 0
best_teams = None
k = 3
    # Generate all possible teams of size k
for team in combinations(pokedex.keys(), k):
        combined_types = set()
        for pokemon in team:
            combined_types.update(pokedex[pokemon])
        
        # Compare number of unique types
        if len(combined_types) > max_types_count:
            max_types_count = len(combined_types)
            best_teams = [(team, combined_types)]
        elif len(combined_types) == max_types_count:
            best_teams.append((team, combined_types))
    



# Example usage



print(f"Strongest teams with {max_types_count} unique types:")
for team, types in best_teams:
    print("Team:", team, "→ Types:", types)
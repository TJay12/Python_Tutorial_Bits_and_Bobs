import random

# Picks one random item from a sequence (like a list, tuple or string)
colors = ["red", "blue", "green"]
print(random.choice(colors))

# Dictionaries aren't sequences - they're mappings (key:value)
creatures = {
    "pixie": "low",
    "dragon": "extreme",
    "griffin": "high"
}

# dict.keys() returns a view object, not a list
# rand.choice() needs a real list or similar
# So you need to get a list of keys first
# lists(my_dict.keys()) gives us something choice() can pick from

# Assigning the variable random_creature a random choice value and turning the dictionary into a list choice() can read
random_creature = random.choice(list(creatures.keys()))
# Assigning the chosen random creatures_stats key to variable danger_level
danger_level = creatures[random_creature]
print(f"Watch out! The {random_creature} has a danger level of {danger_level}")


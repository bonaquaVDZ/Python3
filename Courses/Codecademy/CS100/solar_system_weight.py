"""This code defines a dictionary containing information about the planets in our solar system, including their mass ratios, distance from the sun, number of moons, and length of a year. It then prompts the user to choose a planet and enter their weight in kilograms. The code calculates the weight of the user on the chosen planet, relative to their weight on Earth, and outputs this information along with the distance of the planet from the sun, number of moons and the length of a year in Earth days or Earth years"""

# Planets and their relative masses are:
# Mercury    3.30 x 10^23     mass relative to Earth: 0.0553
# Venus      4.87 x 10^24     mass relative to Earth: 0.815
# Earth      5.97 x 10^24     mass relative to Earth: 1
# Mars       6.42 x 10^23     mass relative to Earth: 0.107
# Jupiter    1.90 x 10^27     mass relative to Earth: 318
# Saturn     5.68 x 10^26     mass relative to Earth: 95.2
# Uranus     8.68 x 10^25     mass relative to Earth: 14.5
# Neptune    1.02 x 10^26     mass relative to Earth: 17.1

# Define a dictionary containing information about the planets
PLANETS = {
    'mercury': {'mass_ratio': 0.0553, 'distance': '57.91 million km', 'moons': 0, 'year_length': '88 Earth days'},
    'venus': {'mass_ratio': 0.815, 'distance': '108.2 million km', 'moons': 0, 'year_length': '225 Earth days'},
    'earth': {'mass_ratio': 1, 'distance': '149.6 million km', 'moons': 1, 'year_length': '365.24 days'},
    'mars': {'mass_ratio': 0.107, 'distance': '227.9 million km', 'moons': 2, 'year_length': '1.88 Earth years'},
    'jupiter': {'mass_ratio': 318, 'distance': '778.3 million km', 'moons': 79, 'year_length': '11.86 Earth years'},
    'saturn': {'mass_ratio': 95.2, 'distance': '1.43 billion km', 'moons': 82, 'year_length': '29.46 Earth years'},
    'uranus': {'mass_ratio': 14.5, 'distance': '2.87 billion km', 'moons': 27, 'year_length': '84.01 Earth years'},
    'neptune': {'mass_ratio': 17.1, 'distance': '4.5 billion km', 'moons': 14, 'year_length': '164.8 Earth years'}
}

# Define the mass of Earth in kilograms
MASS_EARTH_KG = 5.97e24

# Define a list of valid planet names
VALID_PLANETS = ['mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune']

# Prompt the user to choose a planet
print("Please choose a planet from the following list:")
for planet_name in VALID_PLANETS:
    print(f"- {planet_name.capitalize()}")

# Prompt the user for a planet name
while True:
    planet_name = input("Enter the name of a planet in our solar system: ").lower()
    if planet_name not in PLANETS:
        print("Invalid planet name. Please enter a valid planet name.")
    else:
        break

# Prompt the user for their weight
while True:
    try:
        weight = float(input("Enter your weight in kilograms: "))
        if weight <= 0:
            print("Please enter a positive weight.")
        else:
            break
    except ValueError:
        print("Invalid input. Please enter a valid weight.")

# Calculate the weight of the planet relative to Earth
mass_ratio = PLANETS[planet_name]['mass_ratio']
planet_weight_newtons = weight * mass_ratio * 9.81
planet_weight_kg = weight * mass_ratio

# Print the results
print(f"On {planet_name.capitalize()}, your weight would be {planet_weight_kg:.2f} kilos or {planet_weight_newtons:.2f} newtons")
print(f"Distance from the sun: {PLANETS[planet_name]['distance']}")
print(f"Number of moons: {PLANETS[planet_name]['moons']}")
print(f"Length of year: {PLANETS[planet_name]['year_length']}")

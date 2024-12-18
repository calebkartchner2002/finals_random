import random

# List of possible classes in "The Finals"
classes = ['Light', 'Medium', 'Heavy']

# Updated list of guns for each class in "The Finals"
guns = {
    'Light': [
        '93R', 'Dagger', 'LH1', 'M11', 'M26 Matter', 'Recurve Bow', 
        'SH1900', 'SR-84', 'Sword', 'Throwing Knives', 'V9S', 'XP-54', 
    ],
    'Medium': [
        'AKM', 'CL-40', 'Dual Blades', 'FAMAS', 'FCAR', 
        'Model 1887', 'Pike-556', 'R.357', 'Riot Shield', 'Cerberus 12GA'
    ],
    'Heavy': [
        '.50 Akimbo', 'Flamethrower', 'KS-23', 'Lewis Gun', 'M60', 
        'MGL32', 'SA1216', 'Sledgehammer', 'Spear', 'Shak-50' 
    ]
}

def assign_random_class_and_gun():
    # Randomly select a class
    chosen_class = random.choice(classes)

    # Randomly select a gun from the chosen class
    chosen_gun = random.choice(guns[chosen_class])

    return chosen_class, chosen_gun

# Run the function and display the result
if __name__ == "__main__":
    selected_class, selected_gun = assign_random_class_and_gun()
    print(f"{selected_class} class:   {selected_gun}")

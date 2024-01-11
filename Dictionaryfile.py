# Create a dictionary
my_dictionary = {
    "name": "Bard",
    "age": 3,
    "skills": ["text generation", "translation", "code writing"],
    "interests": {"music", "art", "science"},
}

# Accessing elements by key
print(f"My name is {my_dictionary['name']}.")
print(f"I am {my_dictionary['age']} years old.")

# Looping through key-value pairs
for key, value in my_dictionary.items():
    print(f"{key}: {value}")

# Checking for key existence
if "age" in my_dictionary:
    print("Yes, 'age' is a key in the dictionary.")

# Adding new key-value pair
my_dictionary["favorite_color"] = "blue"
print(f"My favorite color is now {my_dictionary['favorite_color']}.")

# Modifying existing value
my_dictionary["skills"].append("humor detection")
print(f"My skills now include {my_dictionary['skills']}.")

# Deleting a key-value pair
del my_dictionary["interests"]
print(f"The 'interests' key has been removed.")

# Demonstrating dictionary methods
print(f"Number of keys: {len(my_dictionary)}")
print(f"Keys: {my_dictionary.keys()}")
print(f"Values: {my_dictionary.values()}")

print("This script demonstrates basic features of a Python dictionary.")
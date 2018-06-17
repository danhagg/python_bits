# Empty () mean the function requires no input
# indendent lines make up body of function
# docstrings are in triple quotes and provide function documentation
# in this case help(greet_user)
def greet_user():
    """Display a simple greeting"""
    print("Hello!")
# call function (not indented)
greet_user()

# The argument "dan" is stored in parameter "username"
# The argument is passed from a function call to a function
def greet_specific(username):
    """Greet a specific user"""
    print("Hello, " + username.title() + "!")
greet_specific('Dan')

# Passing positional "function(pos1,pos2)" arguments
def describe_dog(dog_type, dog_name):
    """Display info on dog"""
    print("\nI have a " + dog_type + ".")
    print("My " + dog_type + "'s name is " + dog_name.title())
describe_dog('maltipoo', 'Oliver')
describe_dog('collie', 'Shep')

# Passing keyword arguments
# same function as above but with name-value pairs in ANY order
describe_dog(dog_name='Izzy', dog_type='German Shepherd')

# Default values, use the = in parameter-value function call
def describe_animal(pet_name, animal_type='dog'):
    """Display info on animal"""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title())
describe_animal('Derek') # pet_name is still positional
describe_animal('Cindarella', animal_type='unicorn')

# Return values with return statement + optional argument(middle)
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        full_name = first_name + ' ' + middle_name + ' ' + last_name
    else:
        full_name = first_name + ' ' + last_name
    return full_name.title()
musician_1 = get_formatted_name('jimi', 'hendrix')
musician_2 = get_formatted_name('john', 'hooker', 'lee')
print("\n", musician_1, "\n", musician_2)

# Returning a dictionary
def build_person(first_name, last_name, age=''):
    """return a dict of info about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person
character = build_person('Keyzer', 'Soze', age=2000)
print(character)

# Using a function with a while loop
def get_formatted_name(first_name, last_name):
    """return a full name, neatly formatted."""
    full_name = first_name + ' ' + last_name
    return full_name.title()

# This is an infinite loop
# while True:
#     print("\nPlease tell me your name:")
#     f_name = input("First name: ")
#     print("(enter 'q' at any time to quit)")
#     if _f_name == 'q':
#         break
#     l_name = input("Last name: ")
#     if l_name == 'q':
#         break
#
#     formatted_name = get_formatted_name(f_name, l_name)
#     print("\nHello, " + formatted_name + "!")

# Pass list to function
def greet_users(names):
    """Print a simple greeting to each user in the list"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)

usernames = ['hannah', 'nat', 'jen']
greet_users(usernames)

# Modifying a list in a function input-output list
#Designs that need to be printed.
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
# simulate printing each design to completed_models after printing
while unprinted_designs:
    current_design = unprinted_designs.pop()
    # simulate creating a 3d print from design
    print("Printing model: " + current_design)
    completed_models.append(current_design)

# Display completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)

# reorganize above code for efficiency with 2 functions
def print_models(unprinted_designs, completed_models):
    """Simulate printing each design, until none are left.
    Move each design to printed models after printing"""
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models):
    """show all models that were printed"""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)

# body of program
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []
print_models(unprinted_designs, completed_models)
show_completed_models(completed_models)

# Preventing a function modifying a list by
# sending a copy of list to function using slice notation
# slower and uses more memory
# function_name(list_name[:])
print_models(unprinted_designs[:], completed_models)

# Passing arbitrary numbers of arguments when unknown
# *indicates make a tuple
def make_pizza(*toppings):
    """Print list of toppings that have been requested"""
    print("\nMaking a pizz with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza('pepporoni')
make_pizza('mushrooms', 'cheese')

# Mixing positional and arbitrary arguments (arbitrary arg at end)
def make_pizza(size, *toppings):
    """Print list of toppings that have been requested"""
    print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
    for topping in toppings:
        print("- " + topping)

make_pizza(16, 'pepporoni')
make_pizza(12, 'mushrooms', 'cheese')

# Using arbitrary keyword arguments **creates empty dict
def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know of user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in user_info.items():
        profile[key] = value
        return profile
user_profile = build_profile('albert', 'einstein', location='princeton', field='physics', race='jew')

print(user_profile)

# Store functions in modules and import modules to main program allows
# u to store details of programs code elsewhere and focus on higher-level logic
# allows u to reuse functions in other programs
# Import an entire modules and libraries written by others
# made a pizza.py with a function make_pizza
# import wholde module, then call module_name.fucntion_name()

import pizza
pizza.make_pizza(16, 'pepporoni')
pizza.make_pizza(12, 'mushrooms', 'feta', 'olives')

# specific function
#from module_name import function_name_1, function_name_2
from pizza import make_pizza
make_pizza(9, 'quatrro fromaggio')

# Using as to give a function an alias
# from module_name import function_name as fn
from pizza import make_pizza as mp
mp(12, 'pesto chicken')

# Using as to give module an alias
import pizza as p
p.make_pizza(20, 'buffalo chicken')

# Importing all functions in a module,
# not advised due to possible naming conflicts
# with your own function names etc
from pizza import *
make_pizza(24, 'huge')

# Styling functions
def function_name(
    paramter_1, parameter_2
    parameter_3, etc):
    function body...
# seperate diff functions by two blank lines

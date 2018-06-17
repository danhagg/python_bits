"""
Dictionary functions
cmp(dict1, dict2) Compares elements of both dict.
len(dict) Gives the total length of the dictionary items.
str(dict) Produces a printable string representation of a dictionary
type(variable) Returns the type of dictionary of the passed variable.

Dictionary methods
dict.clear() Removes all elements of dictionary dict
dict.copy() Returns a shallow copy of dictionary dict
dict.fromkeys() Create a new dictionary with keys from seq and values set to value.
dict.get(key, default=None) For key key, returns value or default if key not in dictionary
dict.has_key(key) Returns true if key in dictionary dict, false otherwise
dict.items() Returns a list of dict's (key, value) tuple pairs
dict.keys() Returns list of dictionary dict's keys
dict.setdefault(key, default=None) Similar to get(), but will set dict[key]=default if key is not already in dict
dict.update(dict2) Adds dictionary dict2's key-values pairs to dict
dict.values() Returns list of dictionary dict's values
"""

# multiple entries into dictionary and a tab indentation for first key
fav_languages = {
    'jen': 'python',
    'sarah': 'c',
    'ed': 'ruby',
    'phil': 'python',
    }

# can loop thru a dictionary "key" and "value" can be represented anyway
for key, value in fav_languages.items():
    print("\nKey: " + key)
    print("Value: " + value)

if 'erin' not in fav_languages.keys():
    print("Erin, please take poll!")

# set is similar to a list except that each item must be unique
# wrap set around list
print("set")
for lang in set(fav_languages.values()):
    print(lang.title())

new_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'ed': ['ruby', 'go'],
    'phil': ['python', 'haskell']
}
# two loops, 1st thru dict second thru list
for name, languages in new_languages.items():
    print("\n" + name.title() + "'s favorite languages are: ")
    for language in languages:
        print("\t" + language.title())

# a dict in a dict
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris', }}

for username, user_info in users.items():
    print("\nUsername: " + username)
    full_name = user_info['first'] + " " + user_info['last']
    location = user_info['location']

    print("\tFull name: " + full_name.title())
    print("\tLocation: " + location.title())

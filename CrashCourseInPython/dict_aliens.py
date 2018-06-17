# make a dictionary inside curly braces
alien_0 = {'color': 'green', "points": 5}

# get a value from dictionary using key in square brackets[]
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points")

# add new key-value pair to existing dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# Can start with an empty dictionary and add key-values to it
alien_1 = {}
alien_1['color'] = 'green'
alien_1['points'] = 5
print(alien_1)

# change a value in dictionary
alien_1['color'] = 'yellow'
print("The alien is now " + alien_1['color'] + "!")

# Give alien a key-value for speed
alien_0['speed'] = 'medium'
print("Original x-position: " + str(alien_0['x_position']))

# change alien position 'value' in dictionary based upon 'speed' value
# move alien to right based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# new position is old position plus increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("new x-position: " + str(alien_0['x_position']))

# removing key-value pairs with name of dictionary plus key
del alien_0['points']
print(alien_0)

# nesting, lists in dicts and dicts in lists
alien_4 = {'color': 'green', 'points': 5}
alien_5 = {'color': 'yellow', 'points': 10}
alien_6 = {'color': 'red', 'points': 15}
aliens = [alien_4, alien_5, alien_6]
for alien in aliens:
    print(alien)

# make an empty list for storing aliens.
aliens = []
# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

# show first 5 aliens
for alien in aliens[:5]:
    print(alien)
print("...")

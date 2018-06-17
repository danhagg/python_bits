responses ={}
# set a flag to indicate polling is active
polling_active = True
while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb? ")
    
    # store response in dictionary
    responses[name] =response
    # Find out if anyone else is going to take poll
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == 'no':
        polling_active = False
        
        # Polling is complete. Show results.
        print("\n--- Poll Results ---")
        for name, response in responses.items():
            print(name + " would like to climb " + response + ".")
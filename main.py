def say_raining():    
    temperature = input(f"What is the current temperature?")
    temperature = int(temperature)
    raining = input("Is it raining? (yes/no)")
    raining = raining.lower()
    if raining == "no" and temperature >= 20: print("Enjoy a sunny day!")
    elif raining == "yes" and temperature >= 20: print("Don't forget your umbrella!")
    elif raining == "no" and temperature < 20:  print("Don’t forget your jacket.")
    else: print("Don’t forget your umbrella and your jacket.")
    
say_raining()    
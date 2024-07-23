def div():
    print('='*50)

# Different types of parameters

# Basic parameters : assume their value from arguments passed into the defined function when it's called

def name_printer(first, middle, last):
    print(f"Hello, {first} {middle} {last}!")

#--- positional arguments : the position of the argument determines which parameter it becomes the value of in our function
name_printer("Travis", "Cline", "Peck")
name_printer("Peck", "Travis", "Cline")

#--- Keyword arguments : we can explicitly state which parameter takes which value
name_printer(last= "Peck", first="Travis", middle="Cline")

div()

#--- Default parameters : Give a parameter a default value if nothing is passed into the function

def greeting(name= "World"):
    print(f"Hello, {name}!")

greeting()
greeting("Travis")

div()

#--- *args : unknown number of arguments, brought into the function as a tuple

def vet_hands(staff, *vols):
    print(f"On staff today we have {staff[0]} and {staff[1]}!")
    if vols:
        print("They will be assisted by the following volunteers:")
        for vol in vols:
            print(vol)

vet_hands(["Dr. Adam", "Dr. Jones"], "Dylan", "Travis", "Grace", "Josh", "Walter", "Phillip")

div()

#--- **kwargs : unknown amount of keyword arguments, brought into the function as a dictionary

def routine(**daily_events):
    print(daily_events)

routine(morning= "I wake up, brush my teeth, and have breakfast", mid_morning= "Walk my dog", afternoon= "Grading and prepping for class", evening= "in class", dinner_time= "time to eat something", night= "Go to sleep")
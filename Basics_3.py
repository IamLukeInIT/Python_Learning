#if else statements
print("Hello, welcome to Luke Coffe")
name = input("What is your name?\n")

if name == "Ben":
    print("Get out from here " + name + "! \n")
else:
    print("Hello "+ name + ", thank you so much for comming in today. \n\n\n")


print("Are 4 < 3?")
if 4 < 3:
    print("Yep, it's true. \n")
else:
    print("Nope, not true. \n")    


#jeśli coś jest w zbiorze
car = input("What is your favourite car? \n")
cars = "Audi, BMW, Chevrolet" 
if car in cars:
    print("I know that car!") 
else:
    print("Oh, I don't know that car.")      
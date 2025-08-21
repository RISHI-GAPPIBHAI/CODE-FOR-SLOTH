#This is that number inversion program that sloth gave as a challenge
print("In this program,we'll invert the number that you feed,through a mirror, and check it's the same even after inversion")
print("I hope you input only numbers🙏")
input_number=input("Enter a number").strip()    #To take input from the user
the_mirrored_number=""   #To store that inverted number
for number in input_number:
    if number=="6":
        the_mirrored_number="9"+the_mirrored_number    #To invert the number
    elif number=="9":
        the_mirrored_number="6"+ the_mirrored_number    #To invert the number
    else:
        the_mirrored_number=number+the_mirrored_number
try:
    if int(the_mirrored_number) == int(input_number):
        print("The number is the same even after inversion through a mirror,that is",the_mirrored_number,"Soo,yeah,true")
    else:
        print(f"The number changes to {the_mirrored_number} after inversion through a mirror, which leaves me with the only choice of returning false🥀🥀")
except ValueError:
    print("You feed something other than numbers too didn't you?😡😡")
#BYEEEEEEEEEE SLOTHHHHHHHHH!!!!!!🙃🙃🙃🙃
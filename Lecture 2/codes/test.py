#b = ":" 
#c = ")"
#s1 = b + 2*c
#print (s1)

#f = "a"
#g = " b"
#h = "3"
#s2 = (f+g)*int(h)
#print (s2)

#s = "abc"
#len(s)
#chars = len(s)
#print(chars)

#a = "the"
#b = 3
#c = "musketeers"
#print(a, b, c)
#print(a + str(b) + c)

#text = input("Type anything: ")
#print(3*text)

#num1 = input("Type a number: ")
#print(2*num1)

#num2 = int(input("Type a number:"))
#print(4*num2)

#verb = input("Type a verb: ")
#print("I can",verb, "better than you")
#print(5*(verb+" "))

#x = int(input("What x to find the cube root of? "))
#g = int(input("What guess to start with?"))

#print("Current estimated cubed = ", g**3)
#next_g = g - ((g**3 - x)/(3*g**2))
#print("Next guess to try = ", next_g)

secret_number = 14
input_number = int(input("Guess a number between 1 and 20: "))
while input_number != secret_number:
    if input_number < secret_number:
        print("Too low - try again")
    else:
        print("Too high - try again")
    input_number = int(input("Guess a number between 1 and 20: "))
print("You guessed:", input_number)
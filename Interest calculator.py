# I = P * R * T
print("What would you like to calculate?")
print("I. Simple Interest")
print("P. Principal - initial amount in $")
print("R. % Interest Rate per year)")
print("T. Time of borrowing or investing money (per year)")

user_input = input("Type the letter of the variable you would like to calculate: ")

if user_input == "I":
    P = float(input("What is the value of P: "))
    R = float(input("What is the value of R: "))
    T = float(input("What is the value of T: "))
    I = P * (R/100) * T
    print("$" + "{:.2f}".format(I))
    
elif user_input == "P":
    R = float(input("What is the value of R: "))
    T = float(input("What is the value of T: "))
    I = float(input("What is the value of I: "))
    P = I / ((R/100) * T)
    print("$" + "{:.2f}".format(P))

elif user_input == "R":
    P = float(input("What is the value of P: "))
    T = float(input("What is the value of T: "))
    I = float(input("What is the value of I: "))
    R = (I / (P * T)) * 100
    print("{:.2f}".format(R) + "%")

else:
    P = float(input("What is the value of P: "))
    R = float(input("What is the value of R: "))
    I = float(input("What is the value of I: "))
    T = I / (P * (R / 100))
    print("{:.2f}".format(T) + " Years")
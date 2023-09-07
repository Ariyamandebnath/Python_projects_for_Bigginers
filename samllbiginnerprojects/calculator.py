#additon
def add(a,b):
    answer = a+b
    print(str(a)+"+"+str(b)+"="+str(answer))
    
    
def sub(a,b):
    answer = a-b
    print(str(a)+"-"+str(b)+"="+str(answer)) 
     
def mul(a,b):
    answer = a*b
    print(str(a)+"*"+str(b)+"="+str(answer))
    
def div(a,b):
    answer = a/b 
    print(str(a)+"/"+str(b)+"="+str(answer))

    
          
          
while True:
    
    

            
    print("A. Addition ")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Enter the choice of operation: ")


    if choice.upper()=="A":
        print("Addition")
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number: "))
        add(a,b)
    elif choice.upper()=="B":
        print("Subtraction")
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number: "))
        sub(a,b) 
    
    elif choice.upper()=="C":
        print("Multiplication")
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number: "))
        mul(a,b)
    
    elif choice.upper()=="D":
        print("Division")
        a = int(input("Enter the first number:"))
        b = int(input("Enter the second number: "))
        div(a,b)
    elif choice.upper()=="E" :
        print("Exit")
        quit()
    
    else:
        print("Wrong input")
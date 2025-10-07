def calculator(n):
    print("+ \n- \n* \n/")
    operation=input("Pick an operation: ")
    m=float(input("What's the next number? "))
    if operation=="+":
        print(f"{n} + {m} = {n+m}")
        n+=m
    elif operation=="-":
        print(f"{n} - {m} = {n-m}")
        n-=m
    elif operation=="*":
        print(f"{n} * {m} = {n*m}")
        n*=m
    elif operation=="/":
        print(f"{n} / {m} = {n/m}")
        n/=m
    Condition = input(f"Type 'y' to continue calculating with {n}, or type 'n' to start a new calculation: ")
    if Condition=='y':
        calculator(n)
    elif Condition=='n':
        print("\n"*20)
        calculator(float(input("What's the first number?: ")))




calculator(float(input("What's the first number?: ")))
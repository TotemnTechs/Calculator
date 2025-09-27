while True:
    print("=============MENU=============")
    print("[1] Add\n[2] Substract\n[3] Multiply\n[4] Divide")
    choice = input("Enter Your Choice: ")
    
    match choice: #jhfdsfjhdsjfk
        case "1":
            num1 = int(input("Enter First Number: "))
            num2 = int(input("Enter Second Number: "))
             #klfjdkjfdksjf
            results = num1 + num2
            print(f"Results: {results}")
            break
        case "2":
            ...
        case "3":
            ...
        case "4":
            ...
        case _:
            print("Invalid Code Menu")
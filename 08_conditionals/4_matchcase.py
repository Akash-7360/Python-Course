a=int(input("Enter a number: "))
match a:
    case 1:
        print("You won rs1")
    case 3:
        print("You won rs3")
    case 45:
        print("You won rs45")
    case _:
        print("Better luck next time")
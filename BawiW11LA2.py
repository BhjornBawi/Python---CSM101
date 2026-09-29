Pizza = [("Pepperoni", "small", 190),
    ("Pepperoni", "medium", 220),
    ("Pepperoni", "large", 300),

    ("Taco Pizza", "small", 190),
    ("Taco Pizza", "medium", 220),
    ("Taco Pizza", "large", 300),

    ("BBQ Chicken", "small", 190),
    ("BBQ Chicken", "medium", 220),
    ("BBQ Chicken", "large", 300)]

flavor = input("Enter pizza flavor (Pepperoni/Taco Pizza/BBQ Chicken): ").lower()

match flavor:

    case "pepperoni":
        print("Pepperoni Pizza")

        bawiSize = input("Enter the size (small/medium/large): ").lower()

        for item in Pizza:
            if item[0].lower() == "pepperoni" and item[1].lower() == bawiSize:
                print("Pizza price:", item[2])
                break
        else:
            print("Invalid size.")
    case "taco pizza":
        print("Taco Pizza")

        bawiSize = input("Enter the size (small/medium/large): ").lower()

        for item in Pizza:
            if item[0].lower() == "taco pizza" and item[1].lower() == bawiSize:
                print("Pizza price:", item[2])
                break
        else:
            print("Invalid size.")
    case "bbq chicken":
            print("BBQ Chicken Pizza")

            bawiSize = input("Enter the size (small/medium/large): ").lower()

            for item in Pizza:
                if item[0].lower() == "bbq chicken" and item[1].lower() == bawiSize:
                    print("Pizza price:", item[2])
                    break
            else:
                print("Invalid size.")
    case _: print("Invalid pizza flavor.")
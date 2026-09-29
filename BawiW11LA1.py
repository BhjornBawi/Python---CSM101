flavor = input("Enter pizza flavor (Pepperoni/Taco Pizza/BBQ Chicken): ").lower()

match flavor:
    case "pepperoni":
        print("Pepperoni Pizza")

        bawiSize = input("Enter the size (small/medium/large): ").lower()

        if bawiSize == "small":
            bawiPrice = 190
        elif bawiSize == "medium":
            bawiPrice = 220
        elif bawiSize == "large":
            bawiPrice = 300
        else:
            bawiPrice = 0
            print("Invalid size.")

        if bawiPrice > 0:
            print("Pizza price:", bawiPrice)


    case "taco pizza":
        print("Taco Pizza")

        bawiSize = input("Enter the size (small/medium/large): ").lower()

        if bawiSize == "small":
            bawiPrice = 190
        elif bawiSize == "medium":
            bawiPrice = 220
        elif bawiSize == "large":
            bawiPrice = 300
        else:
            bawiPrice = 0
            print("Invalid size.")

        if bawiPrice > 0:
            print("Pizza price:", bawiPrice)

    case "bbq chicken":
        print("BBQ Chicken Pizza")

        bawiSize = input("Enter the size (small/medium/large): ").lower()

        if bawiSize == "small":
            bawiPrice = 190
        elif bawiSize == "medium":
            bawiPrice = 220
        elif bawiSize == "large":
            bawiPrice = 300
        else:
            bawiPrice = 0
            print("Invalid size.")

        if bawiPrice > 0:
            print("Pizza price:", bawiPrice)

    case _:
        print("Invalid pizza flavor.")






MachineLearning = [ ("Supervised", "Decision True",),
                    ("Supervised", "Random Forrest"),
                    ("Unsupervised", "K-Means"),
                    ("Unsupervised", "Gaussian Mixture Model"),]

for item in MachineLearning:
    if item[0] == "Supervised":
        print("Supervised: ", item[1])

    else:
        print("Unsupervised: ", item[1])

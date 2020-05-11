while True:
    date_of_year = int(input("Enter the dae of year: "))

    age = 2020 - date_of_year

    if age >18:
        print("Adult")
    elif age in range(13, 18):
        print("Teenager")
    else:
        if age in range (0,12):
            print("Child")
        else:
            print("Enter a correct value")

    print(age)
def toto_check(x):
    from datetime import datetime
    now = datetime.now()
    date = now.strftime("%d %B %Y")
    open(date + ' toto.txt', 'w').close()
    for y in range(x):
        actual = [2, 15, 17, 27, 41, 48, 38]
        counter = 0
        match = []

        num = input("\nEnter your numbers")
        num = num.split(",")
        lst = [int(i) for i in num]
        print(lst)

        for i in range(6):
            if lst[i] in actual:
                counter += 1
                match.append(lst[i])

        with open(date + ' toto.txt', 'a+', encoding='utf-8') as f:
            f.write("Your Number: " + str(lst) + "\n")
            f.write("Actual number: " + str(actual) + "\n")
            f.write("Number of matches: " + str(counter) + "\n")
            f.write("Matched numbers: " + str(match) + "\n\n")


toto_check(int(input("Number of bets: ")))

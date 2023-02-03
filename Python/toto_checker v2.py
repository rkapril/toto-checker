def toto_check():
    from datetime import datetime
    now = datetime.now()
    date = now.strftime("%d %B %Y")
    draw_results = input("Enter the draw results(comma separated): ").split(",")
    draw_results = [int(i) for i in draw_results]

    with open("python/numbers.txt", "r") as f:
        for line in f:
            counter = 0
            match = []
            num = line.strip().split(",")
            lst = [int(i) for i in num]
            for i in range(len(lst)):
                if lst[i] in draw_results:
                    counter += 1
                    match.append(lst[i])
            with open("python/" + date + ' toto.txt', 'a+', encoding='utf-8') as f:
                f.write("Draw results: " + str(draw_results) + "\n")
                f.write("Ticket number: " + str(lst) + "\n")
                f.write("Number of matches: " + str(counter) + "\n")
                match = match if counter > 0 else "none"
                f.write("Matched numbers: " + str(match) + "\n\n")

toto_check()

with open("Кинотеатр.txt", "r", encoding="utf-8") as file:
    movies = []
    for line in file:
        l = []
        l = line.split()
        if (len(l)>4):
            i = len(l) - 4 + 1
            title = ""
            for j in range(i):
                title+=l[j] + " "
            print(title)
            date=l[i]
            price=l[i+1]
            viewers=l[i+2]
        else:
            title, date, price, viewers = l

        price = int(price)
        viewers = int(viewers)
        movies.append((title, date, price, viewers))


target_date = "12.07.2022"
print(f"Фильмы за {target_date}:")

for movie in movies:
    title, date, price, viewers = movie
    if date == target_date:
        print(title)

print()
print("Фильмы с ценой меньше 15 рублей:")

for movie in movies:
    title, date, price, viewers = movie
    if price < 15:
        print(f"{title} - {price} рублей")

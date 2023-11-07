with open("Занятия.txt", "r", encoding="utf-8") as file:
    lessons = {}
    for line in file:
        l = line.split()
        key=""
        kol=0
        for j in l:
            if j[0].isdigit():
                for i in range(len(j)):
                    if j[i+1].isdigit() == False:
                        kol=kol + int(j[0:i+1])
                        break
            else:
                key += j + " "
        key=key[:len(key)-2]
        lessons[key]=kol

print(lessons)
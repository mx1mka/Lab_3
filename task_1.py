f1 = open("F1.txt", "w")
print("Введите данные для файла F1 (пустая строка для окончания ввода):")
while True:
    line = input()
    if line == "":
        break
    f1.write(line + "\n")

f2 = open("F2.txt", "w")
f1 = open("F1.txt", "r")

for line in f1:
    if line[0].isdigit():
        f2.write(line)

f1.close()
f2.close()

f2 = open("F2.txt", "r")
first_line = f2.readline()
f2.close()

words = first_line.split()
word_count = len(words)
print("Количество слов в первой строке файла F2:", word_count)

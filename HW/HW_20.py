file = "test.txt"

f = open(file, "w")
f.write(
    "Замена строки в текстовом файле;\nизменить строку в списке;\nзаписать список в файл;\n"
)
f.close()


f = open(file, "r")
pos1 = int(input("Введите номер первой строки, которую хотите поменять: ")) - 1
pos2 = int(input("Введите номер второй строки, которую хотите поменять: ")) - 1
read_line = f.readlines()
f.close()

if 0 <= pos1 < len(read_line) and 0 <= pos2 < len(read_line):
    read_line[pos1], read_line[pos2] = read_line[pos2], read_line[pos1]
else:
    print("Введите корректные номера строк.")
print(read_line)

f = open(file, "w")
f.writelines(read_line)
f.close()

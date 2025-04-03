
import os

# Задача
'''
dirs = [r"Work\F1", r"Work\F2\F21"]
# for d in dirs: # Создание папок в системе
#     os.makedirs(d)

files = {
    "Work": ["w.txt"],
    r"Work\F1": ["f11.txt", "f12.txt", "f13.txt"],
    r"Work\F2\F21": ["f211.txt", "f212.txt"],
}

for d, files in files.items():
    for file in files:
        file_path = os.path.join(d, file)
        # print(file_path)
        open(file_path, "w").close()

file_with_text = [r"Work\w.txt", r"Work\F1\F12.txt", r"Work\F2\F21\f211.txt", r"Work\F2\F21\f212.txt" ]

for file in file_with_text:
    with open(file, "w") as f:
        f.write(f"Такой - то текст в файле {file}")


def print_tree(root, topdown):
    print(f"Обход {root} {"сверху вниз" if topdown else "снизу вверх"}")
    for root, directory, file_name in os.walk(root, topdown):
        print(root)
        print(directory)
        print(file_name)
    print("-"*50)

print_tree("Work", False)
print_tree("Work", True)

'''

# ________________________ООП Python_________________________________________________________

class Point:
    x = 1
    y = 2


p1 = Point()
print(p1.x) # обращение к свойству (переменной класса)
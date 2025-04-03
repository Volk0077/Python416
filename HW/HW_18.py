# Регулярные выражения

import re

test = "123456@i.ru, 123_456@ru.name.ru, login@i.ru, логин-1@i.ru, login.3@i.ru, login.3-67@i.ru, 1login@ru.name.ru"
reg = r"[0-9a-zA-Zа-яА-Я._-]+@[A-Za-z0-9.-]+\.\w{2}"
print(re.findall(reg, test))

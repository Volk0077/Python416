s = "I am learning Python. hello WORLD!"

a = s[: s.find("h")]
b = s[s.find("h") : s.rfind("h") + 1]
c = s[s.rfind("h") + 1 :]
print(a + b[::-1] + c)

import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)
print(x)

txt = "The rain in Spain"
x = re.findall("Portugal", txt)
print(x)

txt = "The rain in Spain"
x = re.search("\s", txt)

print("The first white-space character is located in position:", x.start())

txt = "The rain in Spain"
x = re.search('\s', txt, 1)
print(x)

txt = "The rain in Paris"
x = re.sub("\s", "o", txt)
print(x)


txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.span())

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.string)

with open("Source/Language_de.xml", "r", encoding="UTF-8") as file:
    content = file.readlines()

l_gentext = []
for line in content:
    if line.startswith("<l:gentext"):
        l_gentext.append(line.strip("\n"))

input_key = input("Bitte Key eingeben: ")
input_value = input("Bitte Value eingeben: ")

l_gentext.append(f'<l:gentext key="{input_key}" value="{input_value}"')



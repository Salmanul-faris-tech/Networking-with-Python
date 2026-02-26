
with open("simple.txt", "w") as file:
    file.write("Hello Guys")
    file.write("Hacked")

    print("The content Successfully writed")

content = file.read

print(content)

file.close()


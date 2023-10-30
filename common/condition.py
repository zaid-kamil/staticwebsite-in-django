file = input("enter file name:")
if file.endswith(".html"):
    print(f"{file} is HTML file")
elif file.endswith(".css"):
    print(f"{file} is CSS file")
elif file.endswith(".js"):
    print(f"{file} is JS file")
else:
    print(f"{file} is unknown file")

# add conditions for .py, .md, .png, .gif, etc
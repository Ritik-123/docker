
usrename= str(input("Enter your username: "))
if usrename:
    with open('username.txt', 'a') as file:
        file.write(usrename + '\n')

show_info= input("Do you want to see the content of the file? (y/n): ")

if show_info == "y":
    try:
        with open('username.txt', 'r') as file:
            content = file.readlines()
    except Exception as e:
        print(e, type(e))

    else:
        for line in content:
            print(f'{line.strip()}')
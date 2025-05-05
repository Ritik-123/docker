def input_values():
    a= float(input("Enter a number: "))
    b= float(input("Enter another number: "))
    print(add(a,b)) 

def add(a,b):
    return f"Sume of two numbers : {a+b}"

def main():

    while True:
        play= input("Do you want to play? (yes/no): ")
        if play.lower() == "yes":
            print("Let's play!")
            input_values()
        elif play.lower() == "no":
            print("Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")
            continue

if __name__ == '__main__':
    main()
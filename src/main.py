from cleaner import clean_to_csv
from cleaner import clean_to_json


def menu():
    print("---Cleaning CSV Files---")
    print("1. Clean File and store it in CSV file")
    print("2. Clean File and store it in JSON file")
    print("0. Exit")

def main():
    while True:
        menu()
        try:
            choice = int(input("Enter a choice(0-2): "))
        except ValueError:
            print("Invalid Input. Please enter integer")
            continue
        if(choice==1):
            clean_to_csv()

        elif(choice==2):
            clean_to_json()
        
        elif(choice==0):
            print("Exiting the program...")
            break
        else:
            print("Invalid Input. Please enter integer between (0-2)")

if __name__ == "__main__":
    main()

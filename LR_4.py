from datetime import datetime

print("\tElectronics Store")
introduction = input("If you want to learn how the program works, please type (yes/no): ")
if introduction == "yes":
    print("This program allows you to interact with an electronics store, add, remove, and display a list of smartphones by their release year using a text menu.")
else:
    print("Then let's get started!")

class Smartphone:
    def __init__(self, name, release_year):
        self.name = name
        self.release_year = release_year

    def calculate_age(self):
        current_year = datetime.now().year
        return current_year - self.release_year

class Store:
    def __init__(self):
        self.smartphones = []

    def add_smartphone(self, smartphone):
        self.smartphones.append(smartphone)

    def remove_smartphone(self, name):
        for smartphone in self.smartphones:
            if smartphone.name == name:
                self.smartphones.remove(smartphone)
                print(f"{name} removed from the store.")
                return
        print(f"{name} not found in the store.")

    def list_smartphones(self, max_year):
        for smartphone in self.smartphones:
            age = smartphone.calculate_age()
            if age <= max_year:
                print(f"{smartphone.name} ({smartphone.release_year}), age: {age} years")

def main():
    store = Store()
    
    while True:
        print("1. Add Smartphone")
        print("2. Remove Smartphone")
        print("3. List Smartphones by Release Year")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            name = input("Enter the smartphone name: ")
            release_year = input("Enter the release year: ")
            try:
                release_year = int(release_year)
                smartphone = Smartphone(name, release_year)
                store.add_smartphone(smartphone)
                print(f"{name} added to the store.")
            except ValueError:
                print("Invalid release year. Please enter a valid year.")
        elif choice == "2":
            name = input("Enter the smartphone name to remove: ")
            store.remove_smartphone(name)
        elif choice == "3":
            max_year = input("Enter the maximum release year: ")
            try:
                max_year = int(max_year)
                store.list_smartphones(max_year)
            except ValueError:
                print("Invalid release year. Please enter a valid year.")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

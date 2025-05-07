print("\nTemperature Converter")

def menu():
    print("\nMenu:")
    print(" 1. Convert Celsius to Fahrenheit")
    print(" 2. Convert Fahrenheit to Celsius")
    print(" 3. Exit")

def cel_to_fah(celsius):
    return (celsius * 9 / 5) + 32

def fah_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

def main():
    while True:
        menu()
        choice = input("Enter your choice from (1-3): ")

        if choice == '1':
            celsius = float(input(" Enter temperature in Celsius: "))
            fahrenheit = cel_to_fah(celsius)
            print(f"Temperature in Fahrenheit: {fahrenheit:.2f}")
        elif choice == '2':
            fahrenheit = float(input(" Enter temperature in Fahrenheit: "))
            celsius = fah_to_cel(fahrenheit)
            print(f"Temperature in Celsius: {celsius:.2f}")
        elif choice == "3":
            print("Thank you for using the temperature converter.")
            break
        else:
            print("Invalid Choice. Choose from (1-3) pls.")


main()

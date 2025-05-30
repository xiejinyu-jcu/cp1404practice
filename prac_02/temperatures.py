MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""

def main():
    """Main program show the menu and handling function execute """
    choice = ""
    while choice != "Q":
        print(MENU)
        choice = input(">>> ").upper()
        if choice == "C":
            celsius = float(input("Celsius: "))
            fahrenheit = celsius_to_fahrenheit(celsius)
            print(f"Result: {fahrenheit:.2f} F")
        elif choice == "F":
            fahrenheit = float(input("Fahrenheit: "))
            celsius = fahrenheit_to_celsius(fahrenheit)
            print(f"Result: {celsius:.2f} C")
        elif choice != "Q":
            print("Invalid option")
    print("Thank you.")

def celsius_to_fahrenheit(celsius):
    """ convert celsius to fahrenheit """

    return celsius * 9.0 / 5 + 32

def fahrenheit_to_celsius(fahrenheit):
    """convert fahrenheit to celsius """
    return 5 / 9 * (fahrenheit - 32)

main()













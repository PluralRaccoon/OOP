from employee import Employee

def main():
    bob = Employee("Bob Esponja", "Cook")
    calamardo = Employee("Calamardo", "Cashier")

    print(bob.get_info())
    print(calamardo.get_info())

    print(Employee.is_valid_position("Manager"))
    print(Employee.is_valid_position("Data Engineer"))

if __name__ == "__main__":
    main()
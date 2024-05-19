class Parent:
    """Parent class that initializes an attribute."""
    
    def __init__(self, value):
        """Initialize the value attribute."""
        self.value = value

    def display_value(self):
        """Display the value."""
        print(f'Value: {self.value}')


class Child(Parent):
    """Child class that inherits from Parent and adds new attributes."""
    
    def __init__(self, value, extra_value):
        """Initialize value attribute from Parent and extra_value attribute."""
        super().__init__(value)
        self.extra_value = extra_value

    def display_extra_value(self):
        """Display the extra value."""
        print(f'Extra Value: {self.extra_value}')


def main():
    """Main function to demonstrate class usage."""
    parent_instance = Parent(10)
    parent_instance.display_value()

    child_instance = Child(20, 30)
    child_instance.display_value()
    child_instance.display_extra_value()


if __name__ == "__main__":
    main()


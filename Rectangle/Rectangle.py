#Gabriel Ranola
#CIS261 Rectangle 02/11/26

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_area(self):
        return self.height * self.width

    def print_info(self):
        print("Rectangle Calculator\n")
        print(f"Height:       {self.height}")
        print(f"Width:        {self.width}")
        print(f"Perimeter:    {self.get_perimeter()}")
        print(f"Area:         {self.get_area()}\n")

    def draw(self):
        # Top border
        print("* " * self.width)

        # Middle rows
        for _ in range(self.height - 2):
            print("* " + "  " * (self.width - 2) + "*")

        # Bottom border
        if self.height > 1:
            print("* " * self.width)


def main():
    while True:
        print("Rectangle Calculator\n")

        height = int(input("Enter height: "))
        width = int(input("Enter width: "))
        print()

        rect = Rectangle(height, width)
        rect.print_info()
        rect.draw()

        print()
        cont = input("Continue? (y/n): ").lower()
        if cont != "y":
            break
        print()

main()
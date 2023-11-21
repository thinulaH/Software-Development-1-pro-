


def input_value(x):
    while True:
        try:
            value = int(input(f"Enter a number {x}: "))
            if value in [0, 20, 40, 60, 80, 100, 120]:
                return value
            else:
                print("Out of range. Enter a number in the set [0, 20, 40, 60, 80, 100, 120].")
        except ValueError:
            print("Need to enter an integer.")

x = "Pass"
value1 = input_value(x)
print("Entered value:", value1)

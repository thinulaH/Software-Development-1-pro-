import part_1
import part_2
import part_3

def main():
    print('Select a part to open :')
    print('1.   Part 1')
    print('2.   Part 2')
    print('3.   Part 3')
    part = input('Enter what part you want to open (1, 2 or 3) : ')
    while part not in ('1','2','3'):
        part = input('Invalid selection. Please enter 1, 2 or 3 :')
    if part == '1' :
        part_1.main()
    elif part == '2' :
        part_2.main()
    elif part == '3' :
        part_3.main()
        
if __name__ == "__main__":
    main()

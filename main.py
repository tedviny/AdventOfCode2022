##### Day 1 AdventOfCode 2022
import itertools


def calory_counting(file_name):
    """
    This function take in parameter the name of txt file containning numbers and
    returning the sum of group of lines separating with back to line. At the end the biggest sum number
    will be printed.
    """
    with open(file_name, 'r') as file:
        # Open and read a file
        # Remove back to line by replacing with space
        lines = file.read().replace('\n',' ')
        # Create list of numbers in file and remove all spaces
        lst = list(lines.split(' '))
        # Create sublists of list with group separated previously with space
        liste = [list(x[1]) for x in itertools.groupby(lst, lambda x: x == '') if not x[0]]
        list_max_values = list()
        for j in liste:
            # convert sublist of string to sublist of integer
            new_list = list(map(int,j))
            # calculate the sum of each numbers in sublists
            max_value = sum(new_list)
            list_max_values.append(max_value)
    # find the biggest number of final list
    val = max(list_max_values)
    print(f'*********** The biggest sum number is : {val} *****************')
    print('************** Program end **************************')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    calory_counting('input_puzzle.txt')

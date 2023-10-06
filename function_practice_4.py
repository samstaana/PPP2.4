# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max([a, b, c])

print(max_num(1, 2, 3))


# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(lst):
    if len(lst) == 0:
        return 0
    prod = lst[0]
    if len(lst) > 1:
        for num in lst[1:]:
            prod = prod * num
    return prod

print(mult_list([1, 2, 3]))
print(mult_list([1, 2, 3,4]))


# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]

print(rev_string('racecar'))
print(rev_string('This should be backwards'))
print(rev_string('sdrawkcab eb dluohs sihT'))


# Write a Python function called num_within() to check whether a number falls in a given range.
# The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
# Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
def num_within(target, start, end):
    return target in range(start, end + 1)

print(num_within(3, 2, 4))
print(num_within(3, 1, 3))
print(num_within(10, 2, 5))


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
# The function accepts the number n, the number of rows to print
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal. Each number is the two numbers above it added together.
triangle = [[1], [1, 1]]

def pascal(n):
    if n < 1:
        print('NO')
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            prev_row = triangle [row_number - 1]
            length = len(prev_row) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length - 1:
                    value = triangle[row_number -1] [i - 1] + triangle[row_number -1][i]
                    row.append()
                else:
                    row.append(1)
            triangle.append(row)
            row_number == 1

        for row in triangle:
            print(row)

pascal(2)
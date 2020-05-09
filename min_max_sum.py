# Note: This is not the most condensed solution
# There are cleaner methods that will solve the challenge in shorter lines of code

array = [7, 69, 2, 221, 8974]
new_array = sorted(array)

def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0

    for i in range(len(new_array)):
        min_sum += new_array[i]
        max_sum += new_array[i]

    min_sum -= new_array[4]
    max_sum -= new_array[0]

    print(min_sum, max_sum)

if __name__ == '__main__':
    miniMaxSum(new_array)
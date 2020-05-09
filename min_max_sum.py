# Note: This is not the most condensed solution
# There are cleaner methods that will solve the challenge in shorter lines of code

array = [7, 69, 2, 221, 8974]
# Sort array to ascending order; used sorted() since it returns an iterable list
new_array = sorted(array)

def miniMaxSum(arr):
    min_sum = 0
    max_sum = 0

    for i in range(len(new_array)):
        # Adds element to the min_sum or max_sum counter
        min_sum += new_array[i]
        max_sum += new_array[i]

    # Subtract last element (since this is the highest number) to get the min sum
    min_sum -= new_array[4]
    # Subtract first element (since this is the lowest number) to get the max sum
    max_sum -= new_array[0]

    print(min_sum, max_sum)

if __name__ == '__main__':
    miniMaxSum(new_array)
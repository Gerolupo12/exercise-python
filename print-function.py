# Without using any string methods, try to print the following:
# Example
# n = 5
# Print the string 12345

# Constraints
# 1 <= n <= 150

# Output Format
# Print the list of integers from 1 through n as a string, without spaces.

# Sample Input 0
# 3

# Sample Output 0
# 123

if __name__ == '__main__':
    n = int(input())
    if 1 <= n <= 150:
        for i in range(1, n+1):
            print(i, end="")
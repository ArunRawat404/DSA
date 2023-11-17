# reverse a array using recursion
def reverseArray(arr, left, right):
    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]

    reverseArray(arr, left + 1, right - 1)


# to check a string is palindrome using recursion
def checkPalindrome(string, left, right):
    if left >= right:
        return True

    if string[left] != string[right]:
        return False

    return checkPalindrome(string, left + 1, right - 1)


arr = [1, 2, 3, 4, 5]
reverseArray(arr, 0, len(arr) - 1)
print(arr)

string = "abcdcba"
print(checkPalindrome(arr, 0, len(string) - 1))

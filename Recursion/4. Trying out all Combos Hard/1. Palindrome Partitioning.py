# Time Complexity: O( (2^n) *k*(n/2) ) ,O(2^n) to generate every substring and O(n/2)  to check if the substring generated is a palindrome. O(k) is for inserting the palindromes in another data structure, where k  is the average length of the palindrome list.

# Space Complexity: O(k * x), The space complexity can vary depending upon the length of the answer. k is the average length of the list of palindromes and if we have x such list of palindromes in our final answer. The depth of the recursion tree is n, so the auxiliary space required is equal to the O(n).


def isPalindrome(start, end, s):
    while start <= end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True


def findPalindromePartition(index, partition_array, ans, s):
    if index == len(s):
        ans.append(partition_array.copy())
        return

    for i in range(index, len(s)):
        # check if palindrome partition is possible
        if isPalindrome(index, i, s):
            partition_array.append(s[index : i + 1])
            findPalindromePartition(i + 1, partition_array, ans, s)
            # after backtracking removing last inserted item
            partition_array.pop()


def partition(s):
    ans = []
    findPalindromePartition(0, [], ans, s)
    return ans


s = "aaaa"
print(partition(s))

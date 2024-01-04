def isBalanced(s):
    count = 0

    for p in s:
        if p == "(":
            count += 1
        elif p == ")":
            # It is a closing parenthesis
            count -= 1

        if count < 0:
            # This means there are more closing parenthesis than opening
            return False

    return count == 0


def removeInvalidParentheses(s):

    # using set to avoid duplicate strings
    string_set = {s}

    # Until we find our answer
    while True:
        # for storing valid parentheses
        valid_strings = []
        # going through each string in string set to check if it is a valid parentheses or not
        for string in string_set:
            if isBalanced(string):
                valid_strings.append(string)

        # if we got valid parentheses
        if valid_strings:
            return valid_strings

        # a empty set to store new generated strings
        new_string_set = set()
        for string in string_set:
            for i in range(len(string)):
                # removing ith character from the string
                new_string_set.add(string[:i] + string[i + 1 :])

        # for new iteration to check valid string
        string_set = new_string_set


s = ")(()()"
print(removeInvalidParentheses(s))

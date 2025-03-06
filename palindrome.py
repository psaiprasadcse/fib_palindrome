def is_palindrome(s: str) -> bool:
    s = s.lower().replace(" ", "")
    return s == s[::-1]


if __name__ == "__main__":
    word = input("Enter a word: ")
    if is_palindrome(word):
        print("It's a palindrome!")
    else:
        print("Not a palindrome.")
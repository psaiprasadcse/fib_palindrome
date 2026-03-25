def is_palindrome(s: str) -> bool:
    # Keep only letters and numbers, ignore case
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


if __name__ == "__main__":
    word = input("Enter a word or phrase: ")
    if is_palindrome(word):
        print("It's a palindrome!")
    else:
        print("Not a palindrome.")

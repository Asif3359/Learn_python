
def is_palindrome(s):
     return s == s[::-1]

def main():
    str = input()
    print(is_palindrome(str))
    
if __name__ == "__main__":
    main()
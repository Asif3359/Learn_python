
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    
    return True
    

def main():
    num = int(input())
    print(is_prime(num))

if __name__ == "__main__":
    main()
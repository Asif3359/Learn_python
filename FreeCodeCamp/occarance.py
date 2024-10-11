

def main():
    items = []
    print("Enter Number of items: ")
    n = int(input())
    
    for item in range(n):
        i = int(input())
        # items = items+[i]
        items.append(i) 
        
    occ = {}
    for item in items:
        if item in occ:
            occ[item] += 1  # Increment the count
        else:
            occ[item] = 1  # Initialize the count

    for item in occ:
        print(f"Item {item} occurs {occ[item]} time(s).")  # Use formatted string for output       
        


def main1():
    dic = {1,2,3,4}
    
    i = 0 
    for item in dic:
        print(f"{i} {item} ")
        i = i+1

if __name__ == "__main__":
    # main()
    main1()


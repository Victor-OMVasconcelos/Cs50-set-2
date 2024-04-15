def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

    



def is_valid(a):
    length = len(a)
    if not a.isalnum():
        return False
    if not  2 <= length <=6:
        return False
    if not a[0:2].isalpha:
        return False
    
    for i in length:
        if a[i].isdigit() and a[i+1].isalpha:
         return False
        if i =="0":
            return False
        
    return True
    
            
    
    
    
    



main()
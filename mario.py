#def main():
 #   print_row(4)


#def print_row(width):
 #   print("?" * width)
def main():
    print_square(3)

def print_square(size):
    for i in range(size):
         for j in range(size):
             print("#", end="")
         print()
main()
#i = 3
#while i != 0:
 #   print("meow")
  #  i -= 1

for i in [0,1,2]:
   print("meow")

#When you need a variable to do something in python but you dont care about the variable, use underscore to represent it
#for _ in range(100):
   # print("meow")

#print("meow\n" * 3, end="")

#while True:
 #   n = int(input("What's n? "))
  #  if n < 0:
   #     continue
    #else:
     #   break

#while True:
  #  n = int(input("What's n? "))
 #   if n > 0:
   #     break

#for _ in range(n):
  #  print("meow")

def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n
        
def meow(n):
    for _ in range(n):
        print("meow")

main()
import random
import string
def main():
  a = int(input())
  i = 0
  s = ""
  while i<a:
      b = random.choice([0,1])
      if (b==0):
          b1 = random.choice([0,1])
          if (b1==0):
              letters = string.ascii_lowercase
              s+= str(random.choice(letters))
          else:
              letters = string.ascii_uppercase
              s+= str(random.choice(letters))
      else:
          s+= str(random.choice([0,1,2,3,4,5,6,7,8,9]))
      i+=1

  s+=".html"
  print(s)
  
main()

abc = int(input("Введіть трицифрове число "))
c= abc%10
b=abc%100//10
a=abc%1000//100
print(a*b*c)
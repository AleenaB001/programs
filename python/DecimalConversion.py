#Converting decimal into binary,hexadecimal and octal
print("Enter decimal number:")
number = int(input())
print("Decimal into binary:")
res = format(number,"b")
print(res)
print("Decimal into Hexadecimal:")
res = format(number,"x")
print(res)
print("Decimal into octal:")
res = format(number,"o")
print(res)

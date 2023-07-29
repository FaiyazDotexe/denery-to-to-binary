num = int(input("Enter a number: "))
num = num * 2
final = []
while (num > 0):
    num = num // 2
    num2 = num % 2

    final.append(num2)
    if (num <= 0):
        final.reverse()
        final.pop(0)
        print(final)
        break


num = int(input("Enter your number: "))
arr_num = [int(x) for x in str(num)]
arr_num.reverse()
arr_count=[]

for i in range(0,len(arr_num)):
    power = 2 ** i
    if arr_num[i] == 1:
        arr_count.append(power)
        count = 0
        for y in arr_count:
            count += y
print(count)

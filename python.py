i = 0
with open("practice.txt", "r") as f:
    data = f.read()
    print(data)

    nums = data.split(",")
    for value in nums:
        if(int(value) % 2 == 0):
            print(value)
            i += 1
        else:
            print("finding...")

print(i)


   




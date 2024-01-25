def multiolication_table(n):
    for i in range(1,n+1):
        for j in range(1,n+1):
            product = i*j
            print(f"{i}*{j} = {product}")
        print("----------------")

n = int(input('Enter n: '))
multiolication_table(n) 
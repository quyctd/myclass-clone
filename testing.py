menu = [1 ,6 ,8 ,1 ,2 ,1 ,5 ,8 ]

n = int(input("enter a number: "))

for i in range(len(menu)-1):
    print(menu[i])
    if menu[i] != n:
        menu.remove(menu[i])
print(len(menu))

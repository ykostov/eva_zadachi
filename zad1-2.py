n = int(input("enter n: "))
list1 = []
if n > 20 and n < 30:
    for i in range(0, n, 1):
        new_num = int(input("enter number: "))
        if new_num > -100 and new_num < 100:
            list1.append(new_num)

    counter_necetni = 0
    counter_edinici = 0
    multi_nums = 1

    for i in range(0, len(list1), 1):
        if i % 2 == 1:
            counter_necetni += list1[i]
    for num in list1:
        if num % 2 == 0: #kratni na 2 == cetni
            counter_edinici += 1
    for num in list1:
        if num < 0 and num % 2 == 0:
            multi_nums *= num

    list1.sort(reverse=True)
    list2 = []
    for num in list1:
        print(num)
        if num > n:
            list2.append(num)

    print(max(list2) - min(list2))        
    
    counter_necetni_list2 = 0

    for num in list2:
        if num % 2 == 1:
            print(num)
            counter_necetni_list2 += 1

    print(counter_necetni_list2)

    list2.remove(min(list2))
               


else:
    print("bad input")


           

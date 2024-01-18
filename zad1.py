n = int(input("enter n: "))
list1 = []
counter_desetici = 0
if n > 15 and n < 35:
    for i in range(0, n, 1):
        new_num = int(input("enter number: "))
        if new_num > 30 and new_num < 300:
            list1.append(new_num)
            # десетици е втората цифра от 050 (5)
            desetici = int(str(new_num[1]))
            if desetici % 3 == 0:
                counter_desetici += 1

        list1.sort()
        for num in list1:
            if num % 6 == 4:
                print(num)
                break
    list2 = [num for num in list1 if (num > 9) and (num % 2 == 0 or num % 3 == 0)]
    # тва е трудно и няма да го имаш 100%

    counter_num_list2 = 0 
    nums_list2 = 0

    for i in range(0, len(list2), 1):
        if i % 2 == 1:
            counter_num_list2 += 1
            nums_list2 += list2[i]
    print(nums_list2 / counter_num_list2)

    list2.sort()

    list2.pop(0)        



else:
    print("bad input")


           

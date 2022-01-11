count = 0
bucket5 = 0
bucket3 = 0
print('Enter an action \n 1. Fill up 5 litters bucket \n 2. Fill up 3 litters bucket \n 3. To empty 5 litters bucket \n 4. To empty 3 litters bucket \n 5. Pour over bucket 5 to bucket 3 \n 6. Pour over bucket 3 to bucket 5 \n 0. exit')
while bucket5 != 4:
    print('Bucket 3 =', bucket3, '\tBucket 5 =', bucket5)
    com = input()
    if com.isdigit() and 0 <= int(com) <= 6:
        if com == '1':
            if bucket5 != 5:
                bucket5 = 5
                count += 1
            else:
                print('Bucket is Full')
        if com == '2':
            if bucket3 != 3:
                bucket3 = 3
                count += 1
            else:
                print('Bucket is Full') 
        if com == '3':
            if bucket5 != 0:
                bucket5 = 0
                count += 1
            else:
                print('Bucket is empty')
        if com == '4':
            if bucket3 != 0:
                bucket3 = 0
                count += 1
            else:
                print('Bucket is empty')
        if com == '5':
            if bucket5 == 0:
                print('Bucket5 is empty')
            elif bucket3 == 3:
                print('Bucket3 is Full')
            else:
                space = 3 - bucket3
                count += 1
                if bucket5 >= space:
                    bucket5 -= space
                    bucket3 = 3                    
                else:
                    bucket3 += bucket5
                    bucket5 = 0
        if com == '6':
            if bucket3 == 0:
                print('Bucket3 is empty')
            elif bucket5 == 5:
                print('Bucket5 is Full')
            else:
                space = 5 - bucket5
                count += 1
                if bucket3 >= space:
                    bucket3 -= space
                    bucket5 = 5                    
                else:
                    bucket5 += bucket3
                    bucket3 = 0
        if com == '0':
            break
    else:
        print('Input error')
        continue
print('Bucket 3 =', bucket3, '\tBucket 5 =', bucket5)
print(count, ' = Steps')
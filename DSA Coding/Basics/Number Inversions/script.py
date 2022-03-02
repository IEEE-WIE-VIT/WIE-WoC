N = input()
global counter1
counter1 = 0

def inversion(new_N):
    for counter in range(1):
        new_N = str(new_N)[:counter1] + str(9 - int(str(new_N)[counter1])) +str(new_N)[(counter1+1):]
    return new_N


if 1 <= int(N) <= (10**18):
    Flag = True
    new_number = N
    while Flag:
        small_number = inversion(new_number)
        if small_number[0] == '0':
            counter1 += 1
            if (counter1+1) > len(str(N)):
                print(new_number)
                break
        elif int(small_number) <= int(new_number):
            new_number = small_number
        else:
            counter1 += 1
            if (counter1+1) > len(str(N)):
                print(new_number)
                break


def CountSmall(Brr):
    iCount = 0

    for i in range(len(Brr)):
        if(Brr[i] >= 'a' and Brr[i] <= 'z'):      #Issue
            iCount = iCount + 1

    return iCount


def main():
    print("Enter String : ")
    Arr = input()

    Ret = CountSmall(Arr)

    print("Number of small characters are : ", Ret)

    

main()
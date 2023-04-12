# Ayush Agarwal-20030480008
def main():
    T=int(input())
    while T>0:
        def reverse(string):
            if len(string) == 0:
                return string
            else:
                return reverse(string[1:]) + string[0]

        a = str(input("Enter the string to be reversed: "))
        print(reverse(a))
    T=T-1
    return 0
if __name__=='__main__':
    main()
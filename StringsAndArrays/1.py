#Reverse a string without affecting special characters

def revFunc(string):
    #small = [chr(x) for x in range(ord('a'), ord('z')+1)]
    #capital = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    ls = list(string)
    l = 0
    r = len(ls)-1
    print(ls[l])
    print(ls[r])

    while(l < r):
        if( ((ls[l] >= 'A' and ls[l] <= 'Z') or (ls[l] >= 'a' and ls[l] <= 'z')) == False ):
            l += 1
        elif( ((ls[r] >= 'A' and ls[r] <= 'Z') or (ls[r] >= 'a' and ls[r] <= 'z')) == False ):
            r -= 1
        else:
            temp = ls[l]
            ls[l] = ls[r]
            ls[r] = temp
            l += 1
            r -= 1
    return(''.join(ls))
if __name__ == "__main__":
    string = 'A!!!b.c.d,e"f,ghi'
    rev = revFunc(string)
    print('Reversed string :' + rev)



def jewels(J,S):
    finalcount = 0
    for char in J:
        if char in S:
            scount = 0
            while(scount < len(S)):
                if S[scount] == char:
                    finalcount += 1
                    scount+= 1
                else:
                    scount += 1
    return finalcount

j = "aA"
s = "aAAbbbb"
j2 = 'b'
s2 = 'aaaaaaaaaajjjjjjj'
j3 = 'cFbh'
s3 = 'AFbcYYhh'
print(jewels(j,s))
print(jewels(j2,s2))
print(jewels(j3,s3))
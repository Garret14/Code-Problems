def rlencrypt(s):
    nstring = ""
    char = s[0]
    count = 0
    for i in s:
        if i != char:
            numchar = str(count)
            nstring = nstring + numchar
            nstring = nstring + char
            char = i
            count = 1
        else:
            count += 1
    finalnumchar = str(count)
    nstring = nstring + finalnumchar
    nstring = nstring + char
    return nstring

def rldecrypt(s):
    nstring = ""
    num = 0
    char = ""
    count = 0
    while count < len(s):
        num = int(s[count])
        char = s[count+1]
        nstring = nstring + (char * num)
        count += 2
    return nstring

print(rlencrypt("AAAABBBCCDAA"))
print(rldecrypt("4A3B2C1D2A"))

def permutation_string(s):
    if len(s)==1:
        return s

    p=[]
    for i in range(len(s)):
        fixed_char=s[i]
        remaining_char=s[:i]+s[i+1:]
        for perm in permutation_string(remaining_char):
            p.append(fixed_char+remaining_char)
    return p
print(permutation_string('ABC'))























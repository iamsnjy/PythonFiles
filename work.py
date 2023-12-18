
#just practice : upper/lower count,frequency of chars/words/consecutive frequency,palindrome
#more practice : roman,pw,rotation,all substring,permutation,bubblr_sort,count of overlapping substring occurence.

"""map,filter,reduce,lambda,enumerate,zip,range,
"""



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























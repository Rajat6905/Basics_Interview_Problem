def permutations(s, fi = 0):
     if fi == len(s):
        n = "".join(s)
        n = int(n)
        a.append(n)
        
     for i in range(fi, len(s)):
        s_list = [j for j in s]
        s_list[fi],s_list[i]=s_list[i],s_list[fi]
        permutations(s_list, fi + 1)

    
a = []
n = int(input())
permutations(str(n))
print(list(set(a)))




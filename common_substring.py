def maxCommStr(s1, s2):
    m = len(s1)
    n = len(s2)

    res = 0

    # Consider every pair of index and find the length
    # of the longest common substring beginning with
    # every pair. Finally return max of all maximums.
    for i in range(m):
        for j in range(n):
            curr = 0
            while (i + curr) < m and (j + curr) < n and s1[i + curr] == s2[j + curr]:
                curr += 1
            res = max(res, curr)

    return res


s1 = "hello welcome"
s2 = "Hello world"
print(maxCommStr(s1, s2))
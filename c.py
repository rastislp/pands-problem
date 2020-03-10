def radix_sort(nlist):
    RADIX = 10
    placement = 1
    max_digit = max(nlist)

    while placement < max_digit:
      buckets = [list() for _ in range( RADIX )]
      for i in nlist:
        tmp = int((i / placement) % RADIX)
        buckets[tmp].append(i)
      a = 0
      for b in range( RADIX ):
        buck = buckets[b]
        for i in buck:
          nlist[a] = i
          a += 1
      placement *= RADIX
    return nlist







nlist = [90,46,43,27,57,41,45,21,70]
print(nlist)
radix_sort(nlist)
print(nlist)
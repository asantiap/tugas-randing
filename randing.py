dataku = [12,1,[22,3,[8,14]],2,6,[11],90]

def partition(l, bwh, ats): 
    pivot = l[bwh]
    index = bwh+1
    for i in range(bwh+1,ats):
      if l[i] < pivot:
          l[index],l[i]=l[i],l[index]
          index += 1
    l[index-1],l[bwh] = l[bwh],l[index-1]
    return index

def quickShort(l, bwh, ats):
    if bwh < ats:
        pt = partition(l, bwh, ats)
        quickShort(l, bwh, pt -1)
        quickShort(l, pt + 1, ats)

def terpisah(pp):
    result = []
    for dataku in pp:
        if isinstance(dataku,list):
            for i in dataku:
                if isinstance(i, list):
                    for x in i :
                       result.append(int(x))
                elif isinstance(i, int) :
                    result.append(i)
        else :
            result.append(dataku)
    return result

def fungsi(l):
  t = terpisah(l)
  quickShort(t, 0, len(t))
  return t


print("sebelum: ",dataku)
x = fungsi(dataku)
print("sesudah: ", x)
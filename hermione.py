from collections import Counter
def collect_runes(runes):
    target = Counter("LUMOS")
    print(target)
    collector = Counter()
    print(collector)
     
    for i,ch in enumerate(runes,start=1):
        collector[ch.upper()] +=1
        for c in target:
            if collector[c] >= target[c]:
                return i
    return -1
rune_in = input("Enter the rune:")
exit = rune_in
result = collect_runes(exit)
if result == -1:
    print("Ruen not found:")
else:
    print("Ruen found")    
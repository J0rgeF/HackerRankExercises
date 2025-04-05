en = int(input())
ren = set(map(int, input().split()))
fn = int(input())
rfn = set(map(int, input().split()))

print (len(ren.symmetric_difference(rfn)))
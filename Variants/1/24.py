s = open('Variants/1/24_9753.txt').readline()
s = s.split("Y")
a = [len(i) for i in s]
mx = max(sum(a[i: i + 151]) for i in range(len(a)))
print(mx + 150)
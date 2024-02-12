from ipaddress import ip_network

ips = ip_network('140.19.96.0/255.255.248.0')
ans = 0
for ip in ips:
    ip = [bin(int(i))[2:] for i in str(ip).split('.')]
    counter = set()
    for i in ip:
        counter.add(str(i).count('1'))
    if len(counter) == 1:
        ans += 1
print(ans)
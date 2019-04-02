lines = []
with open('3.txt', 'r', encoding='utf-8-sig') as f:
    for line in f:
        lines.append(line.strip())
# print(lines)

for line in lines:
    s = line.split(' ') # 分割字串變成清單
    time = s[0][:5] # 清單中的字串也可以當作清單使用
    name = s[0][5:]
    print(time + ' ' + name)



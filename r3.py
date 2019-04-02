lines = []  # 建立一個空清單
with open('3.txt', 'r', encoding='utf-8-sig') as f: # 注意編碼與異常開頭
    for line in f:
        lines.append(line.strip()) # 將每行字串處理過加到lines清單中
# print(lines)

for line in lines:  # 將清單中的字串一行一行撈出來
    s = line.split(' ') # 分割字串變成清單
    time = s[0][:5] # 清單中的字串也可以當作清單使用
    name = s[0][5:]
    print(time + ' ' + name)



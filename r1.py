
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    return lines

def convert(lines):
    new = []
    person = None   # 預設person無值
    for line in lines:
        if line == 'Allen':
            person = 'Allen'
            continue    # 跳下一行
        elif line == 'Tom':
            person = 'Tom'
            continue    # 跳下一行

        if person:  # 若person有值 = True
            new.append(person + ': ' + line)
    return new

def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')

def main():
    # 將input.txt放入read_file函式，return出來的lines清單放入lines變數中
    lines = read_file('input.txt') 
    # 將lines變數放入convert函式，return出來的new清單放入lines變數中
    lines = convert(lines)
    # 將lines變數存入output.txt檔中
    write_file('output.txt', lines)

main()


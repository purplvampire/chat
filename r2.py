
def read_file(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
    return lines


def convert(lines):
    person = None   # 預設person無值
    allen_word_count = 0
    allen_sticker_count = 0
    allen_image_count = 0
    viki_word_count = 0
    viki_sticker_count = 0
    viki_image_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        # print(s)
        if name == 'Allen':
            # 計算貼圖的次數
            if s[2] == '貼圖':
                allen_sticker_count += 1
            # 計算圖片的次數
            elif s[2] == '圖片':
                allen_image_count += 1
            # 計算allen對話字數的加總
            else:
                for m in s[2:]: # 篩選出清單index=2之後的清單項目
                    allen_word_count += len(m)  # 將每行字串長度加總
        elif name == 'Viki':
            # 計算貼圖的次數
            if s[2] == '貼圖':
                viki_sticker_count += 1
            # 計算圖片的次數
            elif s[2] == '圖片':
                viki_image_count += 1
            # 計算allen對話字數的加總
            else:
                for m in s[2:]:
                    viki_word_count += len(m)
    print('allen說了', allen_word_count, '個字')
    print('allen傳了', allen_sticker_count, '個貼圖')
    print('allen傳了', allen_image_count, '張圖片\n')

    print('viki說了', viki_word_count, '個字')
    print('viki傳了', viki_sticker_count, '個貼圖')
    print('viki傳了', viki_image_count, '張圖片')


def write_file(filename, lines):
    with open(filename, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write(line + '\n')


def main():
    # 將input.txt放入read_file函式，return出來的lines清單放入lines變數中
    lines = read_file('-LINE-Viki.txt') 
    # 將lines變數放入convert函式，return出來的new清單放入lines變數中
    convert(lines)
    # 將lines變數存入output.txt檔中
    # write_file('output.txt', lines)

main()


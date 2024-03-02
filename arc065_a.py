# Tに挿入することができる文字列の選択肢は
# dream
# dreamer
# erase
# eraser
# これら好きな回数繰り返してsと合致するかどうか
# dreamerとeraserの文字の区切りがわからんなdreamとeraseの可能性もある
# 逆順から見ていくことで区切りが明確になる
words = ["dream", "dreamer", "erase", "eraser"]
words = [word[::-1] for word in words]
reversed_input = list(reversed(input()))
reversed_S = ''.join(reversed_input)
while len(reversed_S) > 0:
    matched = False
    for word in words:
        if reversed_S.startswith(word):
            reversed_S = reversed_S.replace(word,"",1)
            matched = True
            break
    if not matched:
        break
if len(reversed_S) == 0:
    print("YES")
else:
    print("NO")

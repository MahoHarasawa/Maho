#数字占い

num1=int(input("好きな数字を入力してください⇒"))
if num1 % 3 == 0:
    print()
    print("惜しいです！今日の運勢は中吉です")

elif num1 % 4 == 0:
    print()
    print("おめでとうございます！今日の運勢は大吉です‼")

else:
    print()
    print("今日の運勢は吉です。よい一日を！")

print()

#ラッキーカラー占い

import random

print("今日のあなたのラッキーカラーは…")
print(random.choice("赤青黄緑白黒灰")+"色です！")

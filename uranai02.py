'''ソウルナンバー占い
合計が1桁になるまで足し、最終的に出た数がソウルナンバー
ぞろ目はそのまま'''

#8桁の生年月日を入力 1998/04/11生まれ⇒1,9,9,8,0,4,1,1
num1=int(input("1桁目⇒"))
while num1>=10 or num1<0:
    print("0または1桁の正の数で入力してください")
    print()
    num1=int(input("1桁目⇒"))
num2=int(input("2桁目⇒"))
while num2>=10 or num2<0:
    print("0または1桁の正の数で入力してください")
    print()
    num2=int(input("2桁目⇒"))
num3=int(input("3桁目⇒"))
while num3>=10 or num3<0:
    print("0または1桁の正の数で入力してください")
    print()
    num3=int(input("3桁目⇒"))
num4=int(input("4桁目⇒"))
while num4>=10 or num4<0:
    print("0または1桁の正の数で入力してください")
    print()
    num4=int(input("4桁目⇒"))

num5=int(input("5桁目⇒"))
while num5>=10 or num5<0:
    print("0または1桁の正の数で入力してください")
    print()
    num5=int(input("5桁目⇒"))
num6=int(input("6桁目⇒"))
while num6>=10 or num6<0:
    print("0または1桁の正の数で入力してください")
    print()
    num6=int(input("6桁目⇒"))

num7=int(input("7桁目⇒"))
while num7>=10 or num7<0:
    print("0または1桁の正の数で入力してください")
    print()
    num7=int(input("7桁目⇒"))
num8=int(input("8桁目⇒"))
while num8>=10 or num8<0:
    print("0または1桁の正の数で入力してください")
    print()
    num8=int(input("8桁目⇒"))

total1=num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8
print()
print("合計: ",total1)
#ループ処理を使ってコードの無駄を省けないものか？？

def get_total(x,y):
    return x+y
    #while文がありプログラム内で一度しか使わないため本来は不要

while total1 >= 10:
        if total1 == 11:
            print("あなたのソウルナンバーは11です！ソウルナンバー11の人を一言でいうと「直感で人が何考えているか、どういう人か察知してしまう鋭い感受性」の人です。")
            break
        elif total1 == 22:
            print("あなたのソウルナンバーは22です！ソウルナンバー22の人を一言でいうと「しっかりと準備をしてから行動を行う、冷静な分析力と大胆な行動力」の人です。")
            break
        elif total1 == 33:
            print("あなたのソウルナンバーは33です！ソウルナンバー33の人を一言でいうと「カリスマ性を持つ、人々を魅了する、スター中のスター」です。")
            break
        elif total1 == 44:
            print("あなたのソウルナンバーは44です！ソウルナンバー44の人を一言でいうと「鋭い考えをもった、まさにキレ者。乗り越えられる重責を負う人」です。")
            break
        else:
            num9=int(input("1桁目⇒"))
            while num9>=10:
                print("1桁で入力してください")
                print()
                num9=int(input("1桁目⇒"))
            num10=int(input("2桁目⇒"))
            while num10>=10:
                print("1桁で入力してください")
                print()
                num10=int(input("1桁目⇒"))
            total1=get_total(num9,num10)
            print()
            print("合計: ",total1)

else:
    if total1 == 1:
        print("あなたのソウルナンバーは1です！ソウルナンバー1の人を一言でいうと「才能も運もあるが、ハートが弱く小心者」です。")

    elif total1 == 2:
        print("あなたのソウルナンバーは2です！ソウルナンバー2の人を一言でいうと「頭がよく直感も働くが、短気で人からあれこれ言われたくない人」です。")

    elif total1 == 3:
        print("あなたのソウルナンバーは3です！ソウルナンバー3の人を一言でいうと「面倒見がよく芸術センスもあるがストレスをためやすい人」です。")

    elif total1 == 4:
        print("あなたのソウルナンバーは4です！ソウルナンバー4の人を一言でいうと「働き者でリーダーシップがあるがクールで人間味がない人」です。")

    elif total1 == 5:
        print("あなたのソウルナンバーは5です！ソウルナンバー5の人を一言でいうと「マイペースで安定志向だが恋愛下手な人」です。")

    elif total1 == 6:
        print("あなたのソウルナンバーは6です！ソウルナンバー6の人を一言でいうと「八方美人で愛情深いが裏切りを許さない人」です。")

    elif total1 == 7:
        print("あなたのソウルナンバーは7です！ソウルナンバー7の人を一言でいうと「お調子者でぱわふるだがデリケートで傷つきやすい人」です。")

    elif total1 == 8:
        print("あなたのソウルナンバーは8です！ソウルナンバー8の人を一言でいうと「こだわりが強く金運もあるがものの考え方が極端な人」です。")

    elif total1 == 9:
        print("あなたのソウルナンバーは9です！ソウルナンバー9の人を一言でいうと「記憶力がよく天才肌だが寂しがりや。一番浮気しやすい人」です。")

'''引用
http://soulnumber.me/
https://www.denwauranaichan.com/%E3%82%BD%E3%82%A6%E3%83%AB%E3%83%8A%E3%83%B3%E3%83%90%E3%83%BC/'''

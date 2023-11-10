import random
import xml.etree.ElementTree as ET
import time

def load_config():
    tree = ET.parse('setting.xml')
    root = tree.getroot()
    x1 = int(root.find('x1').text)
    x2 = int(root.find('x2').text)
    n = int(root.find('n').text)
    return x1, x2, n

def play_game(x1, x2, n):
    while True:
        target = random.randint(x1, x2)
        attempts = 0

        while attempts < n:
            guess = int(input(f"猜一個介於 {x1} 到 {x2} 之間的數字："))

            if guess == target:
                print(f"恭喜！你猜對了，目標數字就是 {target}。")
                break
            elif guess < target:
                print("太低了，再猜一次。")
            else:
                print("太高了，再猜一次.")

            attempts += 1

        if attempts == n and guess != target:
            print(f"很抱歉，你已經猜了{n}次，遊戲結束。目標數字是{target}。")

        play_again = input("是否想再次遊戲？ (按Y繼續，按其他鍵退出): ")
        if play_again.lower() != 'y':
            print("再見，希望下次能再玩一局！")
            break

def main():
    x1, x2, n = load_config()
    print(f"遊戲開始！我們將生成一個介於{x1}和{x2}之間的目標數字，試著在{ n }次內猜中它。")
    play_game(x1, x2, n)

if __name__ == "__main__":
    main()
    time.sleep(30)

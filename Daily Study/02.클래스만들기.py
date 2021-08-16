class Monster:
    def say(self):
        print("나는 몬스터다")

orc = Monster()
orc.say()

# 파이썬에서는 자료형도 클래스다
a = 10, # int형 클래스
b = "문자열객체" # string형 클래스
c = True , # 불린형 클래스

print(b.__dir__())
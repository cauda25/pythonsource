# 클래스 정의
# self : 인스턴스 변수
# self 없이 사용 : 클래스 변수
class UserInfo:
    user_count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        UserInfo.user_count += 1

    # toString() 역할
    def __str__(self):
        return f"name : {self.name}, age : {self.age}"


# 객체 생성
user1 = UserInfo("홍길동", 30)
print(user1.uesr_info())
# print(user1.user_count)
print(UserInfo.user_count)


# self == this
class Car:
    # 생성자
    def __init__(self):
        self.color = "Red"
        self.speed = 0

    def up_speed(self, value):
        self.speed += value

    def down_speed(self, value):
        self.speed -= value


car1 = Car()
car2 = Car()

car1.up_speed(100)
car1.down_speed(20)
print(f"car1 자동차 색상은 {car1.color}, 속력은 {car1.speed}")

car2.color = "black"
car1.up_speed(120)
print(f"car2 자동차 색상은 {car2.color}, 속력은 {car2.speed}")

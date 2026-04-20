# print(f'{"hello":*>25}')   # ******************hello
# print(f'{"hello":*<25}')   # hello******************
# print(f'{"hello":*^25}')   # *********hello*********

name = "mult"

# 오른쪽 맞춤 (>)
print(f'{"total price before " + name + " discount":>50}')
# 왼쪽 맞춤 (<)
print(f'{"total price before " + name + " discount":<50}')
# 가운데 맞춤 (^)
print(f'{"total price before " + name + " discount":^50}')

# class Pokemon:
#     # Super() => 부모 클래스의 메서드를 호출할 때 사용
#     def __init__(self):
#         self.hp = 100
    
#     # 자바의 toString()과 같은 역할
#     def __str__(self):
#         return f"Health: {self.hp}"

# p1 = Pokemon()
# print(p1)
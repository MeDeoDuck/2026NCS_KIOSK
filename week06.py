# print(f'{"hello":*>25}')   # ******************hello
# print(f'{"hello":*<25}')   # hello******************
# print(f'{"hello":*^25}')   # *********hello*********

# name = "mult"

# # 오른쪽 맞춤 (>)
# print(f'{"total price before " + name + " discount":>50}')
# # 왼쪽 맞춤 (<)
# print(f'{"total price before " + name + " discount":<50}')
# # 가운데 맞춤 (^)
# print(f'{"total price before " + name + " discount":^50}')

class Pokemon:
    def __init__(self):
        self.hp = 100

    def __str__(self):
        return f"Health: {self.hp}"

p1 = Pokemon()
print(p1)
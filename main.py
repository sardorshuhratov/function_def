# ------------------------------
#         Break, Continue
# -----------------------------
# # 1.
# for i in range(1,11):
#     if i == 5:
#         print(f"{i} topildi")
#         break

# # 2.
# for i in range(1,11):
#     if i % 2 == 1:
#         continue
#     print(i)

# -----------------------------
#         Function-def
# ----------------------------

# # 1
# def alo():
#     for i in range(1, 101):
#         if i % 3 == 0 or i % 5 == 0:
#             print(i, end=" ")
#
# alo()

# # 2.
# def gulruxsor_aytdi():
#     gulruxsor = "Gulruxsor juda aqilli!!!!"
#     print(gulruxsor)
# gulruxsor_aytdi()

# # 3.
# def zaytun_uzum():
#     zaytun = "Zaytun uzum shirin✌️"
#     print(zaytun)
# zaytun_uzum()

# # 4.
# def kitoblar_soni():
#     kitoblar = 5
#     print("Kitoblar soni:", kitoblar)
# kitoblar_soni()

# # 5.
# def chiziq_chiz():
#     belgi = "=" * 40
#     print(belgi)
# chiziq_chiz()
# chiziq_chiz()
# chiziq_chiz()

# -----------------------
#       Return
# ----------------------

# # 1.
# def  kvadrat_top():
#     k = 7
#     natija = k**2
#     return natija
# print(f"Berilgan sonnning kvadrati: {kvadrat_top()}")

# # 2.
# def happy_new_year(name, gurux):
#     print(f"\nHappy New Year to {name}!")
#     print(f"You are good programmer at class {gurux}!")
#     print("Happy birthday to you")
# happy_new_year("Alice", 210)
# happy_new_year("Ali", 205)
# happy_new_year("Vali", 123)

# --------------------------
#           TASKS
# --------------------------

# # 1.
# def greet(ism):
#     print("Hello " + ism)
# greet("Ali")

# # 2.
# def add_number(a, b):
#     return a + b
# a = int(input("a = "))
# b = int(input("b = "))
# print(add_number(a, b))

# # 3.
# n = int(input("n: "))
# def  is_positive(n):
#     return n > 0
# print(is_positive(n))

# # 4.
# x = int(input("Enter a number: "))
# def square(x):
#     return x*x
# print(square(x))

# # 5.
# def is_wovel(harf):
#     if harf == "a" or harf == "o" or harf == "e" or harf == "i" or harf == "u":
#         return True
#     else:
#         return False
# h = str(input("Harf: "))
# print(is_wovel(h))

# # 6.
# def calculate_perimetr(uzunlik, kenglik):
#     return 2 * (uzunlik + kenglik)
# print(f"Perimetri: {calculate_perimetr(10, 5)}")

# # 7.
# def calculate_area(base, height):
#     area = base * height
#     print(area)
#     return area
# base = float(input("Enter the base: "))
# height = float(input("Enter the height: "))
# calculate_area(base, height)

# # 8.
# def is_even(num):
#     return num % 2 == 0
# num = int(input("Son kiriting: "))
# print(is_even(num))

# # 9.
# s1 = int(input("s1: "))
# s2 = int(input("s2: "))
# s3 = int(input("s3: "))
# def find_max(s1, s2,s3):
#     if s1 > s2:
#         return s1
#     elif s2 > s3:
#         return s2
#     else:
#         return s3
#
# print(find_max(s1, s2, s3))

# 10.
# n = int(input("n: "))
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(n))

# ایجاد یک دیکشنری خالی
students_info = {}

# دریافت ورودی‌ها برای 10 دانشجو
for i in range(10):
    # دریافت نام دانشجو
    name = input(f"نام دانشجو {i+1}: ")
    # دریافت سن دانشجو
    age = int(input(f"سن دانشجو {i+1}: "))
    # اضافه کردن نام و سن به دیکشنری
    students_info[name] = age

# نمایش دیکشنری
print("دیکشنری دانشجویان:")
print(students_info)
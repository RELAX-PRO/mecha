# 1. الطريقة التقليدية (المملة)
def add_five(x):
    return x + 5

print(f"Traditional: {add_five(10)}")

# 2. طريقة لامبدا (Lambda Style) - الجوهر النقي
# lambda input: output
# لاحظ: لا يوجد اسم للدالة، هي مجرد "فكرة" تمررها
adder = lambda x: x + 5

print(f"Lambda: {adder(10)}")

# 3. السحر الحقيقي (Currying) - مفهوم متقدم في الخريطة
# دالة تعيد دالة أخرى! (مصنع دوال)
# تخيلها كآلة تصنع آلات
make_adder = lambda n: (lambda x: x + n)

add_10 = make_adder(10) # هذه الآلة تضيف 10
add_100 = make_adder(100) # هذه الآلة تضيف 100

print(f"Factory (+10): {add_10(5)}")   # 15
print(f"Factory (+100): {add_100(5)}") # 105

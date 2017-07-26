speed=40

is_birthday=False
if is_birthday and speed<36 or speed<31:
    print('no ticket')
elif is_birthday and speed>35 and speed<56 or speed>30 and speed<51:
    print('small ticket')
elif is_birthday and speed>55:
    print('big ticket')
else:
    print('big ticket')
    

weigth = 90
is_women = False
limit_weigth = 80
limit_weigth_men = 85
if is_women == True and weigth <= limit_weigth:
    print('is healthly')
elif is_women == True and weigth > limit_weigth:
    print('is unhealthly')
elif is_women == False and weigth <= limit_weigth_men:
    print('is healthly')
elif is_women == False and weigth > limit_weigth_men:
    print('is unhealthly')

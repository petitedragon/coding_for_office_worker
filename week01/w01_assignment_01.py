import random

janre = ['중식','양식','한식']
menu_chinese = ['자금성','만리장성','홍식당']
menu_western = ['JongJong Haberg','BongBong pasta','SoSo Steak']
menu_korean = ['먹자먹자','조금만먹지','많이먹자']


def choose_restaurant(janre):
    p_janre = (input("다음중 한가지를 고르세요 {}".format(janre) ))
    #p_janre = '중식'
    #p_janre = '양식'
    #p_janre = '일식'
               
    if p_janre == '중식':
        return  random.choice(menu_chinese) 
    elif p_janre == '양식':
        return  random.choice(menu_western) 
    elif p_janre == '한식':
        return  random.choice(menu_korean) 
    else:
        return ("중식 양식 한식 중 하나를 입력해주세요")
               
        

print(choose_restaurant(janre))

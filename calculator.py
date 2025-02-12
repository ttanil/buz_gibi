import random

def correctingNumbers(number):
    liste_yeni = []
    for i in number:
        liste_yeni.append(i)
    liste_yeni.pop()
    liste_yeni_str = ""
    for i in range(0, len(liste_yeni)):
        liste_yeni_str += liste_yeni[i]
    number = liste_yeni_str
    return number

def generateNumber_a():
    a=random.randint(0,9)
    return a

def generateNumber_b():
    b=random.randint(0,9)
    return b

def calculate(string_list,number_a,number_b):
    number_list = []
    for i in range(0,len(string_list)):
        number_list.append(int(string_list[i]))
    toplam = 0
    for i in range(0,len(number_list)):
        toplam += number_list[i] * (10**(len(number_list)-(i+1)))
    if toplam==(int(number_a)*int(number_b)):
        return True
    return False

def generateFakeResult_a(result):
    while True:
        if 0<=result<10:
            fake_result_a=random.randint(0,9)
        elif 10<=result<20:
            fake_result_a=random.randint(10,19)
        elif 20<=result<30:
            fake_result_a=random.randint(20,29)
        elif 30<=result<40:
            fake_result_a=random.randint(30,39)
        elif 40<=result<50:
            fake_result_a=random.randint(40,49)
        elif 50<=result<60:
            fake_result_a=random.randint(50,59)
        elif 60<=result<70:
            fake_result_a=random.randint(60,69)
        elif 70<=result<80:
            fake_result_a=random.randint(70,79)
        elif 80<=result<90:
            fake_result_a=random.randint(80,89)
        if fake_result_a!=result:
            break
    return fake_result_a

def generateFakeResult_b(result,result_b):
    while True:
        fake_result_b=random.randint(0,81)
        if fake_result_b!=result and fake_result_b!=result_b:
            break
    return fake_result_b

def generateResultLocation():
    location_list = [480, 620, 760]
    location_list_new=[]
    for i in range(3):
        location_list_new.append(random.choice(location_list))
        location_list.remove(location_list_new[i])
    location_list=list(location_list_new)
    return location_list

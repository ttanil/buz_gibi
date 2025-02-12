import random

destination = [[370,270],[430,270],[490,270],[550,270],[610,270],[670,270],[730,270],
               [390,290],[450,290],[510,290],[570,290],[630,290],[690,290],[750,290],
               [410,310],[470,310],[530,310],[590,310],[650,310],[710,310],[770,310],
               [430,330],[490,330],[550,330],[610,330],[670,330],[730,330],[790,330],
               [450,350],[510,350],[570,350],[630,350],[690,350],[750,350],[810,350],
               [470,370],[530,370],[590,370],[650,370],[710,370],[770,370],[830,370],
               [490,390],[550,390],[610,390],[670,390],[730,390],[790,390],[850,390]]

#number=random.choice([2023,2032,2029,2027,2028,2044,2040,2039,2038,2036,2050,2052,2055,2057,2060,2063,2064,2070,2071,2081,2083,2087,2088,2092,2093,2094])
#random.seed(number)

def makePosyList():
    number_list=[]
    for i in range(7):
        number_list.append(random.choice([0,7,14,21,28,35,42]))
    posy_list_for_seal=[]
    for number in number_list:
        posy_list_for_seal.append(destination[number][1])
    return posy_list_for_seal

#posy_list_for_seal=makePosyList()
#print(posy_list_for_seal)

def ice_on_sea():                                                                                                       #buz parçalarının tüm kütlelerinin kapladığı koordinat aralığını verir
    ice_on_sea_number=[]
    for i in range(0,len(destination)):
        ice_on_sea_number.extend([[destination[i][0]-30,destination[i][0]+30,destination[i][1]-10,destination[i][1]+10]])
    return ice_on_sea_number

ice_on_sea_list=ice_on_sea()

def T_shapeConnection():                                                                # T şeklinde 4 bağlantılı connection oluşturur.
    off_list_T=[]
    t=random.randint(1,47)
    while t==6 or t==42:
        t = random.randint(1, 47)
    if t<=5:
        taraf="alt"
    elif 42<=t<=47:
        taraf = "üst"
    elif t==13 or t==20 or t==27 or t==34 or t==41:
        taraf = "sol"
    elif t==7 or t==14 or t==21 or t==28 or t==35:
        taraf = "sağ"
    else:
        taraf=random.choice(["alt","üst","sağ","sol"])
    T_shape=[t,taraf]
    if T_shape[1]=="alt":
        off_list_T.extend([T_shape[0],T_shape[0]+1,T_shape[0]-1,T_shape[0]+7])
    elif T_shape[1]=="üst":
        off_list_T.extend([T_shape[0],T_shape[0]+1,T_shape[0]-1,T_shape[0]-7])
    elif T_shape[1]=="sağ":
        off_list_T.extend([T_shape[0],T_shape[0]+7,T_shape[0]-7,T_shape[0]+1])
    else:
        off_list_T.extend([T_shape[0], T_shape[0] + 7, T_shape[0] - 7, T_shape[0] - 1])
    return off_list_T

def increaseT_ShapeConnection(list1):                    # T şeklinde olan connectionları aynı bağlantıları kullanmayacak şekilde çoğaltır.
    status=True
    while status:
        counter=0
        list=T_shapeConnection()
        for num in list:
            for sayı in list1:
                if num==sayı:
                    break
                else:
                    counter+=1
                    if len(list)*len(list1)==counter:
                        list1 = list1 + list
                        status=False
    return list1

for_two_group=increaseT_ShapeConnection(T_shapeConnection())                                #aynı bağlantıları kullanmayacak şekilde toplam 2 tane T şeklinde connection üretir.

def I_shapeConnection():
    off_list_I = []
    ı = random.randint(0, 48)
    if ı<=13:
        taraf="alt"
    elif 35<=ı<=48:
        taraf = "üst"
    elif ı==12 or ı==13 or ı==19 or ı==20 or ı==26 or ı==27 or ı==33 or ı==34 or ı==40 or ı==41:
        taraf = "sol"
    elif ı==7 or ı==8 or ı==14 or ı==15 or ı==21 or ı==22 or ı==28 or ı==29 or ı==35 or ı==36:
        taraf = "sağ"
    else:
        taraf=random.choice(["alt","üst","sağ","sol"])
    I_shape=[ı,taraf]
    if I_shape[1]=="alt":
        off_list_I.extend([I_shape[0],I_shape[0]+7,I_shape[0]+14])
    elif I_shape[1]=="üst":
        off_list_I.extend([I_shape[0],I_shape[0]-7,I_shape[0]-14])
    elif I_shape[1]=="sağ":
        off_list_I.extend([I_shape[0],I_shape[0]+1,I_shape[0]+2])
    else:
        off_list_I.extend([I_shape[0],I_shape[0]-1,I_shape[0]-2])
    return off_list_I

def increaseI_ShapeConnection(list1):                    #I şeklinde olan connectionları aynı bağlantıları kullanmayacak şekilde çoğaltırak T listesine ekler.
    status=True
    while status:
        counter=0
        list=I_shapeConnection()
        for num in list:
            for sayı in list1:
                if num==sayı:
                    break
                else:
                    counter+=1
                    if len(list)*len(list1)==counter:
                        list1 = list1 + list
                        status=False
    return list1

I_group1=increaseI_ShapeConnection(for_two_group)
I_group2=increaseI_ShapeConnection(I_group1)
I_group3=increaseI_ShapeConnection(I_group2)                                                #toplam 2 tane I şeklinde connection üretir.

def ı_shapeConnection():
    off_list_ı = []
    ı = random.randint(0, 48)
    if ı<=6:
        taraf="alt"
    elif 42<=ı<=48:
        taraf = "üst"
    elif ı==13 or ı==20 or ı==27 or ı==34 or ı==41:
        taraf = "sol"
    elif ı==7 or ı==14 or ı==21 or ı==28 or ı==35:
        taraf = "sağ"
    else:
        taraf=random.choice(["alt","üst","sağ","sol"])
    ı_shape=[ı,taraf]
    if ı_shape[1]=="alt":
        off_list_ı.extend([ı_shape[0],ı_shape[0]+7])
    elif ı_shape[1]=="üst":
        off_list_ı.extend([ı_shape[0],ı_shape[0]-7])
    elif ı_shape[1]=="sağ":
        off_list_ı.extend([ı_shape[0],ı_shape[0]+1])
    else:
        off_list_ı.extend([ı_shape[0],ı_shape[0]-1])
    return off_list_ı

def increase_ı_ShapeConnection(list1):                    #ı şeklinde olan connectionları aynı bağlantıları kullanmayacak şekilde çoğaltırak T ve I listesine ekler.
    status=True
    while status:
        counter=0
        list=ı_shapeConnection()
        for num in list:
            for sayı in list1:
                if num==sayı:
                    break
                else:
                    counter+=1
                    if len(list)*len(list1)==counter:
                        list1 = list1 + list
                        status=False
    return list1

ı_group1=increase_ı_ShapeConnection(I_group3)
ı_group2=increase_ı_ShapeConnection(ı_group1)
ı_group3=increase_ı_ShapeConnection(ı_group2)
ı_group4=increase_ı_ShapeConnection(ı_group3)

def increase_single_ShapeConnection(list1):                    #tekli connectionları çoğaltırak T, I ve ı listesine ekler.
    status=True
    while status:
        counter=0
        num=random.randint(0,48)
        for sayı in list1:
            if num==sayı:
                break
            else:
                counter+=1
                if len(list1)==counter:
                    list1.append(num)
                    status=False
    return list1

single1=increase_single_ShapeConnection(ı_group4)
single2=increase_single_ShapeConnection(single1)
single3=increase_single_ShapeConnection(single2)
single4=increase_single_ShapeConnection(single3)
single5=increase_single_ShapeConnection(single4)
single6=increase_single_ShapeConnection(single5)
single7=increase_single_ShapeConnection(single6)
single8=increase_single_ShapeConnection(single7)
single9=increase_single_ShapeConnection(single8)
single10=increase_single_ShapeConnection(single9)
single11=increase_single_ShapeConnection(single10)
single12=increase_single_ShapeConnection(single11)
single13=increase_single_ShapeConnection(single12)
single14=increase_single_ShapeConnection(single13)
single15=increase_single_ShapeConnection(single14)
single16=increase_single_ShapeConnection(single15)
single17=increase_single_ShapeConnection(single16)
single18=increase_single_ShapeConnection(single17)
single19=increase_single_ShapeConnection(single18)
single20=increase_single_ShapeConnection(single19)
single21=increase_single_ShapeConnection(single20)
single22=increase_single_ShapeConnection(single21)
single23=increase_single_ShapeConnection(single22)
single24=increase_single_ShapeConnection(single23)                          #toplam 49 eleman olacak şekilde bütün bağlantıları oluşturur.

#print(single24)
#print(len(single24))
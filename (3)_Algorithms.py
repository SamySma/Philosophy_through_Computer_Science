
coin1 = 10 
coin2 = 10
coin3 = 11

if coin1 == coin2:
    if coin1 == coin3:
        print('there are no counterfeit coins')
    elif coin1 > coin3:
        print('coin3 is counterfeit and lighet')
    else:
        print('coin3 is counterfeit and heavier')
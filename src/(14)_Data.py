#(14)_Data

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


# f = open('info.txt','r')


# lines = f.readlines()
# print(lines)

# f = open('new.txt','w')
# f.write('Hello World \n')
# f.write('Does this work?')



f = open('nbaallelo.csv', 'r')


lines = f.readlines()


# for line in lines[1:]:
#     data = line.split(',')
#     print(data[8],data[12])



def team_ELO(code,year):
    elo_n = []

    for line in lines:
        data = line.split(',')
        if data[8] == code and data[4] == str(year):
            elo_n.append(data[12])
    
    return elo_n


# print(team_ELO('GSW',2015))

# def word(sentence,n):
#     words = sentence.split(',')
#     return words[n]


# print(word('allo, ello, allo, a, a, ac, d, d, ,e ,e',3))


def season_team_ELO(code,year):
    elo_n = []

    for line in lines:
        data = line.split(',')
        if data[8] == code and data[4] == str(year) and data[7] == '0':
            elo_n.append(float(data[12]))
    
    return elo_n


LAL_ELOS = season_team_ELO('LAL',2009)

LAL_X = [i for i in range(len(LAL_ELOS))]

GSW_ELOS = season_team_ELO('GSW',2009)
GSW_X = [i for i in range(len(GSW_ELOS))]


plt.scatter(LAL_X,LAL_ELOS,label = 'Lakers')
plt.scatter(GSW_X,GSW_ELOS,label = 'Warriors')
plt.legend()
plt.grid()
plt.show()


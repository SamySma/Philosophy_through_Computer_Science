# (15)_Machine_Learning

import matplotlib.pyplot as plt
import re
import numpy as np
import sklearn
from sklearn.linear_model import *
from sklearn.preprocessing import *
from sklearn.cluster import *
import math


# height = [164,171,180,187,192]
# weight = [61,74,75,77,94]



# # On cherche a et b qui minimise la distance
# # arg min [Somme (Yi - (a*Xi + b))** 2]

# def linear_regression(X, Y):
#     n = len(X)
#     sum_x = sum(X)
#     sum_y = sum(Y)
#     sum_xy = sum(x * y for x, y in zip(X, Y))
#     sum_x2 = sum(x**2 for x in X)
    
#     a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x**2)
#     b = (sum_y * sum_x2 - sum_x * sum_xy) / (n * sum_x2 - sum_x**2)
    
#     return a, b

# # Calculate coefficients
# a, b = linear_regression(height, weight)

# # Predicted values
# predicted_weight = [a * x + b for x in height]

# plt.scatter(height,weight, label = 'Actual Data')
# plt.plot(height,predicted_weight, color = 'red', label = 'Linear regression')
# plt.grid()
# plt.show()


# s = '1: 198 cm, 90 kg 2: 216 cm, 128 kg 3: 203 cm, 112 kg 4: 191 cm, 84 kg 5: 198 cm, 82 kg 6: 182 cm, 77 kg 7: 184 cm, 82 kg 8: 193 cm, 80 kg 9: 190 cm, 90 kg 10: 175 cm, 76 kg'

# # Extract all height and weight values using regular expressions
# heights = re.findall(r'(\d+) cm', s)
# weights = re.findall(r'(\d+) kg', s)

# # Convert the extracted string values to integers
# heights = list(map(int, heights))
# weights = list(map(int, weights))

# plt.scatter(heights,weights, label = 'Actual Data')
# plt.grid()
# plt.show()

# d = np.array([[164,30,61],[171,48,74],[180,32,75],\
#               [187,33,77],[192,50,94]])

# d = np.array([[164,61],[171,74],[180,75],[187,77],[192,94]])


data = np.array([[198,90],[216,148],[203,120],[191,84],\
                [198,82],[182,77],[184,82],[193,80]])

# t = PolynomialFeatures(degree=5)

# model = LinearRegression()

# X = d[:,:2]
# Y = d[:,2]

# model.fit(X,Y)
# print(model.predict([[185,35]]))

# model.fit(t.fit_transform(d[:,:1]),d[:,1])
# print(model.predict(t.fit_transform([[185]])))


kmeans = KMeans(init='random',n_clusters=2)
kmeans.fit(data)

G1,G2 = kmeans.cluster_centers_
new_data = np.array([190,83])
dist1 = math.sqrt(np.sum((G1-new_data)**2))
dist2 = math.sqrt(np.sum((G2-new_data)**2))

if dist1 < dist2:
    print('new data should be classified as G1')
else:
    print('new data should be classified as G2')









import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt


# print('Please, define data (data1,data2...data4) and ')
dt = 'data2'
if len(sys.argv)<2:
    print("Data not specified. Using data2 as example for 3 months deposition for the 1st term of gaussian error series")
else:
    dt =sys.argv[1]
data = pd.read_csv('data/{}.txt'.format(dt), sep=" ", header=None)
#Defining ‘X’ as independent variable and ‘Y’ as dependent variable
X = data[0].values
Y = data[1].values

# this is equivalent to: alpha = np.linalg.lstsq(A, y, rcond=None)[0]
# def get_alpha(X,Y):
def A_erf_pol_exp(X, num_ex):
    A = []
    for i in range(num_ex):
        A.append(X**(2*i+1))
    A.append(np.ones(len(X)))
    return np.vstack(A).T

A = A_erf_pol_exp(X, 1)
Y = Y[:, np.newaxis]
p = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),Y) # can be also defined using pseudo-inverse, np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)) = np.linalg.pinv(A)
    # return alpha                                       # but for the sake of understanding this method, better to show it explicit

plt.figure(figsize = (10,8))
plt.plot(X, Y, 'b.')
plt.plot(X, np.dot(A,p), 'r')
plt.xlabel('x')
plt.ylabel('y')
# plt.show()
plt.savefig("plots/{}_ls.pdf".format(dt))

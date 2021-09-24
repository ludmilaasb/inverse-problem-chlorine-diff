import numpy as np
import pandas as pd
import sys
import matplotlib.pyplot as plt

if len(sys.argv) == 2 and sys.argv[1] in ['-h','--help']:
    print('Please, define data (data1,data2...data4), time (3 or 6) and terms of gaussian error series (must be natural number)')
    exit()

dt = 'data2'
time = 2
num_ex = 3

if len(sys.argv)<2:
    print("Data not specified. Using data2 as example for 6 months deposition for the 3rd term of gaussian error series. In case of doubt, just use help (-h, --help)")
else:
    dt =sys.argv[1]
    assert dt in ['data1','data2','data3','data4'], "data must by like: 'data1','data2','data3','data4'"
    time = int(sys.argv[2])/3
    assert time in [1,2] , 'time must be equal to 3 or 6'
    num_ex = int(sys.argv[3])
    assert num_ex > 0 , "expanssion term must be integer and positive    "

data = pd.read_csv('data/{}.txt'.format(dt), sep=" ", header=None)
# Defining ‘X’ as independent variable and ‘Y’ as dependent variable
X = data[0].values
Y = data[time].values

# this is equivalent to: alpha = np.linalg.lstsq(A, y, rcond=None)[0]
# def get_alpha(X,Y):
def A_erf_pol_exp(X, num_ex):
    A = []
    for i in range(num_ex):
        A.append(X**(2*i+1))
    A.append(np.ones(len(X)))
    return np.vstack(A).T

A = A_erf_pol_exp(X, num_ex)

Y = Y[:, np.newaxis]
p = np.dot((np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)),Y) # can be also defined using pseudo-inverse, in other words, np.dot(np.linalg.inv(np.dot(A.T,A)),A.T)) = np.linalg.pinv(A)
                                                         # but for the sake of understanding this method, better to show it explicit

# ------ Parameters estimation -------
num_monts = 3*time
month2seconds = num_monts*30*24*60*60

D = p[-1][0]/(np.pi*(p[0][0]**2)*month2seconds)
print('It seems that the answer is D = {} and rho={}'.format(D,p[-1][0]))

# ------ Plotting -------
plt.figure(figsize = (10,8))
plt.plot(X, Y, 'b.')
plt.plot(X, np.dot(A,p), 'r')
plt.xlabel('x')
plt.ylabel('y')
# plt.show()
plt.savefig("plots/{}_erf-exp_{}_least_squares.pdf".format(dt,num_ex))











print("If u copy this, u r dumb") 

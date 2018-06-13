import numpy as np
from sklearn import preprocessing

X = np.array([[1., -1., 2.],
              [2., 0., 0.],
              [0., 1., -1.]])
X_scaled = preprocessing.scale(X, with_mean=True)
#
print ("X_scaled: ", X_scaled)
# print "X_scaled mean: ", X_scaled.mean(axis=0)
print ("X_scaled std: ", X.std(axis=0))

m = np.mean(X, axis=0)
std = np.std(X, axis=0)
X_norm = ((X - m)  / std)
print (X_norm)


#
# print ""
# print ""
# print "STANDART SCALER"
# scaler = preprocessing.StandardScaler().fit(X)
# print scaler
# print "X_scaled mean: ", scaler.mean_
# print "X_scaled std: ", scaler.scale_
#
# print "X_scaled: ", scaler.transform(X)
#
# print scaler.transform([[-1., 1., 0.]])

# The function normalize provides a quick and easy way to perform this operation on
#  a single array-like dataset, either using the l1 or l2 norms:

print ("")
print ("")
print ("NORMALIZATION")

X = [[1., -1., 2.],
     [2., 0., 0.],
     [0., 1., -4.]]
X_normalized = preprocessing.normalize(X, norm='l2', axis=0)
print ("")
print  (X_normalized)


X_normalized = preprocessing.normalize(X, norm='l1', axis=0)
print ("")
print  (X_normalized)

X_normalized = preprocessing.normalize(X, norm='max', axis=0)
print ("")
print  (X_normalized)



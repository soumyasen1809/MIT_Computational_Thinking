from sklearn.cluster import KMeans
import numpy as np
from matplotlib import pyplot as plt


def readFile(fileName):
    cardiacData = open('cardiacData.txt', 'r')
    hrList, stElevList, ageList, prevACSList, classList = [], [], [], [], []
    for l in cardiacData:
        l = l.split(',')
        hrList.append(int(l[0]))
        stElevList.append(int(l[1]))
        ageList.append(int(l[2]))
        prevACSList.append(int(l[3]))
        classList.append(int(l[4]))
    return hrList, stElevList, ageList, prevACSList, classList


hrList, stElevList, ageList, prevACSList, classList = readFile("cardiacData.txt")

feature_list = []
for i in range(len(hrList)):
        # features = np.array([hrList[i], prevACSList[i], stElevList[i], ageList[i]])
        feature_list.append([hrList[i], prevACSList[i], stElevList[i], ageList[i]])
# print feature_list

kmean_value = KMeans(n_clusters=4).fit(feature_list)
print ("\n Kmeans algorithm details: \t" + str(kmean_value))

kmean_centroid = kmean_value.cluster_centers_
print ("\n Kmeans centers: \n" + str(kmean_centroid))

# plt.scatter(kmean_centroid[:,0], kmean_centroid[:,1])
# plt.show()
#
# plt.scatter(kmean_centroid[:,1], kmean_centroid[:,2])
# plt.show()
#
# plt.scatter(kmean_centroid[:,2], kmean_centroid[:,3])
# plt.show()

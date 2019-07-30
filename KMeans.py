import math
def solution(arr):
    h = len(arr) - 1
    #Fitst Clustered Number
    c1 = arr[0]
    c2 = arr[1]
    previous_c1 = []
    previous_c2 = []
    while previous_c1 != c1 and previous_c2 != c2:
        cluster_c1 = []
        cluster_c2 = []
        for i in range(len(arr)):

            cent_dist_c1 = math.sqrt(((arr[i][0] - c1[0])**2) + ((arr[i][1] - c1[1])**2))
            cent_dist_c2 = math.sqrt(((arr[i][0] - c2[0])**2) + ((arr[i][1] - c2[1])**2))

            #determine which cluster id
            if cent_dist_c2 > cent_dist_c1 >= 1:
                cluster_c1.append(arr[i])
            elif cent_dist_c1 > cent_dist_c2 >= 1:
                cluster_c2.append(arr[i])

        if len(cluster_c1) >= 1:
            previous_c1 = c1
            c1 = [sum([z[0] for z in cluster_c1]) / len(cluster_c1), sum([z[1] for z in cluster_c1]) / len(cluster_c1)]

        if len(cluster_c2) >= 1:
            previous_c2 = c2
            c2 = [sum([z[0] for z in cluster_c2]) / len(cluster_c2), sum([z[1] for z in cluster_c2]) / len(cluster_c2)]

    return "Cluster coordinates of centroids " + str(c1) + ": " + str(cluster_c1) + "\nCluster coordinates of centroids " + str(c2) + ": " + str(cluster_c2)

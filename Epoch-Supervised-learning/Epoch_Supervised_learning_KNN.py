import numpy as np
import math

class KNN:
    def __init__(self,k):
        self.k=k
    def fit(self,X,y):
        self.X = X
        self.y = y
    def predict_one(self,x):
        k_nearest_neighbours=[]
        index=0
        for sample in self.X:
            dist=Euclidean_dist(x,sample)
            k_nearest_neighbours.append([dist,self.y[index]])
            index+=1
        k_nearest_neighbours = sorted(k_nearest_neighbours, key=lambda x: x[0])
        zero_freq=0
        one_freq=0
        two_freq=0
        for i in range(0,self.k):
            if(k_nearest_neighbours[i][1]==0):
                zero_freq+=1
            elif(k_nearest_neighbours[i][1]==1):
                one_freq+=1
            else:
                two_freq+=1
        print(f"Zero frequency : {zero_freq}")
        print(f"One frequency : {one_freq}")
        print(f"Two frequency : {two_freq}")
        if(zero_freq > one_freq and zero_freq > two_freq):
            return "Apple"
        elif(one_freq > zero_freq and one_freq > two_freq):
            return "Banana"
        else:
            return "Orange"
    def predict(self,X_test):
        y_result=[]
        for sample in X_test:
            y_result.append(self.predict_one(sample))
        y_result=np.array(y_result)
        return y_result
        

def Euclidean_dist(point1,point2):
    runningSum=0
    for i in range(0,len(point1)):
        runningSum+=(point1[i]-point2[i])**2
    distance=math.sqrt(runningSum)
    return distance

def main():
    data = [
    [150, 7.0, 1, 'Apple'],
    [120, 6.5, 0, 'Banana'],
    [180, 7.5, 2, 'Orange'],
    [155, 7.2, 1, 'Apple'],
    [110, 6.0, 0, 'Banana'],
    [190, 7.8, 2, 'Orange'],
    [145, 7.1, 1, 'Apple'],
    [115, 6.3, 0, 'Banana']
]
    X=[]
    y=[]
    for sample in data:
        X.append([sample[0],sample[1],sample[2]])
        if(sample[3]=='Apple'):
            y.append(0)
        elif(sample[3]=='Banana'):
            y.append(1)
        else:
            y.append(2)
    X = np.array(X)
    y = np.array(y)
    knn = KNN(3)
    knn.fit(X,y)
    test_data = np.array([
    [118, 6.2, 0],  # Expected: Banana
    [160, 7.3, 1],  # Expected: Apple
    [185, 7.7, 2]   # Expected: Orange
    ])
    predictions=knn.predict(test_data)
    for i in range(0,len(predictions)):
        print(f"{test_data[i]} : {predictions[i]}")

if __name__=="__main__":
    main()

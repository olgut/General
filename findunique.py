# finds the unique element of a given array
def findunique(array):
    if len(array)==1:
        return array
    for i in range(len(array)):
        duplicate =[j for j in array if j==array[i]]
        if len(duplicate)<2:
            return duplicate

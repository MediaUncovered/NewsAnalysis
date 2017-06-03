
def sortByScore(tupleList, reverse=False):
    return sorted(tupleList, key=lambda x:(x[1], x[0]), reverse=reverse)

def filterList(tupleList, threshold, absolutValue=False):
    if absolutValue:
        return [elem for elem in tupleList if abs(elem[1])>=threshold]
    return [elem for elem in tupleList if elem[1]>=threshold]

#def combineList(self, inputList):
#    if type(inputList) is list:
#        if isString(inputList[0]):
#            inputList[0] = self.model[inputList[0]]
#        if isString(inputList[1]):
#            inputList[1] = self.model[inputList[1]]
#        return inputList[0]-inputList[1] 
#    return inputList

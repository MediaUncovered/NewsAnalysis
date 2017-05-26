
def sortByScore(tupleList, reverse=False):
    return sorted(tupleList, key=lambda x:(x[1], x[0]), reverse=reverse)

def filterList(tupleList, threshold, absolutValue=False):
    if absolutValue:
        return [elem for elem in tupleList if abs(elem[1])>=threshold]
    return [elem for elem in tupleList if elem[1]>=threshold]


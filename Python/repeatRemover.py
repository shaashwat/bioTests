def remove_duplicates(undup):
    edittedList=[]
    for i in undup:
        if i not in edittedList:
            edittedList.append(i)
    return edittedList


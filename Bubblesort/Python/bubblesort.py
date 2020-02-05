# the bubbleSort function definition
def bubbleSort(nlist):
    # defining a range of numbers to pick from, in this case from the first one to the last one
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
        # ompares 2 values that are right next to each other, if the one on the right is bigger keep it that way and move to the nex pair
        # if the nex pair is not like that however, swap them and then keep on checking
        # this is repeated until all the numbers are sorted
            if nlist[i]>nlist[i+1]:
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp

# defining our list of numbers that are not yet sorted
nlist = [28,86,33,7,17,21,145,221,60]
# printing the unsorted list on the screen
print("unsorted")
print(nlist)
# using our bubbleSort function on our list of numbers
bubbleSort(nlist)
# printing the sorted list on the screen
print("sorted")
print(nlist)
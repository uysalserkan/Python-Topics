def ArrayAdvence(A):
    """ Is it possible to advance from the start 
    of the array to the last element given that the 
    maximum you can advance from a position is based 
    on the value of the array at the index you are currently present on? """

    max_reached = 0
    last_index = len(A) - 1
    i = 0
    while i <= max_reached and max_reached < last_index:
        max_reached = max(max_reached, A[i]+i)
        i += 1
    return max_reached >= last_index


def AddOneTheNums(A):
    A[-1] += 1
    for index in reversed(range(1, len(A))):
        if A[index] != 10:
            break
        else:
            A[index] = 0
            A[index-1] += 1
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


def CheckSumBruteForce(Arr, Target):
    """ This function only 1 return which is first reachable """
    for i in range(len(Arr)-1):
        for j in range(i+1, len(Arr)):
            if Arr[i] + Arr[j] == Target:
                print(Arr[i], Arr[j])
                return True
    return False


def CheckSumBasic(Arr, Target):
    i = 0
    j = len(A) - 1

    while i < j:
        if Arr[i] + Arr[j] == Target:
            print(Arr[i], Arr[j])
            return True
        elif Arr[i] + Arr[j] < Target:
            i += 1
        else:
            j -= 1
    return False


def IntersectionArrays(Arr1, Arr2):
    intersectArr = []

    for i in range(len(Arr1)):
        for j in range(len(Arr2)):
            if Arr1[i] == Arr2[j]:
                intersectArr.append(Arr2[j])
    intersectArr.pop(0)
    return intersectArr


A = [3, 3, 1, 0, 2, 0, 1]
print(ArrayAdvence(A))

A = [3, 2, 0, 0, 2, 0, 1]
print(ArrayAdvence(A))
A1 = [1, 4, 9]
A2 = [9, 9, 9]
print(AddOneTheNums(A1))
print(AddOneTheNums(A2))

target = 10
arr = [2, 5, 8, 11, 21, 3, 18, 7]
CheckSumBruteForce(arr, target)
CheckSumBasic(arr, target)

print("Intersection of 2 Array: "+str(IntersectionArrays(arr, A)))

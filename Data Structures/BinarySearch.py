class BinarySearch:
    @classmethod
    def LinearSearch(cls, data, target):
        """
        Complexity is O(n)
        """
        for i in range(len(data)):
            if data[i] == target:
                return True
        return False

    @classmethod
    def BinarySearch(cls, data, target):
        """
        Complexity is O(Log(N))
        """
        start = 0
        end = len(data) - 1

        while start <= end:
            mid = (start + end) // 2
            if data[mid] == target:
                return True
            elif data[mid] > target:
                end = mid - 1
            else:
                start = mid + 1
        return False

    @classmethod
    def RecursiveBinarySearch(cls, data, target, start, end):
        """
        Complexity is O(Log(N))
        """
        if start > end:
            return False
        else:
            mid = (start + end) // 2
            if data[mid] == target:
                return True
            elif data[mid] > target:
                return RecursiveBinarySearch(data, target, start, mid-1)
            else:
                return RecursiveBinarySearch(data, target, mid+1, end)

    @classmethod
    def FindClosestNum(cls, data, target):
        """ Complexity is O(Log(N)) """
        min_dif = float("inf")
        start = 0
        end = len(data) - 1
        closestNum = None

        if len(data) == 0:
            return None
        if len(data) == 1:
            return data[0]

        while start <= end:
            mid = (start + end) // 2

            if mid+1 < len(data):
                min_dif_r = abs(data[mid+1] - target)
            if mid > 0:
                min_dif_l = abs(data[mid - 1] - target)

            if min_dif_l < min_dif:
                min_dif = min_dif_l
                closestNum = data[mid-1]

            if min_dif_r < min_dif:
                min_dif = min_dif_r
                closestNum = data[mid+1]

            if data[mid] < target:
                start = mid + 1
            elif data[mid] > target:
                end = mid - 1

            else:
                return data[mid]

        return closestNum

    @classmethod
    def FindFixedPoint__Linear(cls, data):
        """ Complexity O(N) """
        for i in range(len(data)):
            if data[i] == i:
                return data[i]
        return None

    @classmethod
    def FindFixedPoint(cls, data):
        start = 0
        end = len(data) - 1

        while start <= end:
            mid = (start+end)//2

            if data[mid] < mid:
                start = mid+1
            elif data[mid] > mid:
                end = mid - 1
            else:
                return data[mid]
        return None

    # ? Bitonic peak

    @classmethod
    def FindNumberOfIndex__UNSORTED(cls, data, target):
        """ Complexity O(N) """
        for i in range(len(data)):
            if data[i] == target:
                return i
        return None

    @classmethod
    def FindNumberOfIndex__SORTED(cls, data, target):
        """ Complexity O(Log(N)) """
        start = 0
        end = len(data)-1

        while start <= end:
            mid = (start+end)/2

            if data[mid] < target:
                start = mid + 1
            elif data[mid] > target:
                end = mid - 1

            else:
                if mid - 1 < 0:
                    return mid
                if data[mid] != target:
                    return mid
                end = mid - 1

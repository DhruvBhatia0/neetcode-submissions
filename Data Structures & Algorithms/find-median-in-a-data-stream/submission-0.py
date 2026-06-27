import bisect

class MedianFinder:

    def __init__(self):
        self.sorted_array = []

    def addNum(self, num: int) -> None:
        insert_at = bisect.bisect_left(self.sorted_array, num)

        self.sorted_array.insert(insert_at, num)

    def findMedian(self) -> float:

        array_last_index = len(self.sorted_array) - 1

        if array_last_index % 2 == 0:
            return self.sorted_array[(array_last_index//2)]
        else:
            return (self.sorted_array[array_last_index//2 + 1] + self.sorted_array[array_last_index//2])/2
        
        
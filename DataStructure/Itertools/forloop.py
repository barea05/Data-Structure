#for loop is implemented through itertools method

nums = [1,2,34,4]
i_item = iter(nums)

while True:
    try:
        item = next(i_item)
        print(item)
    except StopIteration:
        print("Traversed to the end of the list")
        break


class MyRange:
    def __init__(self, start, end ):
        self.value = start
        self.end = end
    def __iter__(self):
        return self
    def __next__(self):
        if self.value >= self.end:
            raise StopIteration
        current = self.value
        self.value +=1
        return current

def my_range(start, end):
    current = start
    while current < end:
        yield current
        current +=1

#simplified range function instead of writing whole calss
nums = my_range(1,10)
for num in nums:
    print(num)
print("---------------------")
nums = MyRange(1,10)
for num in nums:
    print(num)
print("****************************")

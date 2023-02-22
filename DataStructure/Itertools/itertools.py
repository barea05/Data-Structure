
import itertools

#use count in zip function
data = [12,34,12,21]
daily_data = list(zip(itertools.count(), data))
for num in daily_data:
    print(num)

print("*******************")

counter = itertools.count(start= 5, step = .2)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))

print("*******************")
#print till the len of data/range
daily_data = list(zip(range(10), data))
print(daily_data)

print("*******************")

daily_data = list(itertools.zip_longest(range(10), data))
print(daily_data)

#repeat

counter = itertools.repeat(2, times = 5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
# print(next(counter)) #raise stopiteration after # of times
# print(next(counter))


squares = map(pow, range(10), itertools.repeat(3))
print("squares: ", list(squares))

#combinators

l = ["a", "b", "c", "d"]

results = itertools.combinations(l, 2)
print("result: ", list(results))

results = itertools.permutations(l, 2)
print("result: ", list(results))

l = [1,2,3,1]
results = itertools.permutations(l, 2)
print("result: ", len(list(results)))

l = [1,2,3,1,2]
results = itertools.permutations(l, 2)
print("result: ", len(list(results)))

l = [1,2,3,1,2]
results = itertools.product(l, repeat= 3)
print("product result: ", len(list(results)), " : ", list(results))
print(list(results))

l = [1,2,3,1,2]
results = itertools.product(l, repeat= 4)
for item in results:
    print(item)


#chain

l = [1,2,3,1,2]
a = ['a', 'e', 'r']
c = ("bat", "apple")
results = itertools.chain(l, a,c)
for item in results:
    print(item)

#isislice -->

result = itertools.islice(range(10), 1,8,2)
#print("slicing through itertools :", list(result))
for item in result:
    print(item)

print("****************",)
print("compress: ")
#compress --> similar to filter function
selectors = [True, True, True, False, True]
result = itertools.compress(l, selectors)
for item in result:
    print(item)

#takewhile, dropwhile, filterfalse, accumulate, mul --> import operator
#groupby
import operator
num = [1,2,3,2,1,5]

result = itertools.accumulate(num)
print(list(result))

result = itertools.accumulate(num, operator.mul)
print("oprator.mul: ")
for item in result:
    print(item)



<<<<<<< HEAD
import heapq


grades=[32,45,64,34,66,76,45,86]

print(heapq.nlargest(3,grades))

stocks=[
    {'ticker': 'AAPL', 'price':201},
    {'ticker': 'GOOG', 'price':800},
    {'ticker': 'FB', 'price':82},
    {'ticker': 'GAGA', 'price':120}
]

=======
import heapq


grades=[32,45,64,34,66,76,45,86]

print(heapq.nlargest(3,grades))

stocks=[
    {'ticker': 'AAPL', 'price':201},
    {'ticker': 'GOOG', 'price':800},
    {'ticker': 'FB', 'price':82},
    {'ticker': 'GAGA', 'price':120}
]

>>>>>>> c3a581a6142b4afe5141cc94fd60406c12aa70fe
print(heapq.nsmallest(2,stocks,key=lambda stock:stock['price']))
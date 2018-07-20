import heapq


grades=[32,45,64,34,66,76,45,86]

print(heapq.nlargest(3,grades))

stocks=[
    {'ticker': 'AAPL', 'price':201},
    {'ticker': 'GOOG', 'price':800},
    {'ticker': 'FB', 'price':82},
    {'ticker': 'GAGA', 'price':120}
]

print(heapq.nsmallest(2,stocks,key=lambda stock:stock['price']))
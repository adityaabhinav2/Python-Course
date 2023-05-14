'''  BINARY SEARCH
Def : Binary Search is defined as a searching algorithm used in a sorted array by repeatedly dividing
      the search interval in half.
Pros: -> Binary search is faster than linear search, especially for large arrays.
      -> Binary search is more efficient than other searching algorithms that have a similar time
         complexity, such as interpolation search or exponential search.
      -> the time complexity reduced to O(log N).
      -> Binary search is relatively simple to implement and easy to understand
Drawbacks: -> We require the array to be sorted. If the array is not sorted, we must first sort it before
              performing the search. This adds an additional O(N * logN) time complexity for the sorting step,
              which makes it irrelevant to use binary search.
           -> Binary search requires that the elements of the array be comparable, meaning that they must be
              able to be ordered. This can be a problem if the elements of the array are not naturally ordered,
              or if the ordering is not well-defined.'''

def binarsearch(n,l,r,f):
    # loop runs until the condition satisfied i.e,,(l<=r)
    while l <= r:
        # getting mid index value of an array
        mid = (l + r)//2
        # condition 1 : if element found at mid index then return mid
        if n[mid] == f:
            return mid
        # condition 2: if element is less than the mid element then set l to mid+1
        elif n[mid] < f:
            l = mid + 1
        # condition 3: if element is greater than the mid element then set r to mid-1
        else:
            r = mid - 1
    # if element not found in list returns -1
    return -1

# array of elements
n=[70,16,32,14,13,71,102,66,49]
# to sort: for B.Search array should be in either ascending or descending order
for i in range(len(n)-1):
    for j in range(i+1,len(n)):
        if n[i]>=n[j]:
            n[i]=n[i]+n[j]
            n[j]=n[i]-n[j]
            n[i]=n[i]-n[j]
print(n)
# Element to be searched in
f=int(input())
# initial index of array
l=0
# length of an array
r=len(n)
# to call BS method
k=binarsearch(n,l,r-1,f)
if k!=-1:
    # if element found it returns the index value of that element
    print("element found at index:", k)
else:
    print("Element not found")


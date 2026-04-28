from collections import deque, defaultdict
from itertools import count
from typing import Optional

class TreeNode:
    def __init__ (self, val=0, left=None, right=None):
        self.val=val
        self.left=left
        self.right=right

def bt(values):
    if not values or [0] is None:
        return None
    root=TreeNode(values[0])
    queue=deque([root])
    i=1
    while queue and i<len(values):
        node = queue.popleft()
        if i<len(values) and values[i] is not None:
            node.left=TreeNode(values[i])
            queue.append(node.left)
        i+=1
        if i<len(values) and values[i] is not None:
            node.right=TreeNode(values[i])
            queue.append(node.right)
        i+=1
    return root

#TASK1
#TIME O(), SPACE O()
def twosum (nums, target):
    map={}
    for i, num in enumerate(nums):
        compl=target-num
        if compl in map:
            return [map[compl], i]
        map[num]=i
    return []

#TASK2
#TIME O(), SPACE O()
def nonrep(s: str):
    count={}
    for c in s:
        count[c]=count.get(c,0)+1
    for i in range(len(s)):
        if count[s[i]]==1:
            return i
    return -1

#TASK3
#TIME O(), SPACE O()
def isom(s, t):
    s_to_t={ }
    t_to_s={ }
    for cs, ct in zip(s,t):
        if cs in s_to_t:
            if s_to_t[cs]!=ct:
                return False
            else:
                if ct in t_to_s:
                    return False
                s_to_t[cs]=ct
                t_to_s[ct]=cs
        return True

#TASK4
# TIME O(), SPACE O()
def happy(n):
    seen=set()
    while n!=1:
        if n in seen:
            return False
        seen.add(n)
        n=sum(int(d)**2 for d in str(n))
    return True

#TASK5
# TIME O(), SPACE O()
def tree(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        level = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level.append(node.val)
            if node.left:  queue.append(node.left)
            if node.right: queue.append(node.right)
        result.append(level)
    return result
root = bt([3, 9, 20, None, None, 15, 7])



#TASK6
# TIME O(), SPACE O()
def maxdepth(root):
    if not root:
        return 0
    return 1 + max(maxdepth(root.left), maxdepth(root.right))
root=bt([3, 9, 20, None, None, 15, 7])


#TASK7
# TIME O(), SPACE O()
def sym(root):
    def mirror(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        return (left.val==right.val
                and mirror(left.left, right.right)
                and mirror(left.right, right.left))
    return mirror(root.left, root.right)
root=bt([1, 2, 2, None, 3, None, 3])


#TASK8
# TIME O(), SPACE O()
def length(root):
    smax=[0]
    def dfs(node, pval, length):
        if not node:
            return
        if node.val==pval+1:
            length = length + 1
        else:
            length=1
        smax[0]=max(smax[0], length)
        dfs(node.left, node.val, length)
        dfs(node.right, node.val, length)
    dfs(root, float('-inf'),0)
    return smax[0]
root=bt([1,None,3,2,4,None,None,None,5])


#TASK9
# TIME O(), SPACE O()
def obj(num):
    low, mid, high=0, 0, len(num)-1
    while mid<=high:
        if num[mid]==0:
            num[low], num[mid]=num[mid], num[low]
            low+=1
            mid+=1
        elif num[mid]==1:
            mid+=1
        else:
            num[mid], num[high]= num[high], num[mid]
            high-=1
num=[2,0,2,1,1,0]
obj(num)


#TASK10
# TIME O(), SPACE O()
def quick(nums, low=None, high=None):
    if low is None:
        low, high=0, len(nums)-1
    def part(lo, hi):
        pivot=nums[hi]
        i=lo-1
        for j in range(lo, hi):
            if nums[j]<=pivot:
                i+=1
                nums[i], nums[j]=nums[j], nums[i]
        nums[i+1], nums[hi]=nums[hi], nums[i+1]
        return i+1
    if low<high:
        pi=part(low, high)
        quick(nums, low, pi-1)
        quick(nums, pi+1, high)
nums=[23, 12, 56, 69, 293, 67]
quick(nums)


#TASK11
# TIME O(), SPACE O()
def merge(numbs):
    if len(numbs)<=1:
        return
    mid=len(numbs)//2
    left, right = numbs[:mid], numbs[mid:]
    merge(left)
    merge(right)
    i=j=k=0
    while i<len(left) and j<len(right):
        if left[i]<=right[j]:
            numbs[k]=left[i]
            i+=1
        else:
            numbs[k]=right[j]
            j+=1
        k+=1
    while i<len(left):
        numbs[k]=left[i]
        i+=1
        k+=1
    while j<len(right):
        numbs[k]=right[j]
        j+=1
        k+=1
numbs=[1, 678, 234, 90, 568, 56]
merge(numbs)


#TASK12
# TIME O(), SPACE O()
def heap(ns):
    n=len(ns)

    def heapify(arr, n, i):
        largest=i
        l, r =2*i +1, 2*i+2
        if l<n and arr[l]>arr[largest]:
            largest=l
        if r<n and arr[r]>arr[largest]:
            largest=r
        if largest!=i:
            arr[i], arr[largest]=arr[largest], arr[i]
            heapify(arr, n, largest)
    for i in range(n//2-1, -1, -1):
        heapify(ns, n, i)
    for i in range (n -1, 0, -1):
        ns[0], ns[i]=ns[i], ns[0]
        heapify(ns, i, 0)
ns=[45,21,89,45,78,23,10, 4]
heap(ns)


if __name__ == "__main__":
    print('1)', twosum([2, 7, 11, 15], 9))
    print('2)',nonrep("loveleetcode"))
    print('3)',isom('egg', 'add'))
    print('4)',happy(19))
    print('5)',tree(root))
    print('6)',maxdepth(root))
    print('7)',sym(root))
    print('8)',length(root))
    print('9)',num)
    print('10)',nums)
    print('11)', numbs)
    print('12)', ns)

'''
multiple choice:
You are developing a real-time multimedia application that requires precise timing for audio and video synchronization. which scheduling algorithm would best ensure the required timing precision?
Rate monotonic scheduling (RMS)
Earliest Deadline First (EDF) <-- this
Fixed Priority scheduling
Round Robin scheduling

Your cloud-based application requires efficient resource allocation to handle varying workloads, which resource allocation strategy would best optimize performance and cost in a cloud environment?
Static partitioning
Dynamic partitioning <-- this or
Fixed resource allocation 
Predictive scalling <-- this

Your web application relies heavily on caching to improve performance, Optimizing cache performance is critical to ensure fast response times. Which caching strategy would best improve cache hit rates and overall performance?
Least recently used (LRU) eviction policy <-- this
random eviction policy
most recently used (MRU) eviction policy
fist in first out (FIFO) eviction policy 

KMP algorithm
Knuth-Morris-Pratt algorithm

function taskScheduler(tasks, n):
    taskCount = len(tasks)
    taskMap = createMap(tasks)
    taskQueue = priorityQueue()
    for task in taskMap:
        taskQueue.push(taskMap[task])
    cycles = 0
    while taskQueue is not empty:
        temp = []
        for i from 0 to n:
            if taskQueue is not empty:
                temp.push(taskQueue.pop())
        for task in temp:
            if task - 1 > 0:
                taskQueue.push(task - 1)
        cycles += (taskQueue is empty) ? len(temp) : n + 1
    return cycles
    
Minimizing task completion time under a fixed inter-task interval constraint
Randomly deprioritizing tasks based on their start time
Scheduling tasks with a maximum gap constraint between similar tasks
Optimizing the frequency of task execution within a time-constrained environment
'''

import heapq
import statistics
from itertools import combinations
from typing import List
import bisect

# refer: https://www.fastprep.io
print("Tiktok practice questions from: https://www.fastprep.io")

print("\nQuestion 1")
def countGoodSubsegments(numServers, numDisconnectedPairs, disconnectedPairs):
    dp = [1] + [0] * (numServers - 1)
    connect = 1

    for i in range(1, len(dp)):
        dp[i] = dp[i - 1] + 1
        if [i - 1 + 1, i + 1] not in disconnectedPairs:
            dp[i] += connect
            connect += 1
        else:
            connect = 1    
    return dp[numServers - 1]

print("Test 1: ", countGoodSubsegments(numServers = 4, numDisconnectedPairs = 2, disconnectedPairs = [[1, 2], [2, 3]]) == 5)
print("Test 2: ", countGoodSubsegments(numServers = 3, numDisconnectedPairs = 0, disconnectedPairs = [0]) == 6)
print("Test 3: ", countGoodSubsegments(numServers = 4, numDisconnectedPairs = 1, disconnectedPairs = [[2, 3]]) == 6)
print("Test 4: ", countGoodSubsegments(numServers = 5, numDisconnectedPairs = 3, disconnectedPairs = [[1, 2], [3, 4], [4, 5]]) == 6)
print("Test 5: ", countGoodSubsegments(numServers = 6, numDisconnectedPairs = 4, disconnectedPairs = [[1, 2], [2, 3], [4, 5], [5, 6]]) == 7)
print("Test 6: ", countGoodSubsegments(numServers = 2, numDisconnectedPairs = 1, disconnectedPairs = [[1, 2]]) == 2)

print("\nQuestion 2")
def getMinimumCost(vouchersCount, prices):
    minn_prices = [-x for x in prices]
    heapq.heapify(minn_prices)
    
    for k in range(vouchersCount - 1, -1, -1):
        curr_price = -heapq.heappop(minn_prices)
        price = curr_price // 2
        heapq.heappush(minn_prices, -price)
    
    return -sum(minn_prices)

print("Test 1: ", getMinimumCost(vouchersCount=3, prices=[8, 2, 13]) == 9) 
print("Test 2: ", getMinimumCost(vouchersCount=5, prices=[10, 20, 30, 40]) == 37)
print("Test 3: ", getMinimumCost(vouchersCount=1, prices=[50, 1]) == 26) 
print("Test 4: ", getMinimumCost(vouchersCount=4, prices=[1, 2, 3]) == 1) # Expected output: 1
print("Test 5: ", getMinimumCost(vouchersCount=0, prices=[100, 200]) == 300)
print("Test 6: ", getMinimumCost(vouchersCount = 2, prices = [5, 5, 10]) == 12)



print("\nQuestion 3")
def balanceContentFrequency(content):
    if not content:
        return 0
    
    freq = [0] * 26
    for c in content:
        freq[ord(c) - ord("a")] += 1
        
    # use median
    non_zero = [x for x in freq if x != 0]
    non_zero.sort()
    median = statistics.median(non_zero)
    return sum([abs(x - median) for x in non_zero])
    
#     minn = float("inf")
#     for f in set(freq):
#         total = 0
#         for c_f in freq:
#             if c_f != 0:
#                 total += abs(f - c_f)
        
#         minn = min(minn, total)
        
#     return minn
    
print("Test 1: ", balanceContentFrequency("xzyzxa") == 2) 
print("Test 2: ", balanceContentFrequency("ababc") == 1) 
print("Test 3: ", balanceContentFrequency("aabbc") == 1) 
print("Test 4: ", balanceContentFrequency("aaabb") == 1) 
print("Test 5: ", balanceContentFrequency("abc") == 0) 
print("Test 6: ", balanceContentFrequency("zzz") == 0) 
print("Test 7: ", balanceContentFrequency("zzzzxx") == 2) 
print("Test 8: ", balanceContentFrequency("x") == 0) 
print("Test 9: ", balanceContentFrequency("aabb") == 0) 
print("Test 10: ", balanceContentFrequency("") == 0) 


print("\nQuestion 4")
# https://www.fastprep.io/problems/tiktok-can-distribute-credits
def canDistributeCredits(participants, credits):
    
    total_ways = 0
    total_credits = sum(credits)

    # Iterate over all possible combinations of boxes
    for r in range(1, len(credits) + 1):
        for combo in combinations(credits, r):
            if sum(combo) % participants == 0:
                total_ways += 1
    # print(total_ways)
    return total_ways 

#     sol = [0]
#     cache = set([])
#     def backtrack(s, p, participants):
#         total = sum(p)
#         if len(p) > 1 and total % participants == 0:
#             print(p)
#             each = total / participants
#             if each not in cache:
#                 print(each)
#                 sol[0] += 1
#                 cache.add(each)
                
#         if len(s) == 0:
#             return
        
#         for i in range(len(s)):
#             backtrack(s[i + 1:], p + [s[i]], participants)
#     backtrack(credits, [], participants)
    
#     return sol[0]

print("Test 1: ", canDistributeCredits(participants = 6, credits = [12, 18, 24, 36]) == 8) 
print("Test 2: ", canDistributeCredits(participants = 5, credits = [7, 3, 6]) == 1) 
   
print("\nQuestion 5") 
def trim(string):
    start = 0
    end = len(string) - 1
    while start <= end and string[start] == " ":
        start += 1
    while start <= end and string[end] == " ":
        end -= 1
        
    return string[start: end + 1]

string = "   test es  "
print("Test 1: ", trim(string) == string.strip()) 
string = "   test es"
print("Test 1: ", trim(string) == string.strip()) 
string = "test es   asd     "
print("Test 1: ", trim(string) == string.strip()) 

print("\nQuestion 6")
def countViralCombinations(video, engagementArray, k):
    # using sliding window
    # https://leetcode.com/problems/count-number-of-nice-subarrays/solutions/419378/java-c-python-sliding-window-o-1-space/
    
    i = res = 0
    count = 0
    for j in range(len(video)):
        weak = abs(1 - engagementArray[ord(video[j]) - ord("a")])
        k -= abs(1 - engagementArray[ord(video[j]) - ord("a")])
        if k == 0:
            while k == 0:
                k += abs(1 - engagementArray[ord(video[i]) - ord("a")])
                i += 1                    
        no_sub = j - i + 1
        res += no_sub
        
    return res

print("Test 1: ", countViralCombinations(video = "abc", engagementArray = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], k = 2) == 5 )
print("Test 2: ", countViralCombinations(video = "abcd", engagementArray = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], k = 2) == 8 )
print("Test 3: ", countViralCombinations(video = "abc", engagementArray = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], k = 3) == 6 )
print("Test 4: ", countViralCombinations(video = "abcd", engagementArray = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], k = 3) == 10 )
print("Test 5: ", countViralCombinations(video = "abcde", engagementArray = [0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], k = 2) == 10 )


    
print("\nQuestion 7")
def optimizeTikTokWatchTime( n, initialWatch, repeatWatch, m):
    # use dp to track this
    
    # dp = [0] + [0] * m
    
    # base case
    # when m == 0, we don't have to watch anything, hence we spend 0 minutes
    # dp[0] = 0
    
    # when m == 1, we have to watch the first video, with the first view cost
    # dp[1] = initialWatch[0] + repeatWatch[0]
    
    # when m >= 2,
    # for example when m == 2, we can choose to move to the second video
    # OR stay at the first video and rewatch it.
    # for cases such as [1, 3, ...], [2, 3, ...] where stay at first will cost (1+ 2) + 2 = 5
    # and moving to the second video cost (1 + 2) + (3 + 3) = 9
    
    # for example when m == 3, we can choose to move to the second video
    # OR stay at the first video and rewatch it OR watch second video and stay at second OR watch third and stay at third
    # for cases such as [1, 3, ...], [2, 3, ...] where stay at first will cost (1+ 2) + 2 = 5
    # and moving to the second video cost (1 + 2) + (3 + 3) = 9
    
#     def recursive(n, m):
#         # n is the number of reels
#         if m <= 0: # <-- base case 0
#             return 0
#         if m == 1: # <-- base case 1
#             return initialWatch[0] + repeatWatch[0]
        
#         minn = float("inf")
        
#         for i in range(m): # <-- m >= 2
#             # i == 0, m == 2
    
    total_time = float("inf")
    no_reels = len(initialWatch)
    
    total_initial_watch = [initialWatch[i] + repeatWatch[i] for i in range(len(repeatWatch))]
    
    for i in range(no_reels):
        initial_watch = i + 1
        repeats = m - initial_watch
        
        initial_min = sum(total_initial_watch[:initial_watch])

        total_time = min(total_time, initial_min + (repeatWatch[i] * repeats))
    
    return total_time

print("Test 1: ", optimizeTikTokWatchTime(n = 4, initialWatch = [1, 5, 9, 11], repeatWatch = [2, 7, 10, 11], m = 4) == 9 )
print("Test 2: ", optimizeTikTokWatchTime(n = 2, initialWatch = [1, 3], repeatWatch = [2, 1], m = 2) == 5 )
# (1 + 2) + 2 + 2 + 2 = 11 vs (1 + 2) + (3 + 1) + 1 + 1 + 1 = 10
print("Test 3: ", optimizeTikTokWatchTime(n = 2, initialWatch = [1, 3], repeatWatch = [2, 1], m = 5) == 10 )
print("Test 4: ", optimizeTikTokWatchTime(n = 3, initialWatch = [2, 5, 3], repeatWatch = [2, 7, 1], m = 4) == 10 )
# 14 + 8 = 22 (+ 3 = 25) OR (+ 6 = 28)
print("Test 5: ", optimizeTikTokWatchTime(n = 3, initialWatch = [7, 5, 1], repeatWatch = [7, 3, 5], m = 3) == 25 )

    
print("\nQuestion 8")
# https://www.fastprep.io/problems/tiktok-stars-and-bars
def starsAndBars(s: str, startIndex: List[int], endIndex: List[int]) -> List[int]:  
    prefixSum, leftClosestBar, rightCloestBar= [], [], []
    count = 0
    leftClosest = -1
    rightClosest = len(s)
    for i, c in enumerate(s):
        if c == "*":
            count += 1
        if c == "|":
            leftClosest = i
        
        prefixSum.append(count)
        leftClosestBar.append(leftClosest)
        rightCloestBar.append(rightClosest)

    for i in range(len(s) -1, -1, -1):
        c = s[i]
        if c == "|":
            rightClosest = i
        rightCloestBar[i] = rightClosest
        
    # print(prefixSum)
    # print(leftClosestBar)
    # print(rightCloestBar)
    
    res = []
    for i in range(len(startIndex)):
        startIdx = startIndex[i] - 1
        start = rightCloestBar[startIdx]
        # print(f"right most of start is {startIdx}, {start}")
        
        endIdx = endIndex[i] - 1
        end = leftClosestBar[endIdx]        
        # print(f"left most of end is {endIdx}, {end}")
        
        
        if not(-1 < start < len(s) and -1 < end < len(s)):
            res.append(0)
        else:
            # print(f"prefix Sum for start at {start} is {prefixSum[start]}")
            # print(f"prefix Sum for end at {end} is {prefixSum[end]}")
            stars = prefixSum[end] - prefixSum[start]
            res.append(max(0, stars))
    # print(res)
    return res

print("Test 1: ", starsAndBars("|**|*|*", [1,1], [5,6]) == [2, 3])
print("Test 2: ", starsAndBars("|*|*|", [1], [3]) == [1]) # I feel like the answer should be 1 here
print("Test 3: ", starsAndBars("**||***|*|*|", [1,1,7,3], [9,2,10,4]) == [3,0,1,0])
print("Test 4: ", starsAndBars("**|*|***", [1,3,5], [3,5,8]) == [0,1,0])
print("Test 5: ", starsAndBars("|*****|", [1,1,5], [5,7,6]) == [0,5,0])


print("\nQuestion 9")
# Cant find on LeetCode or anywhere, closest reference is
# https://www.quora.com/In-how-many-ways-can-you-fit-1-X-1-X-2-sized-dominoes-into-a-domino-of-dimensions-2-X-2-X-N-where-N-is-a-variable
def dominosTiling3D(n: int) -> int:    
    # base case n = 1 has 2, || and =
    # when n = 2, you can start to stack it vertically. has 9
    # when n = 3, = f(n - 1) * 2 (with || and =) + f(n - 2)(9 - 2) + f(n-3) + ... + f(1)

    # return -1
    
    # from Quora
    dp = [1, 2, 9] + [0] * n
    for i in range(3, n + 1):
        # both equation below works
        # dp[i] = 4 * dp[i - 1] - dp[i - 2] + 2 * ((-1) ** i)
        dp[i] = 3 * dp[i - 1] + 3 * dp[i - 2] - dp[i - 3] # for this to work, dp[0] = 1
    # print(dp)
    return dp[n]
        

answer = [0, 2, 9, 32, 121, 450, 1681, 6272, 23409, 87362, 326041, 1216800, 4541161, 16947842, 63250209, 236052992, 880961761]
for i in range(len(answer)):
    print(f"Test {i + 1}: ", dominosTiling3D(i) == answer[i])
    

print("\nQuestion 10")
def threeConsecutiveGreater(nums: List[int], threshold: int) -> int:
    count = 0
    idx = 0
    for i, n in enumerate(nums):
        if n > threshold:
            count += 1
        else:
            count = 0
            idx = i + 1
        if count == 3:
            return idx
    return -1

print(f"Test 1: {threeConsecutiveGreater([0, 1, 4, 3, 2, 5], 1) == 2}")
print(f"Test 2: {threeConsecutiveGreater([-9, 95, 94, 4, 51], 42) == -1}")
print(f"Test 3: {threeConsecutiveGreater([-9, 95, 94, 4, 51], 4) == -1}")
print(f"Test 4: {threeConsecutiveGreater([-9, 1, 5, 4, 51], 3) == 2}")
print(f"Test 4: {threeConsecutiveGreater([-9, 1, 5, 4, 51], 0) == 1}")
print(f"Test 5: {threeConsecutiveGreater([-9,10, 5, 4, 51], -30) == 0}")
print(f"Test 6: {threeConsecutiveGreater([-9,10, 2, 4, 51], 3) == -1}")
    
print("\nQuestion 11")
def reChargeBattery(t: int, capacity: List[int], recharge: List[int]) -> int:
    # # how many batteries?
    # numb = len(capacity)
    # # make cumulative sum of battery runtimes
    # runtimes = [sum(capacity[:i+1]) for i in range(numb)]
    # total_runtime = runtimes[numb-1]
    # # figure out how many batteries we need
    # batts = t // total_runtime * numb
    # t = t % total_runtime
    # if t > 0:
    #     batts += bisect.bisect_left(runtimes, t) + 1
    #     # or
    #     # batts += np.searchsorted(runtimes, x) + 1
    #     # or
    #     # batts += next(idx + 1 for idx, value in enumerate(runtimes) if value >= x)
    # # check if any battery we use has a charge time greater than the total runtime of the other batteries
    # excess_charge_times = [total_runtime - runtime - recharge[idx] for idx, runtime in enumerate(recharge)]
    # # if a battery has to be used more than once and doesn't have enough charge time, fail
    # if any(batts > idx + numb and excess_charge_times[idx] < 0 for idx in range(numb)):
    #     return -1
    # return batts

    # Return the number of full batteries used during the t minutes you need to use your phone. 
    # If it is impossible have the phone working during the t minutes you need to use your phone. 
    # If it is impossible have the phone working during the entire duration of t minutes, 
    # i.e. if at some point all batteries are recharging and unavailable, return -1

    battery_ready = [0] * len(capacity)
    has_battery = 0 
    timestamp = 0
    c = 0
    res = 0

    while timestamp < t and has_battery <= timestamp:
        # print(f"timestamp = {timestamp}")
        # print(f"ready bat = {has_battery}")
        # print(f"list of b ={battery_ready}")
        used = False
        for _ in range(len(capacity)):
            # iterate in order, if this battery is ready, use it, else go to next
            if battery_ready[c] <= timestamp:
                timestamp += capacity[c]
                battery_ready[c] = timestamp + recharge[c]
                used = True
                res += 1
            c += 1
            if c == len(capacity):
                c = 0
            if used:
                break

        has_battery = min(battery_ready)

    # print(f"timestamp = {timestamp}")
    # print(f"ready bat = {has_battery}")
    # print(f"list of b = {battery_ready}")
    # print(f"total used: {res}")

    res = res if t == timestamp else res -1
    if t > timestamp:
        res = -1
    print(f"total fully used: {res}")
    return res

    # below is wrong
    # numb = len(capacity)
    # count = 0
    # now = 0
    # ready = [0, 0, 0, 0]
    # while now < t:
    #     batt = count % numb
    #     if ready[batt] > now:
    #         return -1
    #     now += capacity[batt]
    #     ready[batt] = now + recharge[batt]
    #     count += 1
    # return count

print(f"Test 1 (from stack overflow, not accurate): {reChargeBattery(16, [12, 3, 5, 18], [8, 1, 4, 9]) == 3}")
print(f"Test 2 (from stack overflow, not accurate): {reChargeBattery(46, [12, 3, 5, 8], [13, 14, 40, 20]) == 5}")
print(f"Test 3 (from stack overflow, not accurate): {reChargeBattery(20, [12, 3, 2], [6, 1, 1]) == -1}")
print(f"Test 4 (from TT): {reChargeBattery(16, [2, 5, 6], [12, 1, 4]) == 3}")
# [2, 5, 6]
# [12, 1, 4]
# [14,19,17]    
# t = 16
# t = 0 -> 2 -> 7 ->  13 -> skip(0) to (1), t = 18(not fully depleted)
# hence only fully used 3

    
    
    
    
    
    

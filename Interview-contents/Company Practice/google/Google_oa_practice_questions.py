# refer: https://www.fastprep.io
print("Google practice questions from: https://www.fastprep.io")

print("\nQuestion 1")
def moveBitsToRight(string):
    ones = 0
    double_count = True
    sol = 0
    
    for i, s in enumerate(string):
        if s == "1":
            ones += 1
            double_count = True
        if s == "0":
            if double_count:
                sol += (ones * 2)
            else:
                sol += ones
            double_count = False
    
    return sol

print("Test 1: ", moveBitsToRight("110100") == 13)
print("Test 2: ", moveBitsToRight("0101010") == 12)

print("\nQuestion 2")
def movesToObtain(arr):
    prev_max = -1
    prev_elem = -1
    sol = 0
    
    dp = [0] * len(arr)
    
    for i, current in enumerate(arr):
        if i == 0:
            dp[i] = arr[i]
        else:
            if current <= arr[i - 1]:
                dp[i] = dp[i - 1]
            else:
                dp[i] = dp[i - 1] + (current - arr[i - 1])
    return dp[-1]

print("Test 1: ", movesToObtain([2, 1, 3]) == 4)
print("Test 2: ", movesToObtain([2, 2, 0, 0, 1]) == 3)
print("Test 3: ", movesToObtain([5, 4, 2, 4, 1]) == 7)
print("Test 4: ", movesToObtain([1,2,3,2,1,2,3,2,1,2,3,2,1]) == 7)

print("\nQuestion 3")
def combine3Digits(arr):
    return int(str(arr[0]) + str(arr[1]) + str(arr[2]))

def biggestNumberFromDigits(arr):
    maxx = [0]
    
    # O(n) approach
    first = max(arr[:-2])
    first_index = arr.index(first)
    second_arr = arr[first_index + 1:]
    second = max(second_arr[:-1])
    second_index = second_arr.index(second)
    third = max(second_arr[second_index + 1:])
    return combine3Digits([first, second, third])
    
    # below uses backtracking
    # def backtrack(search_space, path):
    #     if len(path) == 3:
    #         maxx[0] = max(maxx[0], combine3Digits(path))
    #         return
    #     for i in range(len(search_space)):
    #         backtrack(search_space[i+ 1:], path + [search_space[i]])
    # backtrack(arr, [])
    
    return maxx[0]
    
print("Test 1: ", biggestNumberFromDigits([7, 2, 3, 3, 4, 9]) == 749)
print("Test 2: ", biggestNumberFromDigits([0, 0, 5, 7]) == 57)
print("Test 3: ", biggestNumberFromDigits([2, 1, 3]) == 213)
print("Test 4: ", biggestNumberFromDigits([2, 2, 0, 0, 1]) == 221)
print("Test 5: ", biggestNumberFromDigits([2, 2, 7, 0, 1]) == 701)


print("\nQuestion 4")
def performOperation(arr, i):
    arr[i], arr[i - 1] = arr[i - 1], arr[i]

def optimizeLogFile(arr):
    operations = [i for i in range(len(arr))][1:]
    
    while sum(operations) != -len(operations):
        smallest = float("inf")
        smallest_idx = -1
        opr_idx = -1
        for i, opr in enumerate(operations):
            if opr == -1:
                continue
            if arr[opr] < smallest:
                smallest = arr[opr]
                smallest_idx = opr
                opr_idx = i
        
        performOperation(arr, smallest_idx)
        operations[opr_idx] = -1
    
    return arr

print("Test 1: ", optimizeLogFile([5, 4, 1, 3, 2]) == [1, 5, 2, 4, 3])
print("Test 2: ", optimizeLogFile([4, 3, 2, 1]) == [1, 4, 3, 2] )


print("\nQuestion 5")

def numberOfMovesWithSameResults(nums):
    score_1 = nums[0] + nums[1]
    score_2 = nums[-1] + nums[-2]
    score_3 = nums[0] + nums[-1]

    # use @cache to turn your recursive into memoization
    # @cache
    cache = {}
    def recursive(arr, t, curr_score):
        arr = tuple(arr)
        if len(arr) < 2:
            return 0
        
        if (arr, t) in cache:
            return cache[(arr, t)]

        score_1 = arr[0] + arr[1]
        score_2 = arr[-1] + arr[-2]
        score_3 = arr[0] + arr[-1]

        return_score = curr_score
        if score_1 == t:
            return_score =  max(return_score, 1 + recursive(arr[2:], t, curr_score))
        if score_2 == t:
            return_score =  max(return_score,  1 + recursive(arr[:-2], t, curr_score))
        if score_3 == t:
            return_score =  max(return_score,  1 + recursive(arr[1:-1], t, curr_score))
            
        cache[(arr, t)] = return_score
        return return_score

    nums = tuple(nums)
    return max(recursive(nums, score_1, 0), recursive(nums, score_2, 0), recursive(nums, score_3, 0))

print("Test 1: ", numberOfMovesWithSameResults([3, 1, 5, 3, 3, 4, 2]) == 3)
print("Test 2: ", numberOfMovesWithSameResults([4, 1, 4, 3, 3, 2, 5, 2]) == 4 )
print("Test 3: ", numberOfMovesWithSameResults([1, 9, 1, 1, 1, 1,1,1, 8, 1]) == 1 )
print("Test 4: ", numberOfMovesWithSameResults([1, 9, 8, 9, 5, 1, 2]) == 3 )
print("Test 5: ", numberOfMovesWithSameResults([1, 1, 2, 3, 1, 2, 2, 1, 1, 2]) == 4)






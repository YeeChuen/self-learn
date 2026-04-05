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


print("\nQuestion 5")

def largestChosenDigitGroup(nums):
    # An array consists of N two-digit numbers. A group of numbers can be chosen from the array only if all of them share at least one digit. For example, numbers 52, 25, 55 can be chosen together (they share digit 5), but 11, 52, 34 cannot. What is the maximum number of array elements that can be chosen together?

    groups = [0] * 10

    for n in nums:
        sec_digit = n % 10
        fir_digit = (n - sec_digit) // 10

        # print(fir_digit, sec_digit)

        groups[fir_digit] += 1
        if fir_digit != sec_digit:
            groups[sec_digit] += 1

    return max(groups)

print("Test 1: ", largestChosenDigitGroup([52,25,11,52,34,55]) == 4)
print("Test 2: ", largestChosenDigitGroup([71,23,57,15]) == 2 )
print("Test 3: ", largestChosenDigitGroup([11,33,55]) == 1 )
print("Test 4: ", largestChosenDigitGroup([90,90,90]) == 3 )
print("Test 5: ", largestChosenDigitGroup([12,21,13,31,14]) == 4)
# digit 1 connects 12,21,13,31,14 → all share '1'
print("Test 6: ", largestChosenDigitGroup([10,20,30,40]) == 4)
# all share digit '0'
print("Test 7: ", largestChosenDigitGroup([12,34,56,78]) == 1)
# no shared digits → only 1 can be chosen
print("Test 8: ", largestChosenDigitGroup([11,12,13,14,15]) == 5)
# all share digit '1'
print("Test 9: ", largestChosenDigitGroup([22,23,24,25,26,27]) == 6)
# all share digit '2'
print("Test 10: ", largestChosenDigitGroup([98,89,78,87,68]) == 5)
# all connected via digit graph (8 and 9 and 7 and 6 chain)
print("Test 11: ", largestChosenDigitGroup([12,23,34,45,56,67,78,89]) == 8)
# chain connectivity across digits
print("Test 12: ", largestChosenDigitGroup([11,22,33,44,55,66]) == 1)
# no shared digits between numbers
print("Test 13: ", largestChosenDigitGroup([19,91,29,92,39,93]) == 6)
# all connected via digit 9
print("Test 14: ", largestChosenDigitGroup([10,11,12,13,20,21,22]) == 7)
# all connected via digits 1 and 2 through overlap
print("Test 15: ", largestChosenDigitGroup([44,44,44,45,54]) == 5)
# duplicates + shared digit '4'
print("Test 16: ", largestChosenDigitGroup([12,24,46,68,80]) == 5)
# chain via even digits
print("Test 17: ", largestChosenDigitGroup([11,22,12,21,33]) == 4)
# group formed by 1 and 2, excludes 33
print("Test 18: ", largestChosenDigitGroup([70,17,71,27,72]) == 5)
# all connected via digit 7
print("Test 19: ", largestChosenDigitGroup([10,23,45,67,89]) == 1)
# no overlaps
print("Test 20: ", largestChosenDigitGroup([55,56,65,66,67,76]) == 6)
# strong connectivity via digits 5,6,7
print("Test 21: ", largestChosenDigitGroup([12, 23, 34, 45, 56]) == 2)    # Chains don't count; must share one common digit
print("Test 22: ", largestChosenDigitGroup([22, 22, 12, 42]) == 4)        # All share digit 2
print("Test 23: ", largestChosenDigitGroup([10, 20, 30, 40, 50]) == 5)    # All share digit 0



print("\nQuestion 6")
# There is a single-player board game with N positions described by a string. Each position can be empty (denoted by "."), contain a player's token (denoted by "T") or contain a coin (denoted by "C"). The player may possess multiple tokens. A coin is collected by the player when a token is put on the coin's position (each coin can be collected only once).

# In one turn, the player can move a token by exactly three positions to the right (the token does not stop on the positions in between). Every token can be moved multiple times. The token cannot be moved if there is already another token in the position it would move onto. 

# What is the maximum number of coins the player can collect?
def maxNumberOfCoinsCanCollect(s):
    res = 0
    visited = set([])
    for i, c in enumerate(s):
        if c == "T":
            j = i + 3
            while j < len(s) and s[j] != "T":
                if s[j] == "C" and j not in visited:
                    # print("add", i,j)
                    res += 1
                    visited.add(j)
                j += 3 

    return res

print("Test 1: ", maxNumberOfCoinsCanCollect("TT.T.CCCCC") == 3)
print("Test 2: ", maxNumberOfCoinsCanCollect("T...CCCC") == 1)
print("Test 3: ", maxNumberOfCoinsCanCollect("C..TT.CT.C") == 2)
print("Test 4: ", maxNumberOfCoinsCanCollect("T.C...C") == 1)       # Move T from pos 0 -> 3 (collect c), then 3 -> 6 (collect c)
print("Test 5: ", maxNumberOfCoinsCanCollect("T..C..T..C") == 2)     # Both tokens move right once to hit a coin
print("Test 6: ", maxNumberOfCoinsCanCollect("T.CC..") == 1)      # T can hit index 2 or 5; only one coin is at index 2
print("Test 7: ", maxNumberOfCoinsCanCollect("T.CT..") == 0)      # T at pos 0 is blocked by T at pos 3
print("Test 8: ", maxNumberOfCoinsCanCollect("...C...") == 0)     # No tokens to move
print("Test 9: ", maxNumberOfCoinsCanCollect("T..C..C..C..C") == 4)   # T at pos 0 can hit pos 3, 6, 9...
print("Test 9.5: ", maxNumberOfCoinsCanCollect("T.C..C..C..C") == 0)   # T at pos 0 can hit pos 3, 6, 9...
print("Test 10: ", maxNumberOfCoinsCanCollect("TTT...") == 0)      # Tokens exist but no coins in their paths (pos +3, +6, etc.)

print("\n min_amplitude")
def min_amplitude(A):
    # Given an Array A, find the minimum amplitude you can get after changing up to 3 elements. 
    # Amplitude is the range of the array (basically difference between largest and smallest element).
    # TODO: Implement the logic to find the minimum amplitude after 3 changes.

    
    A.sort()
    if len(A) <= 3:
        return 0
    res = float("inf")
    # print(A)
    for i in range(4):
        startJ = len(A) - 4 + i
        for j in range(startJ, len(A)):
            # print(A[i], A[j])
            res = min(res, abs(A[i] - A[j]))


    return res

print("Test 1: ", min_amplitude([-1, 3, -1, 8, 5, 4]) == 2)
print("Test 2: ", min_amplitude([10, 10, 3, 4, 10]) == 0)
print("Test 3: ", min_amplitude([1, 5, 10, 20]) == 0)
print("Test 4: ", min_amplitude([1, 1, 1, 1, 10, 20, 30, 40]) == 9)
print("Test 5: ", min_amplitude([6, 6, 0, 1, 1, 4, 6]) == 2)

print("\n count_equal_unique_splits")
def count_equal_unique_splits(S):
    # Given a string S, we can split S into 2 strings: S1 and S2. 
    # Return the number of ways S can be split such that the number of 
    # unique characters between S1 and S2 are the same.
    # TODO: Implement the logic to count valid split points.
    counter = 0
    for i in range(1, len(S)):
        if len(set(S[:i])) == len(set(S[i:])):
            counter += 1
        # print(S[:i], S[i:])
    return counter

print("Test 1: ", count_equal_unique_splits("aaaa") == 3)
print("Test 2: ", count_equal_unique_splits("bac") == 0)
print("Test 3: ", count_equal_unique_splits("ababa") == 2)
print("Test 4: ", count_equal_unique_splits("abcde") == 0)
print("Test 5: ", count_equal_unique_splits("aabb") == 1)
print("Test 6: ", count_equal_unique_splits("aba") == 0)

print("\n max_equal_sum_moves")
def max_equal_sum_moves(A):
    # You are given an array A consisting of N numbers. In one move you can delete 
    # either the first two, the last two, or the first and last elements of A. 
    # Returns the maximum number of moves that can be performed such that 
    # all performed moves have the same result (sum).
    # TODO: Implement the recursive/DP logic to find the max moves for a target sum.

    def backtracking(l, r, target):
        # base case if l + 1 <= r or else we're looking at the same number of we have overlapped
        if not l + 1 <= r or not 0 <= l < len(A) or not 0 <= r < len(A):
            return 0
        
        # print(l,r)

        firsttwo = A[l] + A[l + 1]
        lasttwo = A[r - 1] + A[r]
        bothends = A[l] + A[r]

        nextft = 0
        if firsttwo == target:
            nextft = 1 + backtracking(l + 2, r, target)
        nextlt = 0
        if lasttwo == target:
            nextlt = 1 + backtracking(l, r - 2, target)
        nextbe = 0
        if bothends == target:
            # print(l, r, target, " --- ", firsttwo, lasttwo, bothends)
            nextbe = 1 + backtracking(l + 1, r - 1, target)
        return max(nextft, nextlt, nextbe)

    n = len(A)
    o1 = 1 + backtracking(2, n - 1, A[0] + A[1])
    o2 = 1 + backtracking(0, n - 3, A[-1] + A[-2])
    o3 = 1 + backtracking(1, n - 2, A[0] + A[-1])
    
    # print(o1, o2, o3)


    return max(o1, o2, o3)

print("Test 1: ", max_equal_sum_moves([3, 1, 5, 3, 3, 4, 2]) == 3)
print("Test 2: ", max_equal_sum_moves([4, 1, 4, 3, 3, 2, 5, 2]) == 4)
print("Test 3: ", max_equal_sum_moves([1, 9, 1, 1, 1, 1, 1, 1, 8, 1]) == 1)
print("Test 4: ", max_equal_sum_moves([1, 9, 8, 9, 5, 1, 2]) == 3)
print("Test 5: ", max_equal_sum_moves([1, 1, 2, 3, 1, 2, 2, 1, 1, 2]) == 4)
print("Test 6: ", max_equal_sum_moves([10, 10]) == 1)
print("Test 7: ", max_equal_sum_moves([1, 2, 3, 4]) == 2)

print("\n min_tree_groups_max_sum")
def min_tree_groups_max_sum(n, A, edges):
    # You are given an undirected tree with N nodes. 
    # Divide the nodes into as few groups as possible such that no two nodes 
    # in a group are adjacent (Bipartite coloring).
    # For each group, find the maximum sum possible by pairing nodes (u, v) 
    # and calculating |A[u] - A[v]|.
    # Return the sum of costs of all groups.
    # TODO: Implement bipartite partitioning and max-weight matching logic.

    # group them into bipartite
    color = {}
    # 0 no color, 1 red, 2 blue
    root = edges[0][0]
    q = [root]
    color[root] = 1
    while q:
        curr = q.pop(0)
        for e in edges:
            if curr not in e:
                continue

            neighbor = e[1] if e[0] == curr else e[0]
            expectedColor = 1 if color[curr] == 0 else 0
            # print(color)
            # print(curr, neighbor)
            # print(color[curr], expectedColor)
            if neighbor not in color:
                color[neighbor] = expectedColor
                q.append(neighbor)
            else:
                if expectedColor != color[neighbor]:
                    # print(color)
                    return -1

    # print(color)
    minn = {}
    # calculate the max value in each group
    for i in range(2):
        for node in color:
            for node2 in color:
                if color[node] == i and color[node2] == i and node != node2:
                    # print(node, node2)
                    # print(A[node - 1], A[node2 - 1])
                    if i not in minn:
                        minn[i] = float("-inf")
                    minn[i] = max(minn[i], abs(A[node - 1] - A[node2 - 1]))
                    # print(minn)

    res = 0
    # sum the max value from each group
    for k in minn:
        res += minn[k]

    return res

print("Test 1: ", min_tree_groups_max_sum(5, [12, 17, 14, 13, 16], [[1, 2], [1, 3], [1, 5], [2, 4]]) == 4)
print("Test 2: ", min_tree_groups_max_sum(4, [10, 20, 30, 40], [[1, 2], [2, 3], [3, 4]]) == 40)
print("Test 3: ", min_tree_groups_max_sum(2, [10, 100], [[1, 2]]) == 0)
print("Test 4: ", min_tree_groups_max_sum(6, [1, 2, 3, 4, 5, 6], [[1, 2], [1, 3], [1, 4], [1, 5], [1, 6]]) == 4)
print("Test 5: ", min_tree_groups_max_sum(3, [1, 2, 3], [[1, 2], [2, 3], [3, 1]]) == -1)

print("\n min_moves_to_target_array")
def min_moves_to_target_array(A):
    # Starting from a zero-filled array, find the minimum number of moves 
    # to obtain array A. In one move, you can choose an arbitrary interval 
    # and increase all elements within it by 1.
    # TODO: Implement the greedy logic to calculate the total moves.

    moves = 0
    # whole array subtract by the minimum. then split the array by zero. 
    def recursion(target):
        if not target or len(target) <= 0:
            return

        nonlocal moves

        minn = min(target)
        moves += minn

        for i in range(len(target)):
            target[i] -= minn

        # split here base on delimeter
        split_target = [[]]
        for n in target:
            if n == 0:
                split_target.append([])
            else:
                split_target[-1].append(n)
                
        for new_target in split_target:
            recursion(new_target)

    
    recursion(A)
    # print(A)
    # print(moves)


    return moves

print("Test 1: ", min_moves_to_target_array([2, 1, 3]) == 4)
print("Test 2: ", min_moves_to_target_array([2, 2, 0, 0, 1]) == 3)
print("Test 3: ", min_moves_to_target_array([5, 4, 2, 4, 1]) == 7)
print("Test 4: ", min_moves_to_target_array([0, 0, 0]) == 0)
print("Test 5: ", min_moves_to_target_array([10, 10, 10]) == 10)
print("Test 6: ", min_moves_to_target_array([1, 2, 3, 2, 1]) == 3)

print("\n count_steps_to_transform")
def count_steps_to_transform(array):
    # You are given an array, and the task is to determine how many steps 
    # it takes to transform an array of all zeros into the given array. 
    # In each step, you can add a contiguous sequence of 1's to the array.
    # TODO: Implement the logic to calculate the minimum number of steps.
    return min_moves_to_target_array(array)

print("Test 1: ", count_steps_to_transform([2, 1, 0, 2]) == 4)
print("Test 2: ", count_steps_to_transform([1, 1, 1, 1]) == 1)
print("Test 3: ", count_steps_to_transform([1, 0, 1, 0]) == 2)
print("Test 4: ", count_steps_to_transform([3, 2, 3]) == 4)
print("Test 5: ", count_steps_to_transform([0, 0, 0]) == 0)
print("Test 6: ", count_steps_to_transform([5]) == 5)

print("\n min_moves_for_range_increments")
def min_moves_for_range_increments(A):
    # Given an array of integers A, with each move you can select an arbitrary 
    # range and increment all the numbers in that range by 1. Return the 
    # minimum number of moves needed to transform an array starting with 
    # all zeros into A.
    # TODO: Implement the logic to calculate the minimum range increments.
    return min_moves_to_target_array(A)

print("Test 1: ", min_moves_for_range_increments([2, 1, 3]) == 4)
print("Test 2: ", min_moves_for_range_increments([5, 5, 5]) == 5)
print("Test 3: ", min_moves_for_range_increments([1, 2, 3, 2, 1]) == 3)
print("Test 4: ", min_moves_for_range_increments([0, 0, 0]) == 0)
print("Test 5: ", min_moves_for_range_increments([10, 0, 10]) == 20)
print("Test 6: ", min_moves_for_range_increments([3, 4, 1, 6, 2]) == 10)

print("\n googleBiggestNumberOfDigits")
def googleBiggestNumberOfDigits(digits):
    # Given an array of N digits, choose at most three digits (not necessarily adjacent) 
    # and merge them into a new integer without changing their relative order.
    # Return the biggest number that can be built.
    # TODO: Implement the logic to find the maximum possible integer from 1, 2, or 3 digits.
    
    digitsize = 3

    offset = 2 if len(digits) >= digitsize else len(digits) - 1
    # print(offset)

    # this is how many digits we want.
    result = [[0,-1]]
    for i in range(digitsize): # <-- we want 3 here
        loop_end = len(digits) - offset + i
        loop_start = result[-1][1] + 1
        # print(loop_start, loop_end)

        new_digit = [0,0]

        if loop_start >= 0 and loop_end <= len(digits):
            for j in range(loop_start, loop_end):
                if digits[j] > new_digit[0]:
                    new_digit = [digits[j], j]

            result.append(new_digit)
    
    # print(result)
    res = ""
    for r in result:
        res += str(r[0])
    # print(res)

    return int(res)

print("Test 1: ", googleBiggestNumberOfDigits([7, 2, 3, 3, 4, 9]) == 749)
print("Test 2: ", googleBiggestNumberOfDigits([0, 0, 5, 7]) == 57)
print("Test 3: ", googleBiggestNumberOfDigits([9, 1, 1, 1, 9]) == 919)
print("Test 4: ", googleBiggestNumberOfDigits([1, 2, 3]) == 123)
print("Test 5: ", googleBiggestNumberOfDigits([9, 0, 0, 0, 0]) == 900)
print("Test 6: ", googleBiggestNumberOfDigits([0, 0, 0, 0]) == 0)
print("Test 7(manual): ", googleBiggestNumberOfDigits([2, 3]) == 23)
print("Test 8(manual): ", googleBiggestNumberOfDigits([3]) == 3)
print("Test 9(manual): ", googleBiggestNumberOfDigits([]) == 0)

print("\n max_three_digit_number")
def max_three_digit_number(nums):
    # Given an array with a minimum length of 3, find a three-digit number 
    # made up of three elements from the array (preserving their original 
    # relative order), such that the resulting number is as large as possible.
    # TODO: Implement the logic to find the maximum possible three-digit integer.
    return googleBiggestNumberOfDigits(nums)

print("Test 1: ", max_three_digit_number([7, 4, 3, 8, 2]) == 782)
print("Test 2: ", max_three_digit_number([1, 2, 3, 4, 5]) == 345)
print("Test 3: ", max_three_digit_number([9, 0, 1, 9, 0]) == 990)
print("Test 4: ", max_three_digit_number([5, 5, 5]) == 555)
print("Test 5: ", max_three_digit_number([1, 9, 1, 8, 1, 7]) == 987)



print("\n get_largest_number")
def get_largest_number(digits):
    # Given an array of digits, select up to 3 digits to form a number 
    # without changing their order. Return the largest possible number.
    # TODO: Implement the logic to find the maximum possible number.
    return googleBiggestNumberOfDigits(digits)

print("Test 1: ", get_largest_number([7, 2, 3, 3, 4, 9]) == 749)
print("Test 2: ", get_largest_number([0, 0, 5, 7]) == 57)
print("Test 3: ", get_largest_number([9, 1, 9, 1]) == 991)
print("Test 4: ", get_largest_number([1, 2, 3, 4, 5]) == 345)
print("Test 5: ", get_largest_number([9, 0, 0, 9]) == 909)
print("Test 6: ", get_largest_number([8]) == 8)
print("Test 7: ", get_largest_number([5, 4, 3, 2, 1]) == 543)

print("\n min_transform_operations")
def min_transform_operations(str1, str2):
    # Given two strings of equal length made up of 'x', 'y', and 'z', 
    # with no consecutive characters the same, determine the minimum 
    # number of operations to transform the first string into the second. 
    # In one operation, you can change any character in the first string, 
    # ensuring no consecutive characters become identical.
    # TODO: Implement the logic to find the minimum operations for string transformation.
    return None

print("Test 1: ", min_transform_operations("zxyz", "zyxz") == 6)
print("Test 2: ", min_transform_operations("xzyzyzyzxyz", "xzyzyzyzyxy") == 15)
print("Test 3: ", min_transform_operations("xyyxyxyxyy", "xzyxyzyxzx") == 13)
print("Test 4: ", min_transform_operations("xyyxyzzyxy", "zyzyzyzyzyz") == 9)
print("Test 5: ", min_transform_operations("xzxyxyzzyxyz", "zyzyzyzyzyzy") == 20)
print("Test 6: ", min_transform_operations("xyz", "xyz") == 0)
print("Test 7: ", min_transform_operations("x", "y") == 1)

print("\n getMeetingIntervals")
def getMeetingIntervals(meetings, dns):
    # You have a list of meetings with start and end times that can overlap.
    # A "Do Not Schedule" (DNS) interval cuts any overlapping meeting time.
    # Return a list of non-overlapping time intervals when you are in a meeting.
    # TODO: Implement the logic to merge meetings and exclude the DNS slot.

    meetings.sort()
    # print(meetings)

    # combine meeting
    new_meeting = []
    for m in meetings:
        if not new_meeting or len(new_meeting) == 0:
            new_meeting.append(m)
            continue

        # if this is not in the same interval, start is > prev end
        if m[0] > new_meeting[-1][1]:
            new_meeting.append(m)
        else:
            # else, previous end intercept with current start, we need to merge them
            # we know curr start will always be >= previous start because we sorted it.
            # but we need to pick the largest end
            # this is in the same interval
            prev_end = new_meeting[-1][1]
            curr_end = m[1]
            new_meeting[-1][1] = max(prev_end, curr_end)

    print(new_meeting)
    meeting_with_dns = []

    # then split it base on dns
    while new_meeting:
        curr = new_meeting.pop(0)

        # if curr is fully within dns, we go to the next
        if curr[0] >= dns[0] and curr[1] <= dns[1]:
            continue
        # if dns is anywhere within curr, we can easily return here. because we only need to split current
        elif curr[0] <= dns[0] and curr[1] >= dns[1]:
            new = []
            if curr[0] < dns[0]:
                new.append([curr[0], dns[0]])
            if curr[1] > dns[1]:
                new.append([dns[1], curr[1]])
            final = meeting_with_dns + new + new_meeting
            print(final)
            return final
        elif curr[0] >= dns[1] and curr[1] <= dns[0]:
        # partial intersection
            meeting_with_dns.append(curr)

        else:
            # put if back if there is no itersaction
            print("partial intersaction")
    print(meeting_with_dns)
    return None

print("Test 1: ", getMeetingIntervals([[1, 7], [5, 10], [12, 30], [22, 30], [40, 50], [60, 70]], [18, 25]) == [[1, 10], [12, 18], [25, 30], [40, 50], [60, 70]])
print("Test 2: ", getMeetingIntervals([[1, 10]], [2, 5]) == [[1, 2], [5, 10]])
print("Test 3: ", getMeetingIntervals([[1, 5], [6, 10]], [11, 15]) == [[1, 5], [6, 10]])
print("Test 4: ", getMeetingIntervals([[1, 5]], [0, 10]) == [])
print("Test 5: ", getMeetingIntervals([[1, 5], [3, 7]], [4, 4]) == [[1, 7]])
print("Test 6: ", getMeetingIntervals([[10, 20], [15, 25]], [12, 18]) == [[10, 12], [18, 25]])
print("Test 7: ", getMeetingIntervals([[20,28],[20,23],[10, 20], [15, 25]], [12, 18]) == [[10, 12], [18, 28]])
print("Test 8(manual): ", getMeetingIntervals([[-1,0],[1,4],[5,8]], [2,3]) == [[1,2], [3,4]])
print("Test 9(manual): ", getMeetingIntervals([[1,4]], [1,3]) == [[3,4]])
print("Test 10(manual): ", getMeetingIntervals([[1,4]], [2,4]) == [[1,2]])

print("\nnumDistinctIslands")
def numDistinctIslands(grid):
    # In an ocean, there are islands marked by 1. Water is represented by 0. 
    # Determine how many unique shapes (no rotation or mirror) among these islands. 
    # Islands are connected 4-directionally.
    # TODO: Implement BFS/DFS with path encoding to identify unique shapes.
    return None

print("Test 1: ", numDistinctIslands([[1, 1, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1], [0, 0, 1, 1, 0, 1], [1, 1, 0, 0, 0, 0], [0, 0, 1, 1, 1, 1], [1, 0, 1, 1, 0, 0]]) == 4)
print("Test 2: ", numDistinctIslands([[1, 1, 0], [0, 1, 1], [0, 0, 0], [1, 1, 0], [0, 1, 1]]) == 1)
print("Test 3: ", numDistinctIslands([[1, 0], [0, 1]]) == 1)
print("Test 4: ", numDistinctIslands([[1, 1], [1, 0]]) == 1)
print("Test 5: ", numDistinctIslands([[0, 0, 0], [0, 0, 0]]) == 0)
print("Test 6: ", numDistinctIslands([[1, 1, 1], [0, 1, 0], [1, 1, 1]]) == 1)


print("\nfull_justify_text")
def full_justify_text(words, maxWidth):
    # Given an array of strings words and a width maxWidth, format the text such that 
    # each line has exactly maxWidth characters and is fully (left and right) justified.
    # Pack words greedily, distributing extra spaces as evenly as possible.
    # The last line and single-word lines should be left-justified.
    # TODO: Implement the greedy packing and space distribution logic.
    return None

print("Test 1: ", full_justify_text(["This", "is", "an", "example", "of", "text", "justification."], 16) == ["This    is    an", "example  of text", "justification.  "])
print("Test 2: ", full_justify_text(["What","must","be","acknowledgment","shall","be"], 16) == ["What   must   be", "acknowledgment  ", "shall be        "])
print("Test 3: ", full_justify_text(["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 20) == ["Science  is  what we", "understand     well", "enough to explain to", "a  computer. Art is", "everything else  we", "do                "])
print("Test 4: ", full_justify_text(["Hello", "World"], 10) == ["Hello     ", "World     "])
print("Test 5: ", full_justify_text(["Listen", "to", "many,", "speak", "to", "a", "few."], 6) == ["Listen", "to    ", "many, ", "speak ", "to a  ", "few.  "])

print("\nmin_splits_for_sorted_chunks")
def min_splits_for_sorted_chunks(nums):
    # You're optimizing video chunks for streaming. Each chunk has a size 
    # represented in a 0-indexed array nums. You can split any chunk into 
    # two smaller chunks whose sizes add up to the original.
    # Return the minimum number of split operations needed to make the 
    # array sorted in non-decreasing order.
    # TODO: Implement the O(n) greedy backward pass to calculate minimum splits.
    return None

print("Test 1: ", min_splits_for_sorted_chunks([10, 5, 8]) == 1)
print("Test 2: ", min_splits_for_sorted_chunks([3, 9, 3]) == 2)
print("Test 3: ", min_splits_for_sorted_chunks([1, 2, 3]) == 0)
print("Test 4: ", min_splits_for_sorted_chunks([10, 1]) == 9)
print("Test 5: ", min_splits_for_sorted_chunks([5, 10, 2]) == 4)
print("Test 6: ", min_splits_for_sorted_chunks([7, 7, 7]) == 0)

print("\nnearest_value_replacement")
def nearest_value_replacement(A, cur, D):
    # Given an array A, a starting index cur, and a distance D.
    # Iteratively update A[cur] by incrementing it, then jump to the nearest 
    # index (within distance D) where this new value exists.
    # If multiple exist at the same distance, choose the leftmost.
    # Stop if the new value is not found within distance D.
    # TODO: Implement the iterative search and jump logic.
    return None

print("Test 1: ", nearest_value_replacement([1, 3, 2, 3, 4, 5, 2], 2, 2) == [1, 3, 3, 3, 4, 5, 2])
print("Test 2: ", nearest_value_replacement([1, 1, 1], 1, 1) == [1, 2, 1])
print("Test 3: ", nearest_value_replacement([5, 5, 5, 5, 5], 0, 2) == [6, 5, 5, 5, 5])
print("Test 4: ", nearest_value_replacement([1, 2, 3, 4], 0, 3) == [2, 2, 3, 4])
print("Test 5: ", nearest_value_replacement([1, 2, 1, 2], 0, 2) == [2, 2, 2, 2])

print("\nget_all_next")
class ImageIterator:
    def __init__(self, allImages, markedFavorites):
        # Implement the getNext() function such that images from markedFavorites 
        # are returned first, followed by remaining images from allImages 
        # that are not in markedFavorites.
        # Order among both lists should be maintained. Return None if at the end.
        # TODO: Implement the iterator setup and tracking logic.
        self.allImages = allImages
        self.markedFavorites = markedFavorites
        pass

    def getNext(self):
        # TODO: Implement the logic to return the next image in the sequence.
        return None

# Helper function for testing purposes
def get_all_next(allImages, markedFavorites):
    iterator = ImageIterator(allImages, markedFavorites)
    result = []
    while True:
        img = iterator.getNext()
        if img is None:
            break
        result.append(img)
    return result

all_imgs = ["i1", "i2", "i3", "i4", "i5", "i6", "i7", "i8", "i9", "i10"]
favs = ["i2", "i5", "i7"]

print("Test 1: ", get_all_next(all_imgs, favs) == ["i2", "i5", "i7", "i1", "i3", "i4", "i6", "i8", "i9", "i10"])
print("Test 2: ", get_all_next(["a", "b", "c"], ["b"]) == ["b", "a", "c"])
print("Test 3: ", get_all_next(["x", "y"], ["x", "y"]) == ["x", "y"])
print("Test 4: ", get_all_next(["z"], []) == ["z"])
print("Test 5: ", get_all_next([], []) == [])


# def <ReadableFunctionName>(input):
#     # Question description here
#     return None

# print("Test 1: ", <ReadableFunctionName>(input) == 1)
# print("Test 2: ", <ReadableFunctionName>(input) == 2)
# print("Test n: ", <ReadableFunctionName>(input) == n)


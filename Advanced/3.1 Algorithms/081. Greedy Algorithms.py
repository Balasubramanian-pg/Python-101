from heapq import heappush, heappop
from collections import defaultdict

# -------------------------------
# 1. Activity Selection
# -------------------------------
def activity_selection(activities):
    """
    activities: list of (start, end)
    returns maximum number of non-overlapping activities
    """
    activities.sort(key=lambda x: x[1])
    result = []

    last_end = 0
    for start, end in activities:
        if start >= last_end:
            result.append((start, end))
            last_end = end

    return result


# -------------------------------
# 2. Fractional Knapsack
# -------------------------------
def fractional_knapsack(items, capacity):
    """
    items: list of (value, weight)
    capacity: max weight
    """
    items.sort(key=lambda x: x[0]/x[1], reverse=True)

    total_value = 0.0

    for value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            break

    return total_value


# -------------------------------
# 3. Huffman Coding
# -------------------------------
class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq


def huffman_encoding(freq_map):
    """
    freq_map: dict {char: frequency}
    returns: dict {char: binary_code}
    """
    heap = []

    for char, freq in freq_map.items():
        heappush(heap, HuffmanNode(char, freq))

    while len(heap) > 1:
        left = heappop(heap)
        right = heappop(heap)

        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heappush(heap, merged)

    root = heap[0]
    codes = {}

    def generate_codes(node, code):
        if node:
            if node.char is not None:
                codes[node.char] = code
            generate_codes(node.left, code + "0")
            generate_codes(node.right, code + "1")

    generate_codes(root, "")
    return codes


# -------------------------------
# 4. Minimum Coins (Greedy)
# -------------------------------
def min_coins(coins, amount):
    """
    coins: list of denominations
    amount: target amount
    """
    coins.sort(reverse=True)
    result = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    if amount != 0:
        return -1  # Not possible

    return result


# -------------------------------
# 5. Job Sequencing with Deadlines
# -------------------------------
def job_sequencing(jobs):
    """
    jobs: list of (id, deadline, profit)
    """
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [-1] * (max_deadline + 1)

    total_profit = 0
    scheduled_jobs = []

    for job_id, deadline, profit in jobs:
        for d in range(deadline, 0, -1):
            if slots[d] == -1:
                slots[d] = job_id
                total_profit += profit
                scheduled_jobs.append(job_id)
                break

    return scheduled_jobs, total_profit


# -------------------------------
# 6. Gas Station (Circular Tour)
# -------------------------------
def can_complete_circuit(gas, cost):
    """
    gas[i]: gas at station i
    cost[i]: cost to go to next station
    """
    total, tank = 0, 0
    start = 0

    for i in range(len(gas)):
        total += gas[i] - cost[i]
        tank += gas[i] - cost[i]

        if tank < 0:
            start = i + 1
            tank = 0

    return start if total >= 0 else -1


# -------------------------------
# 7. Minimum Platforms (Train Scheduling)
# -------------------------------
def min_platforms(arrival, departure):
    """
    arrival: list of arrival times
    departure: list of departure times
    """
    arrival.sort()
    departure.sort()

    i = j = 0
    platforms = max_platforms = 0

    while i < len(arrival) and j < len(departure):
        if arrival[i] <= departure[j]:
            platforms += 1
            max_platforms = max(max_platforms, platforms)
            i += 1
        else:
            platforms -= 1
            j += 1

    return max_platforms


# -------------------------------
# Example Usage
# -------------------------------
if __name__ == "__main__":
    activities = [(1, 3), (2, 5), (4, 7), (6, 9)]
    print("Activity Selection:", activity_selection(activities))

    items = [(60, 10), (100, 20), (120, 30)]
    print("Fractional Knapsack:", fractional_knapsack(items, 50))

    freq_map = {'a': 5, 'b': 9, 'c': 12, 'd': 13}
    print("Huffman Codes:", huffman_encoding(freq_map))

    coins = [1, 2, 5, 10]
    print("Min Coins:", min_coins(coins, 27))

    jobs = [
        ('J1', 2, 100),
        ('J2', 1, 50),
        ('J3', 2, 10),
        ('J4', 1, 20)
    ]
    print("Job Sequencing:", job_sequencing(jobs))

    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print("Gas Station Start:", can_complete_circuit(gas, cost))

    arrival = [900, 940, 950, 1100, 1500, 1800]
    departure = [910, 1200, 1120, 1130, 1900, 2000]
    print("Minimum Platforms:", min_platforms(arrival, departure))

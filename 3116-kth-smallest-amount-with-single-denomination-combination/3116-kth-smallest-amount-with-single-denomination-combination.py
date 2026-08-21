class Solution(object):

  def findKthSmallest(self, coins, k):
    """
    :type coins: List[int]
    :type k: int
    :rtype: int
    """

    def gcd(a, b):
      while b:
        a, b = b, a % b
      return a

    def lcm(a, b):
      return (a * b) // gcd(a, b)

    # Filter out coins that are multiples of another coin to reduce subset size
    coins = sorted(list(set(coins)))
    filtered_coins = []
    for i in range(len(coins)):
      if not any(coins[i] % c == 0 for c in filtered_coins):
        filtered_coins.append(coins[i])
    coins = filtered_coins

    n = len(coins)
    subsets = []

    # Precompute (lcm, sign) for all 2^n - 1 non-empty subsets using bitmasking
    for mask in range(1, 1 << n):
      current_lcm = 1
      size = 0
      for i in range(n):
        if (mask >> i) & 1:
          current_lcm = lcm(current_lcm, coins[i])
          size += 1

      sign = 1 if size % 2 == 1 else -1
      subsets.append((current_lcm, sign))

    def count(x):
      total = 0
      for sub_lcm, sign in subsets:
        total += sign * (x // sub_lcm)
      return total

    # Binary search for the kth value
    low = 1
    high = min(coins) * k
    ans = high

    while low <= high:
      mid = (low + high) // 2
      if count(mid) >= k:
        ans = mid
        high = mid - 1
      else:
        low = mid + 1

    return ans
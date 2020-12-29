def shortsell(n, k, prices_n):
    lot_prices = [price * 100 for price in prices_n]
    diff = [lot_prices[i] - lot_prices[i+1] for i in range(n-1)]  # We reduce the problem to a maximum subarray problem
    max_gain = gain = diff[0] - 2 * k

    for i in range(1, n-1):
        gain = max(diff[i] - 2 * k, gain + diff[i] - k)
        max_gain = max(max_gain, gain)

    return max(max_gain, 0)


N, K = map(int, input().split())
prices = list(map(int, input().split()))
print(shortsell(N, K, prices))

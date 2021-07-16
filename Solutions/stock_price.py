def solution(stock_prices: list) -> list:
    # Using Double Loop
    result_list = [0] * len(stock_prices)
    for i in range(len(stock_prices)):
        for j in range(i+1, len(stock_prices)):
            if stock_prices[i] > stock_prices[j]:
                result_list[i] += 1
                break
            else:
                result_list[i] += 1
    return result_list


def solution2(stock_prices: list) -> list:
    # Using Stack
    result_list = [0] * len(stock_prices)
    stack = []

    for i, price in enumerate(stock_prices):
        while stack and price < stock_prices[stack[-1]]:
            j = stack.pop()
            result_list[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        result_list[j] = len(stock_prices) - 1 - j
    return result_list


if __name__ == '__main__':
    prices = [1, 2, 3, 2, 3]
    print(solution2(prices))

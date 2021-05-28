# 이중 for 문
def solution(prices):
    len_price = len(prices)
    answer = [0] * len_price

    for i in range(len_price - 1):
        for j in range(i, len_price-1):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                break
    return answer

# 스택
# 처음 price를 stack에 쌓고, 다음 price가 더 크면, 스택에 쌓고, 작으면 pop


def solution(prices):

    len_price = len(prices)
    answer = [0] * len_price
    stack = []
    stack.append((prices[0], 0))

    for i in range(1, len_price):
        # 현재 price가 더 작다면,
        while stack and stack[-1][0] > prices[i]:
            out = stack.pop()  # stack에서 뽑아낸 정보
            answer[out[1]] = i - out[1]
        stack.append((prices[i], i))

    # 나머지 다 뽑기
    for st in stack:
        answer[st[1]] = len_price - st[1] - 1

    return answer

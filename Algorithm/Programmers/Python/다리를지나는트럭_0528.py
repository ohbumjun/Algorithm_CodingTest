from queue import deque
# 기본 개념 : 오른쪽으로 들어와서, 왼쪽으로 빠진다
# 이동 처리는 deque 를 통해 처리한다


def solution(bridge_length, weight, truck_weights):
    # time : 경과 시간 저장
    time = 0
    # bridge_weight : 현재 다리 weight
    bridge_weight = 0
    # 총 트럭 개수
    len_trucks = len(truck_weights)
    # 대기 트럭
    truck_weights = deque(truck_weights)
    # 현재 다리위의 트럭 정보
    bridge = deque([0 for i in range(bridge_length)])

    # 계속 왼쪽으로 truck들이 오는 개념으로 생각하면 된다
    while len(bridge) != 0:
        out = bridge.popleft()
        bridge_weight -= out
        time += 1
        # 대기 트럭이 존재한다면 넣는다
        if truck_weights:
            if bridge_weight + truck_weights[0] <= weight:
                in_truck = truck_weights.popleft()
                bridge.append(in_truck)
                bridge_weight += in_truck
        # 대기 트럭이 없다면, 새로 넣을 필요가 없다
            else:
                bridge.append(0)
    return time

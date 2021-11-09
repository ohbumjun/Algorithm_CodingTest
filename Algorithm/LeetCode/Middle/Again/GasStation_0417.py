#  https://leetcode.com/problems/gas-station/


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        즉, 특정 정점에서 출발해서
        cost는 빼주고
        gas는 더해주면서

        처음 출발점으로 돌아오게 된다면
        true
        아니면
        false
        를 return 해주는 것이다 

        < 특징 >
        - cost의 합이, gas 합들보다 크면 절대 다시 돌아올 수 없다
        - gas < cost인 정점은, start 정점으로 삼을 수 없다

        '''
        if sum(gas) < sum(cost):
            return -1
        for stIdx in range(len(gas)):
            cG = gas[stIdx] - cost[stIdx]
            if cG < 0:
                continue
            edIdx = stIdx
            cIdx = stIdx
            totGas = cG
            while True:
                '''
                매 이동마다, totGas에 그 다음 idx 에서의 gas[idx] - cost[idx] 를 더해간다
                '''
                cIdx += 1
                if cIdx == len(gas):
                    cIdx = 0
                totGas += (gas[cIdx] - cost[cIdx])
                if cIdx == edIdx and totGas >= 0:
                    return cIdx
                elif totGas < 0:
                    break
        return -1

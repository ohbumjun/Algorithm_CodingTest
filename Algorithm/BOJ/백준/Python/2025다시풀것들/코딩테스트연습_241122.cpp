#include <string>
#include <vector>
#include <queue>

using namespace std;


int solution(int stAlg, int stCod, vector<vector<int>> problems) 
{
    int answer = 0;
    
    int algReq = 0, codReq = 0;
    
    // 모든 문제 풀 수 있는 알고력, 코딩력 구하기
    for (const vector<int>& prob : problems)
    {
        algReq = algReq < prob[0] ? prob[0] : algReq;
        codReq = codReq < prob[1] ? prob[1] : codReq;
    }
    
    if (algReq <= stAlg && codReq <= stCod)
    {
        return 0;
    }
    
    // 5.1 vs 3.3
    algReq = stAlg > algReq ? stAlg : algReq;
    codReq = stCod > codReq ? stCod : codReq;
    
    // dp[알고력][코딩력] : 해당 알고력, 코딩력을 가지기 까지 걸리는 최소 시간
    vector<vector<int>> dpValue(algReq + 1, vector<int>(codReq + 1, int(1e9)));
    
    dpValue[stAlg][stCod] = 0;
    
    for (int alg = stAlg; alg <= algReq; alg++)
    {
        for (int cod = stCod; cod <= codReq; cod++)
        {
            // 알고리즘 공부로 알고력 상승
            if (alg + 1 <= algReq)
            {
                dpValue[alg + 1][cod] = min(dpValue[alg + 1][cod], dpValue[alg][cod] + 1);
            }
    
            // 코딩 공부로 코딩력 상승
            if (cod + 1 <= codReq)
            {
                dpValue[alg][cod + 1] = min(dpValue[alg][cod + 1], dpValue[alg][cod] + 1);
            }

            // 문제 풀어서 상승
            for (const vector<int>& prob : problems)
            {
                if (alg < prob[0])
                    continue;
                if (cod < prob[1])
                    continue;
                
                int algRet = prob[2];
                int codRet = prob[3];
                int cost = prob[4];
                
                int nxtAlg = alg + algRet;
                int nxtCod = cod + codRet;
                
                // 여기서 중요한 개념 : nxtAlg, nxtCod 가 algReq, codReq 를 넘으면
                // algReq, codReq 으로 nxtAlg, nxtCod 를 맞추면 된다.
                // 결국 nxtAlg, nxtCod 까지의 최단 시간이나, algReq, codReq 까지의 최단 시간이나
                // 동일한 값을 가지게 되기 때문이다.
                
                dpValue[min(algReq, nxtAlg)][min(codReq, nxtCod)] = min(
                    dpValue[min(algReq, nxtAlg)][min(codReq, nxtCod)], dpValue[alg][cod] + cost);
            }
        }
    }
    
    return answer = dpValue[algReq][codReq];
}
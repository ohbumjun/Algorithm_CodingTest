https://school.programmers.co.kr/learn/courses/30/lessons/60057

/*

*/

#include <string>
#include <vector>
#include <iostream>

using namespace std;


int solution(string s) {

    int answer = 10000;
    for(int i=1; i<= s.length(); i++){
        // 가장 작은 단위부터 먼저 나눈다.
        string sub = "";
        string str=s.substr(0,i); 
        int cnt=1;
        // 같은 단위의 숫자만큼 비교 시작점 위치를 증가시킨다.
        for(int j=i;j<=s.length();j+=i){
            // 같을 경우, 같은 개수 cnt 증가 (compare return == 0 ? 같은 케이스)
            if(str.compare(s.substr(j,i))==0)
                cnt++;            
            else{
                // 같지 않을 경우, 지금까지의 결과를 문자열로 만들어준다.
                if(cnt!=1)
                    sub+=to_string(cnt)+str;
                else
                    sub+=str;
                // 비교할 새로운 기준 문자열 ? 을 만든다.
                // substr 의 경우, j + i  의 범위가 끝을 넘어가도, 끝까지의 범위 str 만 add
                str=s.substr(j,i);
                
                // 범위를 벗어나는 경우, 현재 남은 str 을 add 한다. 그 다음 for 문 break 할 것이므로
                if(j+i>s.length())
                    sub+=str;
                cnt=1;   
            }        
        }
        if(sub.length()<answer)
            answer=sub.length();
    }

    return answer;
}
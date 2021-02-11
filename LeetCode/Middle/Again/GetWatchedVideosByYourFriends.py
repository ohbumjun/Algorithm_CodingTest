# https://leetcode.com/problems/get-watched-videos-by-your-friends/


class Solution(object):
    def watchedVideosByFriends(self, watchedVideos, friends, id, level):
        """
        :type watchedVideos: List[List[str]]
        :type friends: List[List[int]]
        :type id: int
        :type level: int
        :rtype: List[str]
        """
        # Part 1.  BFS to get friends of id at level k
        q, visited = deque([id]) , set()
        visited.add(id)

        # 보통 queue가 빌때까지, True로 하지만, 여기서는 level단위로 while 탈출문을 정의한다.
        while level > 0 :
            # 한레벨에 내려갈 때마다 level -= 1을 해준다.
            level -= 1

            for _ in range(len(q)):
                # 레벨 단위로 접근한다는 것은, 한 레벨에, queue에 들어가는 애들이 set가 된다.
                j = q.popleft()
                # 꺼낸 애들에 대해서 다시 모두 넣어준다.
                for x in friends[j] :
                    # 중복될 수 있으므로, x not in visited라고 해준다 ( 친구들이, 같은 친구의 친구를 가질 수 있다 )
                    if x not in visited :
                        visited.add(x)
                        q.append(x)
            # q contains frinds at level k


        # Part 2. Get watched movies of level k friends and sort them 
        res, freq = [],  Counter() # res variable needed to sort in alphabetorder 
        for x in q : # list of friends exist in q 
            for w in watchedVideos[x] : # 해당 friend가 본 비디오 
                freq[w] += 1
                if w not in res :
                    res.append(w)
        
        res.sort( key = lambda x : ( freq[x], x ) )
        
        return res
    
                
        
    
    
                    
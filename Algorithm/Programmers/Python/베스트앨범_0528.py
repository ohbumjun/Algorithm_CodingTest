def solution(genres, plays):
    hash_map = {}
    answer = []

    # 장르를 먼저 살핀다
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        if genre in hash_map:
            hash_map[genre]['plays'][i] = play
            hash_map[genre]['total_play'] += play
        else:
            hash_map[genre] = {
                # 같은 장르내에서도, 재생횟수 기준 정렬해야 한다
                # 몇번째 idx가 몇번 play 되었는지
                'plays': {
                    i: play
                },
                'total_play': play
            }
    # total play 수를 기준으로 sorting 한다
    # x[i] : value 부분에 해당하는 것 (key 제외)
    # - 을 붙여준 이유 : 내림차순 처리
    # 장르별 sorting 완료
    temp = sorted(hash_map.items(), key=lambda x: -x[1]['total_play'])
    print(temp)

    # 이제 plays 목록들을 정렬해야 한다
    # 각 곡별 sorting 완료
    for item in temp:
        target = item[1]['plays']
        # play 수 기준 먼저 정렬 --> 그 다음 idx 기준 정렬
        # -x[1] : plays 수 기준 정렬 + 내림 차순
        # x[0]  : idx 기준 오름차순 정렬
        item[1]['plays'] = sorted(target.items(), key=lambda x: (-x[1], x[0]))

    temp = dict(temp)

    for key in temp:
        try:
            answer += [temp[key]['plays'][0][0], temp[key]['plays'][1][0]]
        except:
            # 2개가 아니라 1개일 수도 있다
            answer += [temp[key]['plays'][0][0]]
    return answer

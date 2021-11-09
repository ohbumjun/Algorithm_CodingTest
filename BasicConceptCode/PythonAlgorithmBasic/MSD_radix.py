def radix_sort_MSD_for_strings(array, i):
    if len(array) <= 1:  # 길이 1이라는 것은, 이미 sorting 된 상태
        return array
    done_bucket = []
    bucket = [[] for _ in range(64, 100)]
    for s in array:
        if len(s) <= i:
            done_bucket.append(s)
        else:
            bucket[ord(s[i])-ord('a')].append(s)
    bucket = [radix_sort_MSD_for_strings(b, i+1) for b in bucket]
    # b 하나하나가 바로 말파벳에 해당한다
    return done_bucket + [b for blist in bucket for b in blist]


def main():
    # ASCII TABLE A-Z is from 64 to 90 if you want to    #change it  to lowercase letter Also change the bucket list's range
    array_of_strings = ['VEYSEL', 'EGE', 'EVY', 'EGF', 'YASIN', 'SELIN']


main()

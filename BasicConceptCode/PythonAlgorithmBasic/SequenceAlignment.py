# Sequence의 개념 ---
'''
# Sequence 란 무엇인가 ? 그리고 왜 Sequence Alignment를 해주는 가 ?

- Sequence : 연관된 요소들끼리 successive 하게 연결한 order를 의미한다
- Alignment를 해주는 이유는, 둘간의 similarity를 측정하기 위해서이다 ( 얼마나 다르고, 얼마다 비슷한지 )

'''
# Sequence Comparison & Edit Distance ---
'''
기본 개념 
1) match 
2) mismatcch >> substitution
3) gap ( 하나가 아예 없는 것 )
- Insertion
- Deletion

Deletion과 Insertion은 어떻게 구별할까 ??

" Edit Distance " ? 
=> Edit Distance between strings a and b , is the smallest number of the following operations, needed to transform a into b
1) mutate(replace) character
2) delete character
3) insert character

ex) 
from : TGCCATACT
to   : ATCCGAT

delete 3
insert 2
substi 1

'''

# Global Sequence Alignment : Needleman-Wunsch ---
'''
Match : 1
Mistmatch : -1
GAP : -2

DP로 푼다 
'''

# link : https://www.notion.so/Sequence-Alignment-7479f9733688471f89fc4757a80607e2

# Code
# Import Module

# Ask for sequences from the user
# sequence_1 = input("Enter or paste sequence 1 :")
# sequence_2 = input("Enter or paste sequence 2 :")

import numpy as np
sequence_1 = "ATCGT"
sequence_2 = "ACGT"

# Create Matrices
main_matrix = np.zeros((len(sequence_1)+1, len(sequence_2)+1))
match_checker_matrix = np.zeros((len(sequence_1), len(sequence_2)))

# Providing the scores for match , mistmatch, and gap
match_reward = 1
mistmatch_penalty = -1
gap_penalty = -2

# Fill the match checker matrix according to match or mismatch
for i in range(len(sequence_1)):
    for j in range(len(sequence_2)):
        if sequence_1[i] == sequence_2[j]:
            match_checker_matrix[i][j] = match_reward
        else:
            match_checker_matrix[i][j] = mistmatch_penalty

# print(match_checker_matrix)

# Filling up the matrix using Neeleman_Wunsch
# STEP1 : Initialization
for i in range(len(sequence_1)+1):
    main_matrix[i][0] = i * gap_penalty

for j in range(len(sequence_2)+1):
    main_matrix[0][j] = j * gap_penalty
for m in main_matrix:
    print(m)
print()
# STEP 2: Matrix Filling
for i in range(len(sequence_1)+1):
    for j in range(len(sequence_2)+1):
        main_matrix[i][j] = max(main_matrix[i-1][j-1] + match_checker_matrix[i-1][j-1],  # match or mismatch
                                main_matrix[i][j-1] + gap_penalty,  # from Left
                                main_matrix[i-1][j] + gap_penalty)  # from Up


# STEP 3 : Traceback
aligned_1 = ""
aligned_2 = ""

ti = len(sequence_1)
tj = len(sequence_2)

while(ti > 0 and tj > 0):
    # mismatch or match
    if(ti > 0 and tj > 0 and main_matrix[ti][tj] == main_matrix[ti-1][tj-1] + match_checker_matrix[ti-1][tj-1]):
        aligned_1 = sequence_1[ti-1] + aligned_1  # 문자를 더해간다
        aligned_2 = sequence_2[tj-1] + aligned_2

        ti = ti - 1
        tj = tj - 1
    # From Up to Down
    elif(ti > 0 and main_matrix[ti][tj] == main_matrix[ti-1][tj] + gap_penalty):
        aligned_1 = sequence_1[ti-1] + aligned_1
        # add gap to 2nd ( 왜냐하면, sequence_1은 그대로 이고, sequence_2 쪽에서 새로운 것을 채운 개념이라고 할 수 있기 때문이다 )
        aligned_2 = '-' + aligned_2

        ti = ti - 1
    else:  # From Left to Right
        aligned_1 = '-' + aligned_1
        aligned_2 = sequence_2[tj-1] + aligned_2

        tj = tj - 1

print("aligned_1", aligned_1)
print("aligned_2", aligned_2)

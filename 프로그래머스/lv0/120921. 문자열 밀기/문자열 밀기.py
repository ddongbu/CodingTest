def solution(A,B):
    A, B = list(A), list(B)
    #리스트 활용
    for cnt in range(len(A)):
        if A == B:
            return cnt
        
        A.insert(0,A.pop())
    
    return -1
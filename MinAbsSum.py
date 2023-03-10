def solution(A):
    # initialize S to all 1's
    S = [1] * len(A)
    # compute initial value of val(A, S)
    min_val = abs(sum(A))
    # repeat until no sign change reduces val(A, S) anymore
    while True:
        changed = False
        # try flipping the sign of each element in A
        for i in range(len(A)):
            # flip the sign of S[i]
            S[i] *= -1
            # compute new value of val(A, S)
            new_val = abs(sum(A[j] * S[j] for j in range(len(A))))
            # if new value is lower, keep the sign change
            if new_val < min_val:
                min_val = new_val
                changed = True
            # otherwise, revert the sign change
            else:
                S[i] *= -1
        # if no sign change reduced val(A, S), we're done
        if not changed:
            break
    return min_val

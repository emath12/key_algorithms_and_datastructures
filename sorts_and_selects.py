# ---- Quicksort ---- #

def partition(A, lo, hi):
    pivot = A[hi]

    # i points to where the pivot should go!
    # invariant: all the elements between the pivot and i should be less than the pivot,
    # and all the elements between the pivot and the end, represented by j, should be greater.

    # we decrement by 1 because lo points to first element we want to consider.
    # this is the "temp piv index". It's where the pivot should go as of now, simply the front of the list.
    i = lo - 1

    for j in range(lo, hi):
        if A[j] <= pivot:

            # we need to make room for the new element
            i = i + 1

            # move the element so that it goes before this temporary pivot.
            (A[i], A[j]) = (A[j], A[i])

    # putting the pivot where it needs to go.
    (A[i + 1], A[hi]) = (A[hi], A[i + 1])

    # returning the index of that pivot, showing the two sides that we need to recurse on.

    return i + 1

def quicksort(A, lo, hi):
    if lo < hi:

        piv = partition(A, lo, hi)

        # Recursive call on the left of pivot
        quicksort(A, lo, piv - 1)

        # Recursive call on the right of pivot
        quicksort(A, piv + 1, hi)

    return A

# ---- Quickselect ---- #

def q_select_partition(A, lo, hi):
    pivot = A[hi]

    i = lo - 1

    for j in range(lo, hi):
        if A[j] <= pivot:
            i = i + 1

            (A[i], A[j]) = (A[j], A[i])

    (A[i + 1], A[hi]) = (A[hi], A[i + 1])

    return i + 1

def quick_select(A, lo, hi, k): # also just k-th smallest

    pivot_index = q_select_partition(A, lo, hi)

    if pivot_index == k:
        return A[pivot_index]
    elif pivot_index > k:
        return quick_select(A, lo, pivot_index - 1, k)
    else:
        return quick_select(A, pivot_index + 1, hi, k - pivot_index)
        # find its order statistic relative to the right side. Since we know that it has to be on this right side.

if __name__ == '__main__':
    data = [1, 2, 0, -1, 2]

    # print(quicksort(data, 0, len(data) - 1))

    k = 0
    print(quick_select(data, 0, len(data) - 1, k))
    data.sort()
    print(data)
    print(data[k])
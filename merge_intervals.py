"""
Given a set of time intervals in any order, merge all overlapping intervals into one and output the result which should have only mutually exclusive intervals. Let the intervals be represented as pairs of integers for simplicity.
For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8}}. The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become {1, 4}. Similarly, {5, 7} and {6, 8} should be merged and become {5, 8}


1) Sort all intervals in increasing order of start time.
2) Traverse sorted intervals starting from first interval,
   do following for every interval.
      a) If current interval is not first interval and it
         overlaps with previous interval, then merge it with
         previous interval. Keep doing it while the interval
         overlaps with the previous one.
      b) Else add current interval to output list of intervals.
"""


def merge_intervals(arr):
    #sort based on the first element in the increasing order
    arr.sort(key = lambda x : x[0])
    m = []
    s = -10000
    max = -100000
    for i in range(len(arr)):
        a = arr[i]
        if a[0] > max:
            if i !=0:
                m.append([s, max])
            max = a[1]
            s = a[0]
        else:
            if a[1] >= max:
                max = a[1]
    if max != -100000 and [s, max] not in m:
        m.append([s, max])
        print ('Merged intervals are: ', end = '')
        for i in range(len(m)):
            print(m[i], end ='')


gq = [[6, 8], [1, 9], [2, 4], [4, 7]]
q = merge_intervals(gq)

        # if a[0] > max:
        #     if i !=0:
        #         m
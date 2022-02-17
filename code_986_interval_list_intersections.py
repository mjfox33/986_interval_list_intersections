class Solution:
    def intervalIntersection(self, firstlist: list[list[int]], secondlist: list[list[int]]) -> list[list[int]]:
        p1 = 0
        p2 = 0

        nf = len(firstlist)
        ns = len(secondlist)

        RANGE_START = 0
        RANGE_END = 1

        ranges = list()
        while p1 < nf and p2 < ns:
            if firstlist[p1][RANGE_START] < secondlist[p2][RANGE_START]:
                # go to the next range in the first list if the entire range
                # is before the start of the range from the second list
                if firstlist[p1][RANGE_END] < secondlist[p2][RANGE_START]:
                    p1 += 1
                else:
                    ranges.append([secondlist[p2][RANGE_START], min(firstlist[p1][RANGE_END], secondlist[p2][RANGE_END])])
                    if secondlist[p2][RANGE_END] < firstlist[p1][RANGE_END]:
                        p2 += 1
                    else:
                        p1 += 1
            else:
                # same as above but reversed 
                # if second range is before first range
                if secondlist[p2][RANGE_END] < firstlist[p1][RANGE_START]:
                    p2 += 1
                else:
                    ranges.append([firstlist[p1][RANGE_START], min(firstlist[p1][RANGE_END], secondlist[p2][RANGE_END])])
                    if firstlist[p1][RANGE_END] < secondlist[p2][RANGE_END]:
                        p1 += 1
                    else:
                        p2 += 1

        return ranges




                
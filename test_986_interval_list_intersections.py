from code_986_interval_list_intersections import Solution

def test_example_1():
    s = Solution()
    firstList = [[0,2],[5,10],[13,23],[24,25]]
    secondList = [[1,5],[8,12],[15,24],[25,26]] 
    result = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
    assert s.intervalIntersection(firstList, secondList) == result

def test_example_2():
    s = Solution()
    firstList = [[1,3],[5,9]]
    secondList = [] 
    result = []
    assert s.intervalIntersection(firstList, secondList) == result

def check(course, Visit, preMap):
    if course in Visit:
        return False
    if preMap[course] == []:
        return True
    Visit.add(course)
    for pre in preMap[course]:
        if check(pre, Visit, preMap) == False:
            return False
    Visit.remove(course)
    preMap[course] = []
    return True


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        Visit = set()
        for i in range(numCourses):
            preMap[i] = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
        for crs in preMap:
            if check(crs, Visit, preMap) == False:
                return False
        return True
        


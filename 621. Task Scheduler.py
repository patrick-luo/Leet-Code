class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        counts = [0] * 26
        for t in tasks:
            counts[ord(t)-ord('A')] += 1
        counts.sort(reverse=True)
        maxCnt = max(counts)
        # the idleTime is allocated here
        # for the task with the max count,
        # add then we keep filling these
        # idleTime (slots)
        idleTime = (maxCnt-1) * n
        for cnt in counts[1:]:
            # if a task has the same max count,
            # it will consume one more slot, and
            # thus the final idleTime could < 0
            idleTime -= min(maxCnt-1, cnt)
        return len(tasks)+idleTime if idleTime>0 else len(tasks)

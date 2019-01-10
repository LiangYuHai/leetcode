class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        triangle = []
        for k in range(rowIndex + 1):
            row = []
            if k == 0:
                row.append(1)
                triangle.append(row)
                continue

            for i in range(k + 1):
                if i == 0:
                    row.append(1)
                    continue
                if i == k:
                    row.append(1)
                    continue
                row.append(triangle[k - 1][i - 1] + triangle[k - 1][i])
            triangle.append(row)

        return triangle[-1]
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        tr=[]
        for i in range(numRows):
            row=[]
            if i==0:
                row.append(1)
                tr.append(row)
                continue
            for j in range(i+1):
                if j==0:
                    row.append(1)
                    continue
                if j==i:
                    row.append(1)
                    continue
                row.append(tr[i-1][j-1]+tr[i-1][j])
            tr.append(row)
        return tr
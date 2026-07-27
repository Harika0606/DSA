class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        rows=[]
        for i in range(numRows):
            num=1
            row=[]
            for j in range(i+1):
                row.append(num)
                num=num*(i-j)//(j+1)
            rows.append(row)
        return rows
        
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        

        # details = ["1313579440F2036","2921522980M5644"]
        #                   0                   1
        #            0 = "1313579440F2036"
        #        0[12] = 2           


        count = 0
        for i in details:
            if int(i[11:13]) >= 61:
                count +=1
            
        return count 
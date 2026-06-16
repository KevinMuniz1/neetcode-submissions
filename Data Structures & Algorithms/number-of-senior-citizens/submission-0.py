class Solution:
    def countSeniors(self, details: List[str]) -> int:

        count = 0

        print(details[0][11:13])

        for i in details:

            if int(i[11:13]) > 60:
                count += 1
        
        return count

        

               
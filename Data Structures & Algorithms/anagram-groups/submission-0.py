class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
   
        results = defaultdict(list) # auto create an empty list for empty keys


        for word in strs:
                count = [0] * 26 # set up an empty freq list for all possible letters (26 of them)

                for char in word:

                    count[ord(char) - ord("a")] += 1  #since words are producing same count tuples as
                results[tuple(count)].append(word)    #keys, thats how it nows to put anagrams togethers

        return list(results.values())





    

            

class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        people.sort()   #Sorting of list
        r = len(people)-1   # right pointer
        l = 0 # left pointer
        count=0 

        while(l<=r):
            capacity =  limit - people[r] 
            if capacity>= people[l]: #if capacity >0  and less than the left 
            # pointer #it means capacity exceed and (3>4) then left cant  
            #be adjusted make count++
                l = l+1
    
            r = r-1    # update it always
            count = count + 1
        return count
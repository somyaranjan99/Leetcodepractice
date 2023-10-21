class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unque_set=set()
        for email in emails:
            name,domain=email.split('@')
            name= name.split('+')[0]
            name=name.replace('.','')
            unque_set.add((name,domain))
        return len(unque_set)
            
        
class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueMail=set()
        for e in emails:
            name,domain= e.split("@")
            name=name.replace('.','')
            name =name.split('+')[0]
            uniqueMail.add((name,domain))
        return len(uniqueMail)


        
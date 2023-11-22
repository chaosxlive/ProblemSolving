# https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visit = {}
        for cpdomain in cpdomains:
            cp_split = cpdomain.split(' ')
            cnt = int(cp_split[0])
            domain_split = reversed(cp_split[1].split('.'))
            temp = ""
            for domain_name in domain_split:
                temp = domain_name + temp
                if temp in visit:
                    visit[temp] += cnt
                else:
                    visit[temp] = cnt
                temp = '.' + temp
        
        result = []
        for key, value in visit.items():
            result.append(str(value) + " " + key)
        return result
            
# https://leetcode.com/problems/unique-email-addresses/

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        seen = set()
        for email in emails:
            local, domain = email.split('@')
            local = "".join(local.split('+')[0].split('.'))
            seen.add(local + '@' + domain)
        return len(seen)

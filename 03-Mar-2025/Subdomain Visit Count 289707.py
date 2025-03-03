# Problem: Subdomain Visit Count - https://leetcode.com/problems/subdomain-visit-count

class Solution:

    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:


        domain_visits_count = Counter()

      


        for cpdomain in cpdomains:


            visit_count = int(cpdomain.split(' ')[0])

            domain = cpdomain.split(' ')[1]

          


            subdomains = domain.split('.')

          

            

            for i in range(len(subdomains)):

                

                subdomain = '.'.join(subdomains[i:])

                domain_visits_count[subdomain] += visit_count

      

      

        result = [f"{count} {domain}" for domain, count in domain_visits_count.items()]

      


        return result
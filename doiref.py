#copied from https://gist.github.com/dobrosketchkun/f14e1ab9ae817b00b28251f11786fbcf

import requests
 
class CrossRefClient(object):
 
    def __init__(self, accept='text/x-bibliography; style=apa', timeout=3):
        """
        # Defaults to APA biblio style

        # Usage:
        s = CrossRefClient()
        print s.doi2apa("10.1038/nature10414")		
        """
        self.headers = {'accept': accept}
        self.timeout = timeout
 
    def query(self, doi, q={}):
        if doi.startswith("http://"):
            url = doi
        else:
            url = "http://dx.doi.org/" + doi

        r = requests.get(url, headers = self.headers)
        return r

    def doi2apa(self, doi):
        self.headers['accept'] = 'text/x-bibliography; style=apa'
        return self.query(doi).text
		
    def doi2turtle(self, doi):
        self.headers['accept'] = 'text/turtle' 
        return self.query(doi).text
		
    def doi2json(self, doi):
        self.headers['accept'] = 'application/vnd.citationstyles.csl+json' 
        return self.query(doi).json()
		

# keys = ['indexed', 'reference-count', 'publisher', 'issue', 'funder', 'content-domain', 'published-print', 'DOI', 'type', 'created', 'update-policy', 'source', 'is-referenced-by-count', 'title', 'prefix', 'volume', 'author', 'member', 'published-online', 'reference', 'container-title', 'original-title', 'language', 'link', 'deposited', 'score', 'subtitle', 'short-title', 'issued', 'references-count', 'journal-issue', 'alternative-id', 'URL', 'relation', 'ISSN', 'container-title-short', 'article-number']

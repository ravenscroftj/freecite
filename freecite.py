'''
Created on 22 Nov 2015

@author: James Ravenscroft
'''
from __future__ import print_function

import requests
import xml.etree.ElementTree as ET


__all__ = ["Client"]

class Client:
    
    def __init__(self, endpoint="http://freecite.library.brown.edu/citations/create"):
        self.endpoint = endpoint
        
    def parse(self, citationstring):
        
        r = requests.post(self.endpoint, 
                          data={"citation" : citationstring}, 
                          headers={"Accept": "text/xml"} )
        
        etree = ET.fromstring(r.text)
             
        citation = etree.find("citation")
        
        
        return { "authors": [ a.text for a in citation.iter("author")], 
               "title": citation.find("title").text, 
               "journal" : citation.find("journal").text,
               "volume" : citation.find("volume").text,
               "pages" : citation.find("pages").text
        }

    def parse_many(self, citations):

        r = requests.post(self.endpoint, 
                          data={"citation[]" : citations }, 
                          headers={"Accept": "text/xml"} )


        etree = ET.fromstring(r.text)

        for citation in etree.findall("citation"):
                  
            yield { "authors": [ a.text for a in citation.iter("author")], 
                   "title": citation.find("title").text, 
                   "journal" : citation.find("journal").text,
                   "volume" : citation.find("volume").text,
                   "pages" : citation.find("pages").text
            }
  
        
        
if __name__ == "__main__":
    
    client = Client()
    citation = client.parse("Whiting, D., Goldmark, J., Modern British Potters and their Studios, A&C Black, 2009. ISBN-10: 0713687320, p. 128-133.")
    
    print(citation)


    citations = client.parse_many(["Whiting, D., Goldmark, J., Modern British Potters and their Studios, A&C Black, 2009. ISBN-10: 0713687320, p. 128-133.",
        "A] Kirwan, J. (2004), Alternative Strategies in the UK Agro-Food System: Interrogating the Alterity of Farmers' Markets. Sociologia Ruralis, 44: 395-415. doi: 10.1111/j.1467-9523.2004.00283."])

    for c in citations:
        print (c)


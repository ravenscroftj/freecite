# FreeCite Python Client #

Simple python wrapper for FreeCite citation parsing service hosted by Brown university at http://freecite.library.brown.edu/

## Installation ##

Clone the git repository then run python setup:

````bash
$ git clone https://github.com/ravenscroftj/freecite.git
...

$ python setup.py install

````

## Usage ##

Very simple interface. To parse a citation do:

````python
>>> import freecite
>>> c = freecite.Client()
>>> c.parse("A] Kirwan, J. (2004), Alternative Strategies in the UK Agro-Food System: Interrogating the Alterity of Farmers' Markets. Sociologia Ruralis, 44: 395-415. doi: 10.1111/j.1467-9523.2004.00283.")
{'volume': '44', 'journal': 'Sociologia Ruralis', 'title': "Alternative Strategies in the UK Agro-Food System: Interrogating the Alterity of Farmers' Markets", 'pages': '395--415', 'authors': ['J Kirwan']}
````

If you have many citations to parse then making a separate HTTP request for each is going to be very inefficient. You can bundle up a number of citations into one request if you want too. For example:


````python
>>> import freecite
>>> c = freecite.Client()
>>> citations = client.parse_many(["Whiting, D., Goldmark, J., Modern British Potters and their Studios, A&C Black, 2009. ISBN-10: 0713687320, p. 128-133.","Kirwan, J. (2004), Alternative Strategies in the UK Agro-Food System: Interrogating the Alterity of Farmers' Markets. Sociologia Ruralis, 44: 395-415. doi: 10.1111/j.1467-9523.2004.00283."])
{'volume': '2009', 'journal': 'A&C Black', 'title': 'Modern British Potters and their Studios', 'pages': '128--133', 'authors': ['D Whiting', 'J Goldmark']}
{'volume': '44', 'journal': 'Sociologia Ruralis', 'title': "Alternative Strategies in the UK Agro-Food System: Interrogating the Alterity of Farmers' Markets", 'pages': '395--415', 'authors': ['J Kirwan']}}
````

## Running your own server ##

If you have freecite installed on your own server then you can change the client endpoint when you initialise

````python
>>> import freecite
>>> c = freecite.Client("http://localhost:3000/citations/create")
````


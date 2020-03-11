
#Program to read and write from and to graph db repository

from SPARQLWrapper import SPARQLWrapper, BASIC

#connecting to graph db repository named project

db = SPARQLWrapper("http://localhost:7200/repositories/project/statements")

#SPARQL query to insert a relation
query = '''
PREFIX dc: <http://purl.org/dc/elements/1.1/>
INSERT { dc:temperature dc:value  "29" } WHERE {}
'''

db.setHTTPAuth(BASIC)
db.setCredentials('login', 'password')
db.setQuery(query)
db.method = "POST"
db.setReturnFormat('json')

#set query type as INSERT to insert into repository
db.queryType = "INSERT"

#run the query 
result = db.query()



#Program to write into a graph db repository

from SPARQLWrapper import SPARQLWrapper, BASIC

#connecting to graph db repository named project

db = SPARQLWrapper("http://localhost:7200/repositories/project/statements")

"""SPARQL query to insert a relation, crowded has temperature in namespace dc
and stored in variable query"""

query = '''
PREFIX dc: <http://purl.org/dc/elements/1.1/>
INSERT { dc:empty dc:has dc:co2 } WHERE {}
'''

#query for authentication to graph db repository with login and password

db.setHTTPAuth(BASIC)
db.setCredentials('login', 'password')

#sets query to prepare for execution

db.setQuery(query)
db.method = "POST"

"""When a relation is inserted ,a status report is sent in return .
The below code sets the status report in JSON format."""

db.setReturnFormat('json')

#set query type as INSERT to insert into repository

db.queryType = "INSERT"

#execute the query ,the status report returned is stored in variable result as a dictionary file
result = db.query()


#Print status report 
print(result)
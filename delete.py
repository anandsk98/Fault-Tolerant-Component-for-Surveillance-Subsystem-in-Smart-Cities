
#Program to delete a relation from graphdb repository

from SPARQLWrapper import SPARQLWrapper, BASIC,JSON

#connecting to graph db repository named project

db = SPARQLWrapper("http://localhost:7200/repositories/project/statements")

#SPARQL query to delete a relation, which is stored in variable query

query = '''
PREFIX : <http://purl.org/dc/elements/1.1/>
DELETE WHERE{dc:temperature ?name "high"}
'''

#query for authentication to graph db repository with login and password

db.setHTTPAuth(BASIC)
db.setCredentials('login', 'password')

#sets query to prepare for execution
db.setQuery(query)
db.method = "POST"

"""When a relation is inserted ,a status report is sent in return .
The below code sets the status report in JSON format."""

db.setReturnFormat(JSON)

#execute the query ,the status report returned is stored in variable result as a dictionary file
result = db.query()

#Prints status report
print(result)
#Program to query and fetch data from graph db repository.

from SPARQLWrapper import SPARQLWrapper, XML,BASIC,JSON,POST,N3
import json
import ast   
res=[]
topiclist=['TemperatureHumidity','Sound']
""" function to add namespace to query """
def append_topic(xc,query):
    xc="dc:"+xc
    query=query+"""?label ?l """+xc+"."
    print(query)

    return query
    

"""
This function is to fetch only the name of the sensors from the dictionary file in JSON format.
It is a recursive function.
result: dictionary from the graphdb
k,v :   key and value of dictionary 
res: list used to store the final output ,ie, the sensor names
"""

def myprint(result):
            for k,v in result.items():
                    if isinstance(v,dict):
                        myprint(v)
                    elif isinstance(v,list):
                        for l in v:
                            if isinstance(l,dict):
                                myprint(l)
                    else:
                        if(k=="value"):
                            res.append(v.split('/')[-1])


def search_query_ontology2(topiclist):
    
    if(len(topiclist)==0):
        print("Blank, returning")
        return
    else:
        #connecting to graph db repository named project
        db= SPARQLWrapper("http://localhost:7200/repositories/project")

        query="""
            PREFIX dc: <http://purl.org/dc/elements/1.1/>
            SELECT ?label
            WHERE { """

        
        print("Topic List",topiclist)
        
        for xc in topiclist:
            if len(xc)!=0:
                query=append_topic(xc,query)
        query=query+" }"
        print(query)


        #query for authentication to graph db repository with login and password

        db.setHTTPAuth(BASIC)
        db.setCredentials('login', 'password')

        #sets query to prepare for execution
        db.setQuery(query)
        db.method = "POST"

        #sets return format of the query containing the sensor details in a JSON format

        db.setReturnFormat(JSON)



        #run the  query 

        result = db.query().convert()

        #the result is stored in this variable as a dictionary format

        print(result)
        
        myprint(result)

        #prints the list of sensors under crowded

        for i in res: 
            print(i)
        return res
        
        
search_query_ontology2(topiclist)
from elasticsearch import Elasticsearch, helpers
import json

client = Elasticsearch(HOST="http://localhost", PORT=9200)
INDEX = 'tamilsongs_db'
top_words = ['சிறந்த',
             'மிக சிறந்த',
             'மிகச்சிறந்த',
             'மிகசிறந்த',
             'மிகவும்சிறப்பான',
             'சிறப்பான',
             'தலைசிறந்த']


def standard_analyzer(query):
    q = {
        "analyzer": "standard",
        "text": query
    }
    return q


def basic_search(query):
    q = {
        "query": {
            "query_string": {
                "query": query
            }
        }
    }
    return q

# match
def search_with_field(query, field):
    q = {
        "query": {
            "match": {
                field: query
            }
        }
    }
    return q

# Multi Match Query
def multi_match_query(target):
    q = {
            "query": {
                "multi_match" : {
                    "query": target,
                    "type": "most_fields",
                    "fields": [ "மூல பொருள் 1", "மூல பொருள் 2", "மூல பொருள் 3", "மூல பொருள் 4", "மூல பொருள் 5", "மூல பொருள் 6", "மூல பொருள் 7"]
                }
            }
        }
    return q


def multi_match(query, fields=['பாடல் பெயர்', 'பாடகர்','இசையமைப்பாளர்', 'பாடலாசிரியர்', 'திரைப்படம்', 'வெளியிடப்பட்ட ஆண்டு', 'பாடல் வரிகள்'], operator='or'):
    q = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": fields,
                "type": "best_fields"
            }
        }
    }
    return q


def exact_search(query):
    q = {
        "query": {
            "multi_match": {
                "query": query,
                "type": "phrase"
            }
        }
    }
    return q


def process_query(query):
    if '''"''' in query:
        query_body = exact_search(query)
    else:
        query_body = basic_search(query)
    return query_body


def search(query):
    query_body = process_query(query)
    print('Searching...')
    resp = client.search(index=INDEX, body=query_body)
    return resp

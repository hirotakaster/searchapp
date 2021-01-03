from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=[{'host': 'elasticsearch', 'port': 9200}])

def main():
    res = es.search(index="survey",
           body={"query":
                    {"match":
                        {"comment": "道路"}},
                "size" : 20})
    print (str(res['hits']['total']['value']) + "件ヒット")
    for doc in res['hits']['hits']:
        print (doc['_source'])

if __name__ == "__main__":
    main()
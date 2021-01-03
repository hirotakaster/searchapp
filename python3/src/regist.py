from elasticsearch import Elasticsearch
es = Elasticsearch(hosts=[{'host': 'elasticsearch', 'port': 9200}])

def main():
    for line in open('data.tsv', 'r'):
        it = line[:-1].split('\t')
        doc = {"category": it[0],
                "comment": it[1]}
        print (doc)
        res = es.index(index="survey", body=doc)
        print (res)

if __name__ == "__main__":
    main()
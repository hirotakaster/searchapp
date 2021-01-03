from django.shortcuts import render
from django.views.generic import View
from elasticsearch import Elasticsearch

class SearchView(View):
    es = Elasticsearch(hosts=[{'host': 'elasticsearch',
                               'port': 9200}])
    def get(self, request, *args, **kwargs):
        return render(request, 'search.html')

    def post(self, request, *args, **kwargs):
        searchstr = request.POST['word']
        res = self.es.search(
            index="survey",
            body={"size": 20,
                  "query":{
                    "match": {
                        'comment': searchstr
        }}})

        docs = []
        for doc in res['hits']['hits']:
            print (type(doc['_source']['category']))
            docs.append({'category': int(doc['_source']['category']),
                         'comment': doc['_source']['comment']})

        return render(request, 'search.html',
                      {'keyword': searchstr, 'docs': docs,})


# elastic-kuromoji
```
docker-compose build
docker-compose up -d
# create index
docker-compose exec elasticsearch bash
cd /mapping
curl -H "Content-Type: application/json" -X PUT 'http://localhost:9200/survey?pretty' -d @kuromoji_setting.json
curl -H "Content-Type: application/json" -X PUT 'http://localhost:9200/survey/_mapping/type?include_type_name=true&pretty' -d @mapping.json
exit
# regist data
docker-compose run python3 python regist.py
# search match_all
docker-compose run python3 python search.py
# django
http://localhost:8080/elastic/
```

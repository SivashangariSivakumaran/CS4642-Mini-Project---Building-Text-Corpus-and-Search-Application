# Tamil Songs  Database

This Repository includes the frontend,backend implementation for a search query.
After configuring the elasticsearch, the sample search engine is used to try the query searches.

Demo
---
* Install ElasticSearch
* Install packages `pip install -r requirements.txt`
* Add 'analyze' folder in config of Elasticsearch and add files from analyzers
* Run ElasticSearch
* Add index(uncomment indexing part if not manually added) and add data (`processed_review_bulk.json`)
* Run app.py
* Go to http://localhost/5000/
* Enter keyword for search
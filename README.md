# Tamil Songs  Database

Objectives of this proect
*Build a text corpus of Tamil movie songs contains at least one metaphor per song 
*Build a search engine using the corpus built which can be used to search wider range of queries about songs and metaphors used in it

Initially I build a corpus consists of 100 Unique songs including the metaphors in it 

The corpus file format was in csv. So As a first step we need to convert it into a json file which contains all 100 songs.

Later we need to create the index and add the documents in it using elastic search.

This search engine is capable of searching queries on tamil songs composed by AR Rahman and Yuvan from 2000 to 2022

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

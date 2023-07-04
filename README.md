# vector-es71

## Test
	docker build -t es71:0.1 .
	docker run --name estest -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" es71:0.1 


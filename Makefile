build: 
	docker build . -t server
run: 
	docker run -d -p 7002:65430 server
stop: 
	docker stop server
clean: 
	docker ps -a -q  --filter ancestor=server | docker rm

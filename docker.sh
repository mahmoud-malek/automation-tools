#!/bin/bash 
Container=$(docker ps -a --format "{{.Names}}"| fzf --header "Please choose a container")
if [ ! "$Container" ]; then
	echo "No Container selected!"
	exit
fi
if docker ps --format "{{.Names}}" | grep "$Container"; then
	echo "Container $Container is already started"
else
	echo "Starting $Container container"
	docker start "$Container"
fi
docker exec -it "$Container" /bin/bash

#!/bin/sh
image=$(basename $PWD)
docker run -d  -p 27017:27017 -v mongo_data_directory:/data/db --name=$image  -it  $1:latest 
#Run your Docker Image


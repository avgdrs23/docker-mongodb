#!/bin/sh

docker run -d  -p 27017:27017 -v mongo_data_directory:/data/db  -it $1:latest 
#Run your Docker Image


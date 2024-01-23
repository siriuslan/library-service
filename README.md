# library-service

## How to run for dev 
uvicorn main:app --reload

## How to run with a docker
enter project folder
docker build -t library-service .
docker run --env OPENAI_API_KEY=<you_opanai_key> -d --name library-service-container -p 8050:8050 library-service
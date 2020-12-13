# Hello
Test case for avito MI unit:
https://github.com/avito-tech/mi-backend-trainee-assignment


## Installation and launch:
            
-       $ git clone https://github.com/bestpilotingalaxy/test-case-av.git
                         
       
-       $ cd test-case-av
             
       
-       $ docker-compose up -d --build

Default: ARQ stats collecting sheduler set to run every 2 minutes.
Get a look on #TODO to set another time interval.

## Run tests

-      $ docker-compose exec fastapi pytest . 
      
## Docs

http://localhost:8000/docs

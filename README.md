   ### A simple redis queue system
   ##### What is this?
    Application have REST Service, Woker Queue using Redis. Request received using rest service , will add to Redis list and worker will process as redis-queue.
   #####  How do I use it?
    1. Run main_service.py for REST service.
         $ python main_service.py
        the application will host on 'http://localhost:5000/' and redis service will start on 'localhost:6379'.
        two rest end point :
        1. http://localhost:5000/{int}/{int}
        2. http://localhost:5000/status/{job-id}

    2. now Run worker_server.py as daemon:
         '$ python worker_service.py'
         the application will 'keep running'

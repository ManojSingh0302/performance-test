#  Setup
For setting up server we have followed the official documentations and from below url we have taken the code repository 
   `git clone -b v1.31.0 https://github.com/grpc/grpc`
   
Here we are taking simple example of hello world to demonstrate the load test with locust. 
Please install dependencies from requirement.txt before starting the test execution by following command.
    `$ pip install -r requirement.txt` 


#  Load Test Hello world with Locust UI
    1) To start the server run the following command 
        $ python server/python/helloworld/greeter_server.py
    2) To manually test the client you can run the client by following commands
        $  python server/python/helloworld/greeter_client.py
    3) Now to Run the locust in web mode run the following command 
        $ locust -f locust/load_test_grpc.py
    4) Locust load test sever started on default port[8089] and we can access by URL http://localhost:8089/
    5) Now to start the test select Number of total users to simulate along with Hatch rate (users spawned/second)
        Please note initially select smaller number so that your system doesn't hang.
    6) Now Start Swarming and observe the statistics and charts, you can stop the locust at any given point.
    
# Ways to run locust
    To run locust from command line, without web-ui, run following command
    locust -f locust/load_test_grpc.py --headless -u <No_users> -r <hatch/second> -t <stop_time>
                        
    e.g. locust -f locust/load_test_grpc.py --headless -u 10 -r 5 -t 3s

    WHERE 
    -u NUM_USERS, --users NUM_USERS
                        Number of concurrent Locust users. Only used together
                        with --headless
    -r HATCH_RATE, --hatch-rate HATCH_RATE
                        The rate per second in which users are spawned. Only
                        used together with --headless
    -t RUN_TIME, --run-time RUN_TIME
                        Stop after the specified amount of time, e.g. (300s,
                        20m, 3h, 1h30m, etc.). Only used together with
                        --headless
    
    
# To complie Proto file
Run following command from project directory (grpc-load-test-with-locust)

## Command Syntax: 
      ```grpc_tools.protoc -I=$SRC_DIR --python_out=$DST_DIR --grpc_python_out=$SRC_DIR proto/<app-name>.proto```

## Command:
      ```python3 -m grpc_tools.protoc -I=server/proto --python_out=server/proto --grpc_python_out=server/proto server/proto/helloworld.proto ```

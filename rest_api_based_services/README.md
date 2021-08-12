# Ways to run locust
    To run locust from command line, without web-ui, run following command
    locust -f locust/load_test_grpc.py --headless -u <No_users> -r <hatch/second> -t <stop_time>
                        
    e.g.  locust -f rest_api_based_services/load_test_rest_api_by_locust.py --headless -u 1 -r 1 -t 10s

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
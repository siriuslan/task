import sys

from worker_thread import WorkerThread


# ideally below 4 keys should be put in env varible or local file and loaded on application run,
# due to time limit I just leave them here with manually configured
api_key = "AAA"
api_key_secret = "BBB"
access_token = "CCC"
access_token_secret = "DDD"

if __name__ == '__main__':
    if api_key == "AAA" or api_key_secret == "BBB" or access_token == "CCC" or access_token_secret == "DDD":
        print("Please enter valid twitter api keys and access tokens")
        sys.exit()
    account = input("Please enter twitter account name you want to monitor(exclude @, i.e. @BillGates, you should enter BillGates): ")
    if not account:
        print("Please enter valid account and start application again")
        sys.exit()
    new_command = None
    worker = WorkerThread(account, api_key, api_key_secret, access_token, access_token_secret)
    while new_command != 'quit':
        new_command = input("please enter run, dump or quit: ")
        if new_command == 'run':
            try:
                worker.start()
            except:
                print(f"Error: unable to start thread.")
        elif new_command == 'dump':
            print(f"Currently collected tweets - {total_tweets}")
        elif new_command == 'quit':
            worker.stop()
            print("Quit application.")
        else:
            print("Invalid command, please enter run, dump or quit.")
    
    worker.join()
    print("Bye!")
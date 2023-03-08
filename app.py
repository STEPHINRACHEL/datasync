import argparse
import time
from synchronization import sync

# Adding CLI arguments
all_args = argparse.ArgumentParser(description="Synchronize two folders...!")
all_args.add_argument("--source", required=True, type=str,
                      help="Provide path to source folder")
all_args.add_argument("--replica", required=True, type=str,
                      help="Provide path to the folder for copying data from source")
all_args.add_argument("--sync_interval", required=True, type=int,
                      help="Provide interval in seconds between synchronizations")
all_args.add_argument("--log_file", required=True, type=str,
                      help="Provide path to log file for logging the sync actions")
args = all_args.parse_args()


def main():
    # For better readability store values of arguments to variables
    source = args.source
    replica = args.replica
    sync_interval = args.sync_interval
    log_file = args.log_file
    sync.getLogs(log_file)
    print("Synchronizing source folder to replica folder.....!")
    # Periodically execute the syncData() function at a specified interval
    while True:
        sync.syncData(source, replica)
        time.sleep(sync_interval)


if __name__ == '__main__':
    main()
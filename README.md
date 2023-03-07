# Datasync
This is a data sync tool that allows synchronization of source and replica folders periodically.

# Prerequisites
* Install Python 3 from [Python.org](https://www.python.org/downloads/) 
* git CLI

# Usage

1. Open terminal and checkout this repo using `git clone https://github.com/STEPHINRACHEL/datasync.git`
2. From the root of the directory execute `python3 app.py -h` to list the argumets along with the description
3. Run `python3 app.py --source <path-to-source-file> --replica <path-to-replica-file> --sync_interval <interval-in-seconds> --log_file <path-to-log-file>` <br />
  Example:  
  ```
  python3 app.py --source data/source --replica data/replica --sync_interval 3 --log_file data/logs
  ```


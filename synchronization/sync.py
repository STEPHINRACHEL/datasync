import logging
import os
import shutil
import time


#Set up logging
def get_logs(log_file):
    #save logs to the log_file
    logging.basicConfig(filename=log_file, encoding='utf-8',
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s:%(message)s',
                        datefmt='%Y-%m-%d %I:%M:%S %p')

    #add console_handler for printing logs in the console
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logging.getLogger().addHandler(ch)


# Check if the source file is modified
def is_modified(file_path, sync_interval):
    current_time = time.time()
    modified_time = os.path.getmtime(file_path)
    if current_time - modified_time < sync_interval:
        return True
    else:
        return False


# Synchronize source and replica folders
def sync_data(source, replica, interval):
    source_items = set(os.listdir(source))
    replica_items = set(os.listdir(replica))
    
    # Copy new files/folders from source to replica
    for item in source_items:
        if item not in replica_items:
            source_path = os.path.join(source, item)
            replica_path = os.path.join(replica, item)
            if os.path.isfile(source_path):
                shutil.copy2(source_path, replica_path)
                logging.info(f"Created new file {replica_path}")
            else:
                shutil.copytree(source_path, replica_path)
                logging.info(f"Created new folder {replica_path}")

    # Delete files/folders in replica that are not in source
    for item in replica_items:
        if item not in source_items:
            replica_path = os.path.join(replica, item)
            if os.path.isdir(replica_path):
                shutil.rmtree(replica_path)
                logging.info(f"Folder deleted {replica_path}")
            else:
                os.remove(replica_path)
                logging.info(f"File deleted {replica_path}")

    # Update files if modified
    for item in source_items & replica_items:
        source_path = os.path.join(source, item)
        replica_path = os.path.join(replica, item)
        if os.path.isfile(source_path):
            if is_modified(source_path, interval):
                shutil.copy2(source_path, replica_path)
                logging.info(f"Updated file {replica_path}")
        else:
            # Recursively sync sub folders
            sync_data(source_path, replica_path, interval)


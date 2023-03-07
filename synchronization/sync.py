import hashlib
import logging
import os
import shutil



def updateData(source_file, replica_file):
    pass
    # with open(source_file, 'rb') as file:
    #     file_contents = file.read()
    #
    # # Compute the MD5 hash of the file contents
    # md5_hash = hashlib.md5(file_contents).hexdigest()
    #
    #
    # previous_hash = get_perevious_hash()
    # # Check if the hash has changed
    # if md5_hash != previous_hash:
    #     print(f"The file has been updated! {previous_hash}")
    #     previous_hash = md5_hash
    # return previous_hash

def getLogs(log_file):
    #Set up logging
    logging.basicConfig(filename=log_file, encoding='utf-8',
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s:%(message)s',
                        datefmt='%Y-%m-%d %I:%M:%S %p')

    #create console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    logging.getLogger().addHandler(ch)
def syncData(source, replica):
    source_contents = set(os.listdir(source))
    replica_contents = set(os.listdir(replica))



    for content in source_contents:
        if content not in replica_contents:
            source_path = os.path.join(source, content)
            replica_path = os.path.join(replica, content)
            if os.path.isfile(source_path):
                shutil.copy2(source_path, replica_path)
                logging.info(f"Created new file {replica_path}")
            else:
                shutil.copytree(source_path, replica_path)
                logging.info(f"Created new folder {replica_path}")

    for content in replica_contents:
        if content not in source_contents:
            replica_path = os.path.join(replica, content)
            if os.path.isdir(replica_path):
                shutil.rmtree(replica_path)
                logging.info(f"Folder deleted {replica_path}")
            else:
                os.remove(replica_path)
                logging.info(f"File deleted {replica_path}")

    for item in source_contents & replica_contents:
        source_path = os.path.join(source, item)
        replica_path = os.path.join(replica, item)
        if os.path.isdir(source_path):
            syncData(source_path, replica_path)
        else:
            prev_hash = updateData(source_path, replica_path)




# * Aim: Create a system to track files (Addition, modification or deletion) using watchdog

import os
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class monitorFolder(FileSystemEventHandler):
    global FILE_SIZE
    FILE_SIZE = 0
    
    def on_created(self, event):
        print('File created in path:', event.src_path, 'type:', event.event_type)
        self.checkFolderSize(event.src_path)
    
    def on_modified(self, event):
        print('File modified in path:', event.src_path, 'type:', event.event_type)
        self.checkFolderSize(event.src_path)
    
    def on_deleted(self, event):
        print('File deleted on path:', event.src_path, 'type:', event.event_type)
    
    def checkFolderSize(self, src_path):
        if os.path.isdir(src_path):
            if os.path.getsize(src_path) > self.FILE_SIZE:
                print('File size exceeded the given size of', FILE_SIZE)

if __name__ == "__main__":
    src_path = sys.argv[1]

    event_handler = monitorFolder()
    observer = Observer()
    observer.schedule(event_handler, path=src_path, recursive=True)
    print("Monitoring started")     # TODO: Augment this with a timestamp using the datetime library, as well as output this to the log file
    observer.start()

    try:
        while True:
            time.sleep(5)
        
    except KeyboardInterrupt:
        observer.stop()
        observer.join()
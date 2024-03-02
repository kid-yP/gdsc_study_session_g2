import os
import shutil
import time

def collect_and_move_files():
    try:
        current_directory = os.getcwd()
        last_24hours_directory = os.path.join(current_directory, "last_24hours")

        if not os.path.exisits(last_24hours_directory):
            os.makedirs(last_24hours_directory)

        files = [f for f in os.listdir(current_directory) if os.path.isfile(os.path.join(current_directory, f))]
        current_time = time.time()

        for file in files:
            file_path = os.path.join(current_directory,file)
            file_stat = os.stat(file_path)

            if (current_time -  file_stat.st_mtime) < 24 * 3600 or (current_time - file_stat.st_ctime) < 24 * 3600:
                shutil.move(file_path, os.path.join(last_24hours_directory, file))
    except Exception as e:
        print(f"Error: {e}")
collect_and_move_files()
import time
import subprocess
import os
import sys

filename = sys.argv[1]+'.py'

justfile_dir = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(justfile_dir, 'src', filename)

# Last change time
current_mod_time = os.stat(file_path).st_mtime

while True:
    # If there was a change run pytest
    if os.stat(file_path).st_mtime != current_mod_time:
        current_mod_time = os.stat(file_path).st_mtime
        # Change the current working directory because pytest runs from it
        os.chdir(os.path.join(justfile_dir))
        subprocess.run('cmd /C "set PYTHONPATH={} && pytest -s src/__tests__/test_{}"'.format(
            os.path.join(justfile_dir), filename), shell=True)

    # Wait before checking again
    time.sleep(1)

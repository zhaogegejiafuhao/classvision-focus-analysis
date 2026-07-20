import subprocess
import os
import signal

result = subprocess.run(['wmic', 'process', 'where', "name='python.exe'", 'get', 'processid,commandline', '/format:csv'], capture_output=True, text=True)
for line in result.stdout.split('\n'):
    if 'test_retrieve_only' in line:
        parts = line.strip().split(',')
        pid = int(parts[-1])
        print(f"Killing PID {pid}: {line.strip()}")
        try:
            os.kill(pid, signal.SIGTERM)
            print(f"  Killed {pid}")
        except Exception as e:
            print(f"  Failed: {e}")
    elif 'test_dual_mode' in line:
        parts = line.strip().split(',')
        pid = int(parts[-1])
        print(f"Killing PID {pid}: {line.strip()}")
        try:
            os.kill(pid, signal.SIGTERM)
            print(f"  Killed {pid}")
        except Exception as e:
            print(f"  Failed: {e}")
print("Done")

import pty
import os
import subprocess
import time

m, s = pty.openpty()
p = subprocess.Popen(["agy"], stdin=s, stdout=s, stderr=s, close_fds=True, env=os.environ.copy())
os.close(s)

print("Reading...")
import fcntl
fl = fcntl.fcntl(m, fcntl.F_GETFL)
fcntl.fcntl(m, fcntl.F_SETFL, fl | os.O_NONBLOCK)

time.sleep(2)
try:
    print(os.read(m, 1024))
except Exception as e:
    print(e)
p.kill()

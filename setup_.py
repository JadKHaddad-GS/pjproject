from pathlib import Path
import subprocess

current_file_dir = Path(__file__).absolute().parent
pjproject_dir = current_file_dir.parent.parent.parent.parent
returncode = subprocess.Popen("ls", shell=True, cwd=pjproject_dir).wait()
print("-----------------> returncode: ", returncode)
returncode = subprocess.Popen("./configure --enable-shared", shell=True, cwd=pjproject_dir).wait()
print("-----------------> returncode: ", returncode)
if returncode > 0:
    exit(returncode)
    
p = subprocess.Popen("make dep", shell=True, cwd=pjproject_dir).wait()
p = subprocess.Popen("make", shell=True, cwd=pjproject_dir).wait()
p = subprocess.Popen("make install", shell=True, cwd=pjproject_dir).wait() # this one installs the libs

p = subprocess.Popen(["swig \
    -I../../../../pjlib/include \
    -I../../../../pjlib-util/include \
    -I../../../../pjmedia/include \
    -I../../../../pjsip/include \
    -I../../../../pjnath/include \
    -c++ \
    -w312 \
    -python \
    -o pjsua2_wrap.cpp \
    ../pjsua2.i"], shell=True, cwd=current_file_dir).wait()

# find / -name libpjsua.so.2
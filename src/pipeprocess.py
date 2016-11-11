import multiprocessing
import logging as log
import io
import time
import subprocess
import signal

from multiprocessing import Value

# This class launches the usbboard data acquisition as a python subprocess.
# The data is sent through the std::cout of the usbboard software which pipes it to python.
class PipeProcess(object):
    def __init__(self, result_queue,
                 cmd="./fake_track_pebs.py", args=[]):
        self.queue = result_queue
        self.proc = None
        self.exit = multiprocessing.Event()
        self.cmd = cmd
        self.args = args
        self.is_running = True
        log.info("PipeProcess ready")

    
    def start(self): 
        if not self.proc:
            self.proc = multiprocessing.Process(target=self.run) # object multiprocessing
            self.proc.start() # commence
        self.is_running = True
    
    def run(self):
        timestamp = time.time()
        self.proc = subprocess.Popen([self.cmd,  ] + self.args,   # deffinie les buffers dans lesquels multiprocessing va chercher les donners
                                stdout=subprocess.PIPE,
                                stdin=subprocess.PIPE,
                                universal_newlines=True,
                                bufsize=1)
        for line in self.proc.stdout:
            """io.TextIOWrapper(proc.stdout, 
                                    line_buffering=False,
                                    write_through=True,
                                    encoding=None):
            """
            """
            if self.exit.is_set():
                log.info("Subprocess finishing...")
                self.proc.terminate()
            """
            data = line.strip()
            if self.is_running and data != '':
                self.queue.put(data)

    def stop(self):   # stop le processing
        log.info("Subprocess finishing...")
        self.is_running = False
        """
        if self.proc:
            self.proc.terminate()
        """
        log.info("PipeProcess finishing...")
        self.exit.set()

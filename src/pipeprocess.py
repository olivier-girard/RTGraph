import multiprocessing
import logging as log
import io
import time
import subprocess
import signal
import signal

from multiprocessing import Value

class PipeProcess(object):
    def __init__(self, result_queue,
                 cmd="./fake_acq.py", args=[]):
        self.queue = result_queue
        self.proc = None
        self.exit = multiprocessing.Event()
        self.cmd = cmd
        self.args = args
        log.info("PipeProcess ready")

    
    def start(self):
        self.proc = multiprocessing.Process(target=self.run)
        self.proc.start()
    
    def run(self):
        print("Running!")
        timestamp = time.time()
        self.proc = subprocess.Popen([self.cmd,  ] + self.args,
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
            if self.exit.is_set():
                log.info("Subprocess finishing...")
                self.proc.terminate()

            data = line.strip()
            if data != '':
                self.queue.put(data)

    def stop(self):
        log.info("Subprocess finishing...")
        if self.proc:
            self.proc.terminate()
        log.info("PipeProcess finishing...")
        self.exit.set()

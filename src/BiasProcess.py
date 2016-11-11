import multiprocessing
import logging as log
import io
import time
import subprocess
import signal

from multiprocessing import Value

class BiasProcess(object):
    def __init__(self, 
                 cmd="", args=[]):
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
        log.info("Setting bias voltage...")
    
    def run(self):
        self.proc = subprocess.Popen([self.cmd,  ] + self.args)


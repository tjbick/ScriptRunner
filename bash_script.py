import os
import subprocess


class Bash_Script:
    def __init__(self, path):
        self.path = path
        self._raw_usage = subprocess.run([path, '-u'], stdout=subprocess.PIPE).stdout.decode('utf-8')
        self._argv_labels = self._raw_usage.split()[1::]
        self._argv = []

    def run(self):
        pass


    

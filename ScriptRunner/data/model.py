import os
import subprocess
from errors import DirException, CmdException

class Folder:
    def __init__(self, dir):
        self.dir = dir + '/'
        if not os.path.isdir(self.dir):
            raise DirException (self.dir + 'Is not a valid directory')
        self.inner_folders = []
        self.scripts = []
        self.text_files = []
        self.all_contents = []
        self.extract_contents()
    
    def extract_contents(self):
        self.all_contents = Script.run_cmd('ls', self.dir).split('\n')

        for entry in self.all_contents:
            if os.path.isdir(self.dir + entry):
                self.inner_folders.append(entry)
            elif entry[-3::] == '.sh':
                self.scripts.append(entry)
            elif entry[-4::] == '.txt':
                self.text_files.append(entry)
        self.all_contents.append("Return")



class Script:
    def __init__(self, cmd, args=None):
        self.cmd = cmd
        self.args = args

    def run(self):
        return Script.run_cmd(self.cmd, self.args)

    def run_cmd(cmd, argv=None):
        try:
            if argv == None:
                results = subprocess.run([cmd], stdout=subprocess.PIPE).stdout.decode('utf-8')
            else:
                results = subprocess.run([cmd, argv], stdout=subprocess.PIPE).stdout.decode('utf-8')
        except Exception as e:
            raise CmdException ("{} Failed for the following reason\n {}".format(cmd, e))
        return results

class Text_File:
    def __init__(self):
        pass

f = Folder("/users/groups/cs324ta/grading")
s = Script('ls')
print(s.run())
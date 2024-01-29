import sys
import os
class runner:
    def __init__(self, run, lists):
        self.run = run
        self.list = lists

    def superrun(self):
        #for i in range(self.list.size()):
        #intel = self.list[i]
        with open(self.list) as f:
            for line in f:
                intel  = line.strip()
                (lambda v: os.popen(self.run+v))(intel)

class superstantiate(runner):
    def __init__(self, run, lists):
        super(superstantiate, self).__init__(run, lists)
testrun = superstantiate(sys.argv[1], sys.argv[2])

testrun.superrun()
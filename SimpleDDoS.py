﻿import time
import ProcessFactory
import sys
import Requster

ProcessArray = list()

i = int(sys.argv[1])
URL = sys.argv[2]


TestRq = Requster.HTTPClient()
TestRq.SetPayload({"Russian_Warship" : "Go Fuck yourself"})

while i != 0:
    ProcessArray.append(ProcessFactory.ProcessFactory(f"Process{i}").CreateInstance(TestRq.PostRequest))
    i -= 1


if __name__ == '__main__':
    start = time.perf_counter()
    for process in ProcessArray:
        process.start()
    end = time.perf_counter()
    print(f'Finished in {round(end-start, 2)} second(s)')

import time
import App.ProcessFactory as ProcessFactory
import sys
import App.Requster as Requster

ProcessArray = list()

i = int(sys.argv[1])
URL = sys.argv[2]


TestRq = Requster.HTTPClient(URL)
TestRq.SetPayload({"Russian_Warship" : "Go Fuck yourself"})

while i != 0:
    ProcessArray.append(ProcessFactory.ProcessFactory(f"Process{i}").CreateInstance(TestRq.GetRequest))
    i -= 1


if __name__ == '__main__':
    start = time.perf_counter()
    for process in ProcessArray:
        process.start()
    end = time.perf_counter()
    print(f'Finished in {round(end-start, 2)} second(s)')


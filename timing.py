import atexit
from time import process_time
from functools import reduce

def secondsToStr(t):
  #Build (Hours, Minutes, Seconds, Miliseconds) tuple
  timeTuple = reduce(lambda ll,b : divmod(ll[0],b) + ll[1:], [(t*1000,),1000,60,60])
  #Build easy to read format
  formattedTime = ""
  if timeTuple[0] > 0:
    formattedTime = "%d hours " % timeTuple[0]
  if timeTuple[1] > 0:
    formattedTime += "%2d minutes " % timeTuple[1]
  if timeTuple[2] > 0:
    formattedTime += "%2d seconds " % timeTuple[2]
  if timeTuple[3] > 0:
    formattedTime += "%3d milliseconds" % timeTuple[3]
  return formattedTime

line = "=" * 40
def log(s, elapsed=None):
  print(line)
  print(now(), '-', s)
  if elapsed:
    print("Elapsed time:", elapsed)
  print(line)
  print

def endlog():
  end = process_time()
  elapsed = end - start
  log("End Program", secondsToStr(elapsed))

def now():
  return secondsToStr(process_time())

start = process_time()
atexit.register(endlog)
log("Start Program")
###################################################################
# producer and comsumer treads communicating with a shared queue
###################################################################

numconsumers = 2                  # how many consumers to start
numproducers = 4                  # how many producers to start
nummessages  = 4                  # messages per producer to put

import thread, Queue, time
safeprint = thread.allocate_lock()    # else prints may overlap
dataQueue = Queue.Queue()             # shared global. infinite size

def producer(idnum):
    for msgnum in range(nummessages):
        time.sleep(idnum)
        dataQueue.put('producer %d:%d' % (idnum, msgnum))

def consumer(idnum):
    while 1:
        time.sleep(0.1)
        try:
            data = dataQueue.get(block=False)
        except Queue.Empty:
            pass
        else:
            safeprint.acquire()
            print 'consumer', idnum, 'got =>', data
            safeprint.release()

if __name__ == '__main__':
    for i in range(numconsumers):
        thread.start_new_thread(consumer, (i,))
    for i in range(numproducers):
        thread.start_new_thread(producer, (i,))
    time.sleep(((numproducers-1) * nummessages) + 1)

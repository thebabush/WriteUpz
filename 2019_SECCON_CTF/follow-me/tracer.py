# WARNING: using qbdi w/ python2

import struct
import sys

import pyqbdi


# Read the rebased trace (skip first few jumps)
trace = [int(l.strip(), 16) for l in open('./trace.txt', 'r').readlines()]
trace = trace[5:]

# Keep a set of the interesting jumps
interesting = set(trace)

# .text start/stop range for rebasing
image_start, image_stop = None, None

# =1 if we don't analyze the execution anymore
early_exit = 0


def mycb(vm, gpr, fpr, _):
    global trace
    global early_exit

    if early_exit:
        return

    inst = vm.getInstAnalysis(pyqbdi.ANALYSIS_INSTRUCTION)

    if not (image_start <= inst.address and inst.address < image_stop):
        return

    addr = inst.address - image_start

    # If we still have branches to follow
    if trace:
        # If we are in an interesting branch
        if addr in interesting:
            # If we got it right, remove it from the branches to follow
            # Otherwise, we failed
            if addr == trace[0]:
                trace = trace[1:]
            else:
                early_exit = 1
    else:
        print "WIN"
        early_exit = 1


def pyqbdipreload_on_run(vm, start, stop):
    global image_start, image_stop

    # First mapped range should be ourself's .text
    text = pyqbdi.getCurrentProcessMaps()[0]
    image_start = text.range[0]
    image_stop  = text.range[1]

    # Add the callback and run
    vm.addCodeCB(pyqbdi.PREINST, mycb, None)
    vm.run(start, stop)

    # Print guess fitness for other script
    print 'OUT', len(trace)

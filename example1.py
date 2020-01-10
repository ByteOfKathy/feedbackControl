import random

class Buffer:
    def __init__(self, max_wip, max_flow):
        self.queued = 0
        self.wip = 0 # ready pool

        self.max_wip = max_wip
        self.max_flow = max_flow

# Adds to ready pool, then queue, then downstream process
def work(self, u):
    # ready pool
    u = max(0, int(round(u)))
    u = min(u, self.max_wip)
    self.wip += u

    # queue
    r = int(round(random.uniform(0, self.wip)))
    self.wip -= r
    self.queued += r

    # downstream
    r = int(round(random.uniform(0, self.max_flow)))
    r = min(r, self.queued)
    self.queued -= r

    return self.queued
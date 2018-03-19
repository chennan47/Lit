# /**
# * Design a data structure to hold objects with a corresponding integer weight. It should support:
# Obtain an object randomly with probability equal to
# (weight of the element) / (sum of the weights).
# Set an object-weight pair. If the object is already in the structure, its weight will
# be updated. Otherwise, the object will be inserted and set to its weight. If the weight is zero, the object can be removed.
# put("A",3) 3/33 put("B",30) 30/33 *
# */

import random


def weighted_choice(choices):
    total = sum(w for c, w in choices)
    r = random.uniform(0, total)
    upto = 0
    for c, w in choices:
        if upto + w >= r:
            return c
        upto += w
    assert False, "Shouldn't get here"

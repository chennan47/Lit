# Random iterator dividable by 5
# Be clear what to remove and when to remove them!
class Iterator(object):
    def __init__(self, nums):
        self.nums = nums
        self.x = 0
        self.y = 0
        self.last_return = None

    def hasNext(self):
        while self.x < len(self.nums) and \
              self.y >= len(self.nums[self.x]):
            self.x += 1
            self.y = 0
        return self.x < len(self.nums) and self.y < len(self.nums[self.x])

    def next(self):
        if self.hasNext():
            val = self.nums[self.x][self.y]
            self.last_return = (self.x, self.y)
            self.y += 1
            return val
        else:
            raise Exception('No more values')

    def remove(self):
        if self.last_return:
            x, y = self.last_return
            self.last_return = None
            self.nums[x].pop(y)
            self.x, self.y = x, y
        else:
            raise Exception('None couldn\'t be removed')


# bool hasNext() {
#         # Either way is okay, hasNext() or next()
#         while (self.n % 5 != 0 and Iterator::hasNext()) {
#             self.n = Iterator::hasNext();
#         }
#         return self.n % 5 == 0;
#     }
#     int next() {
#         if (!hasNext())
#             throw runtime_error("no more elements!");
#
#         val = self.n
#
#         self.n = INIT_VAL # not equal to n * 5
#
#         return val;
#     }
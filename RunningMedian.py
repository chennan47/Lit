#295. Find Median from Data Stream
# Median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value.
# So the median is the mean of the two middle value.
#
# Examples:
# [2,3,4] , the median is 3
#
# [2,3], the median is (2 + 3) / 2 = 2.5
#
# Design a data structure that supports the following two operations:
#
# void addNum(int num) - Add a integer number from the data stream to the data structure.
# double findMedian() - Return the median of all elements so far.
# For example:
#
# addNum(1)
# addNum(2)
# findMedian() -> 1.5
# addNum(3)
# findMedian() -> 2

# I keep two heaps (or priority queues):
#
# Max-heap small has the smaller half of the numbers.
# Min-heap large has the larger half of the numbers.
#
# This gives me direct access to the one or two middle values (they’re the tops of the heaps),
# so getting the median takes O(1) time. And adding a number takes O(log n) time.

#然后补充说如果内存不够存stream可以用reservoir sampling     sample一个subset来估算

# Supporting both min- and max-heap is more or less cumbersome, depending on the language,
# so I simply negate the numbers in the heap in which I want the reverse of the default order.
# To prevent this from causing a bug with -231 (which negated is itself, when using 32-bit ints),
# I use integer types larger than 32 bits.
#
# Using larger integer types also prevents an overflow error when taking the mean of the two middle numbers.
# I think almost all solutions posted previously have that bug.


from heapq import *


class MedianFinder:

    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0

import math


#Average and Standard Deviation:
class RollingStatistic(object):

    def __init__(self, window_size, average, variance):
        self.N = window_size
        self.average = average
        self.variance = variance
        self.stddev = math.sqrt(self.variance)

    def update(self, new, old):
        oldavg = self.average
        newavg = oldavg + (new - old)/self.N
        self.average = newavg
        self.variance += (new-old)*(new-newavg+old-oldavg)/(self.N-1)
        self.stddev = math.sqrt(self.variance)

# public class RunningStatDemo {
#
#   public static void main(String[] args) {
#
#     RunningStatDemo rsd = new RunningStatDemo();
#     rsd.go();
#   }
#
#   private void go() {
#
#     RunningStat rs = new RunningStat();
#     rs.put(1);
#     System.out.println("ave: " + rs.getAverage());
#     System.out.println("std: " + rs.getStandardDeviation());
#
#     rs.put(1);
#     System.out.println("ave: " + rs.getAverage());
#     System.out.println("std: " + rs.getStandardDeviation());
#
#     rs.put(10);
#     System.out.println("ave: " + rs.getAverage());
#     System.out.println("std: " + rs.getStandardDeviation());
#
#     rs.put(20);
#     System.out.println("ave: " + rs.getAverage());
#     System.out.println("std: " + rs.getStandardDeviation());
#
#     rs.put(50);
#     System.out.println("ave: " + rs.getAverage());
#     System.out.println("std: " + rs.getStandardDeviation());
#
#     rs.put(50);
#     System.out.println("ave: " + rs.getAverage());
#     System.out.println("std: " + rs.getStandardDeviation());
#   }
#
#   public class RunningStat {
#
#     private int count = 0;
#     private double average = 0.0;
#     private double pwrSumAvg = 0.0;
#     private double stdDev = 0.0;
#
#     /**
#      * Incoming new values used to calculate the running statistics
#      *
#      * @param value
#      */
#     public void put(double value) {
#
#       count++;
#       average += (value - average) / count;
#       pwrSumAvg += (value * value - pwrSumAvg) / count;
#       stdDev = Math.sqrt((pwrSumAvg * count - count * average * average) / (count - 1));
#
#     }
#
#     public double getAverage() {
#
#       return average;
#     }
#
#     public double getStandardDeviation() {
#
#       return Double.isNaN(stdDev) ? 0.0 : stdDev;
#     }
#
#   }
#
# }

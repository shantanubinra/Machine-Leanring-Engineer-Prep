#https://www.codingninjas.com/studio/problems/count-ways-to-reach-nth-stairs_798650?utm_source=youtube&utm_medium=affiliate&utm_campaign=love_babbar_10

"""find the number of ways to reach the to of stairs when you can tae only 1 or 2 steps each time"""

from os import *
from sys import *
from collections import *
from math import *
import sys

def countDistinctWays(nStairs: int) -> int:
    #  Write your code here.
    if nStairs==0:
        return 1
    if nStairs<0:
        return 0
    return countDistinctWays(nStairs-1)+countDistinctWays(nStairs-2)
# def main():
#     nStairs = int(sys.argv[1])
#     print("Number of ways to reach top are",countDistinctWays(nStairs))


if __name__=="__main__":
    nStairs = int(sys.argv[1])
    print("Number of ways to reach top are",countDistinctWays(nStairs))






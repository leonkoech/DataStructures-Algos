# Question 1:

# Consider the following class:


# class Point {

#     constructor(x, y) {

#         this.x = x;

#         this.y = y;

#     }

# }


# Write a function that takes an array of Points and logs to the console the bounds of the smallest upright rectangle which encloses all the points.  For example, given the points (-1, 0), (2, 2), (1,3) the function should print:

# Bottom-left: (-1, 0)

# Top-right: (2,3)


# Question 2:

# Write a function to convert the [red, green, blue] values of a colour into the corresponding HTML hex values.  Each red/green/blue value is in the range 0 to 255.  For example given red=68, green=58, blue=197 the function should return “#443ac5”


# Question 3:

# Write a function that takes an array of unordered integers and logs values at the 25th, 50th, 75th, 90th, 95th, 99th, and 100th percentiles.  For example, given the list [8, 6, 6, 20, 9, 1, 12, 16, 3, 16, 22, 2] it should log the following:


# 25% of the numbers are less than or equal to 3

# 50% of the numbers are less than or equal to 8

# 75% of the numbers are less than or equal to 16

# 90% of the numbers are less than or equal to 20

# 95% of the numbers are less than or equal to 22

# 99% of the numbers are less than or equal to 22

# 100% of the numbers are less than or equal to 22


class Point:
    def __init__(self,x=None,y=None):
        self.x=x
        self.y=y

p1=Point(-1,0)
p2=Point(2,2)
p3=Point(1,3)

points=[p1,p2,p3]
def rgb(num):
    return '%02x%02x%02x' % num
def find(arr):
    hx,hy=0,0
    lx=ly=0
    if not arr:
        return

    for i in range(len(arr)):
        hx=max(hx,arr[i].x)
        hy=max(hy,arr[i].y)
        lx=min(lx,arr[i].x)
        ly=min(ly,arr[i].y)
    print(lx,ly)
    print(hx,hy)

def percentiles(nums):
    #  [8, 6, 6, 20, 9, 1, 12, 16, 3, 16, 22, 2]
#      [1, 2, 3, 6, 6, 8, 9, 12, 16, 16, 20, 22]
#                     p1
#                           p2
# create percentiles
    nums.sort(reverse=True)
    n=len(nums)
    set = [25,50,75,90,95,99,100]
    
    for i in range(len(set)):
        mul=set[i]/100
        if mul>0.9 and mul<1:
            print(set[i],nums[-int(n*mul)])
        else:
            print(set[i],nums[-int(n*mul)-1])
        # print(i,nums[int(n*i)])
    # print(set[-1],nums[:-1])
if __name__=="__main__":
    percentiles([8,6,6,20,9,1,12,16,3,16,22,2])



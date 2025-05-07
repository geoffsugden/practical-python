# bounce.py
#
# Exercise 1.5

num_bounces = 0
height = 100 # Initial height in meters

while num_bounces < 10:
    num_bounces += 1
    height = height * 0.6 
    print(num_bounces, round(height,4))
###############################################################################################################
# Common Charting Problem:
# When looking at a century of data entries that vary wildly year to year, and often have holes or spikes
# in the data, charts can become jagged and difficult to draw conclusions from.
#
# The Typical Solution:
# Place data in arbitrarily sized bins. This can lead to a loss of sensitivity and confusion over what
# is happening within or at the edges of the bin.
#
# This Project's Solution
# This project takes a list of data, preserves the first and last entry, and rounds all other points
# with the surrounding data
#
# Disclaimer:
# This project was initially inspired by a sample project on Code Abbey (#57, smoothing the weather)
# They have requested that users not put the problems on GitHub. This project has been significantly changed
# to serve the purposes of a chart in my doctoral dissertation.
################################################################################################################

# To prepare your data, lay out your data points with a space as separator. The output will be similarly printed.

# Enter your space-separated data
input_values = input().split(' ')

# Turns data into floats
original_list = [float(x) for x in input_values]

# Initialize the output list with the first original value. Initialize a counter for list position.
smoothed_list = [original_list[0]]
counter = 0

# Round each item from 2nd to penultimate with it's preceding and following entry from the input list.
# Append to output list.
for x in original_list[1:-1]:
    counter += 1
    smoothed_list.append((original_list[counter - 1] + original_list[counter] + original_list[counter + 1])/3.0000000)

# Add the last entry to finish output list.
smoothed_list.append(original_list[-1])

# Print results
for x in smoothed_list:
    print(x)

# NOTE: I chose to print out the results like this and re-enter the data into excel, where I did most of my analysis.
# This code could be easily modified to change the input and output style, or even produce
# a PyPlot chart from the code directly. I chose not to for my own purposes.
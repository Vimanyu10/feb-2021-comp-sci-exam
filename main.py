""" 
5th Year Computer Science February Assessment 2021
Name: Vimanyu Taneja
"""

"""NOTE"""
# There is a list of functions at the end of the code, which can be used for testing by simply uncommenting and commenting the functions accordingly.

"""Modules"""
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np
import math
import statistics

"""Given data"""

# Part 1
day_one_temp = [4.5,4.2,4,3.2,2.5,1.9,2.8,3,2.3,1.7,2,3.6,4.5,5,5.7,5.4,5.1,4.3,3.1,3,2.5,1.7,1.5,1.2] # 29/12/2020
day_two_temp = [1.1,0.6,0.1,0.3,0.4,0.8,1.3,1.4,1.3,1.3,1.4,1.7,1.9,2.6,2.2,2.8,2.1,0.7,0,-0.3,-0.6,-1.1,-1.2,-1.5] # 30/12/2020
day_three_temp = [-1.4,-1.4,-1.3,-1.5,-1.6,-1.2,-1.5,-1.4,-0.6,-0.4,0.3,0.7,1.9,2.5,2.1,2.4,2.1,2.4,3.2,3.9,4.2,4.4,4.4,4.5] # 31/12/2020
# Assumption: Each of the 24 items in the above lists of temperature represents the average temperature over the period of the correpsonding hour of the day
# For example, day_one_temp[0] represents the average temperature betwwen 00:00 and 00:59 on the 29th of December, 2020.

# Part 2
day_one_rainfall = [0,0,0.1,0.3,0,0.1,0.2,0.6,1.1,3.4,0.7,0,0,0,0,0,0,0,0,0.5,2.2,1.3,0.3,0] # 29/12/2020
day_two_rainfall = [0,0,0,0,0,0,0,0.1,0.5,0.2,0,0,0.1,0.3,1.7,0.9,0.4,0.1,0,0,0,0,0,0] # 30/12/2020
day_three_rainfall = [0.3,0.2,0.1,1.3,0,0,0.6,0,0.1,0.2,0.3,0.4,2.4,0,0,0.5,0,0.1,0,0.8,0.1,0,0.1,0.8] # 31/12/2020

"""Solution"""

def part1_question1():

  figure, (day1_axes, day2_axes, day3_axes) = plt.subplots(3, figsize=(7.5,7.5), facecolor="oldlace")
  figure.suptitle("Temperature from 29th to 31st December 2020", fontsize=15, weight="bold", x=0.5, y=0.965) # The 'x' and 'y' arguments set the x and y co-rodinates of the centre of the title, relative to a coordinate system of the figure where the width(x-axis) of the figure is 1 unit and the height(y-axis) of the figure is 1 unit.

  xvalues = [hour+0.5 for hour in range (24)] # The +0.5 is used to conform with the assumption that the given temperatures represent the average temperature over the duration of a given hour, so we will plot each value at the middle of the correpsonding hour, i.e. at every hh:30.

  linewidth_for_plots = 3
  weight_for_subplot_titles = "bold"

  day1_axes.plot(xvalues, day_one_temp, "royalblue", linewidth=linewidth_for_plots)
  day1_axes.set_title("29th December 2020", weight=weight_for_subplot_titles)

  day2_axes.plot(xvalues, day_two_temp, "orange", linewidth=linewidth_for_plots)
  day2_axes.set_title("30th December 2020", weight=weight_for_subplot_titles)

  day3_axes.plot(xvalues, day_three_temp, "green", linewidth=linewidth_for_plots)
  day3_axes.set_title("31st December 2020", weight=weight_for_subplot_titles)

  plt.subplots_adjust(top=0.85, hspace=0.7)
  # top=0.85 adjusts the subplots so that there is a distance equivalent to 85% of the entire figure's height between the top edge of the top axes(day1_axes) and the bottom edge of the entire figure.
  # hspace=0.7 adjusts the subplots so that there is a distance equivalent to 70% of the average of all three subplot's heights between each subplot.

  # The major xticks are only every four hours to prevent the labels from being too close together.
  xticks = []
  hours_xticks_labels = []
  for i in range (6):
    xticks.append(i*4)
    hours_xticks_labels.append(str(i*4) + ":00")
    if (len(hours_xticks_labels[i])) < 5:
      hours_xticks_labels[i] = "0" + hours_xticks_labels[i]
  xticks.append(24)
  hours_xticks_labels.append("00:00")

  overall_max_temp = max(max(day_one_temp), max(day_two_temp), max(day_three_temp))
  overall_min_temp = min(min(day_one_temp), min(day_two_temp), min(day_three_temp))
  yticks = np.arange(start=math.floor(overall_min_temp)-2, stop=math.ceil(overall_max_temp)+2.1, step=2) # The '.1' component of '+2.1' ensures that there is a tick at y=math.ceil(overall_max_temp)+2, as the np.arange() function does not include the stop number in the result if it is equal to the start value plus some multiple of the step value. Therefore, if we set stop=math.ceil(overall_max_temp)+2, then there would be no tick at y=max.ceil(overall_max_temp)+2 as this value is some multiple of the step value, 2, greater than the start value, math.floor(overall_min_temp)-2, so it would lie perfectly as the final value in the range and therefore be omitted.

  subplots = (day1_axes, day2_axes, day3_axes)
  for axes in subplots:
    plt.minorticks_on()
    axes.set(xlim=(0,24), ylim=(overall_min_temp-2,overall_max_temp+2))
    axes.set_xlabel("Time", weight="bold")
    axes.set_ylabel("Temperature (" + "\u00b0" + "C)", weight="bold") # "\u00b0" represents the degrees symbol (°).
    axes.grid(which="major", axis="both", color="black", linestyle="-", linewidth=1, alpha=0.4)
    axes.grid(which="minor", axis="both", color="grey", linestyle="--", linewidth=1, alpha=0.3)

    plt.sca(axes) # This selects each axes individually before setting xticks and yticks because an axes object itself does not have the attributes 'xticks' and 'yticks'.
    plt.xticks(ticks=xticks, labels=hours_xticks_labels)
    plt.yticks(yticks)

  plt.savefig("part1_question1.png")
  plt.show()

def part1_question2():

  plt.figure(figsize=(7.5,7.5), facecolor="oldlace")
  plt.title("Temperature from 29th to 31st December 2020", fontsize=17.5, weight="bold", pad=20)

  xvalues = [hour+0.5 for hour in range (24)] # The +0.5 is used to conform with the assumption that the given temperatures represent the average temperature over the duration of a given hour, so we will plot each value at the middle of the correpsonding hour, i.e. at every hh:30.

  linewidth_for_plots = 3
  plt.plot(xvalues, day_one_temp, label="29th December 2020", color="royalblue", linewidth=linewidth_for_plots)
  plt.plot(xvalues, day_two_temp, label="30th December 2020", color="orange", linewidth=linewidth_for_plots)
  plt.plot(xvalues, day_three_temp, label="31st December 2020", color="green", linewidth=linewidth_for_plots)

  overall_max_temp = max(max(day_one_temp), max(day_two_temp), max(day_three_temp))
  overall_min_temp = min(min(day_one_temp), min(day_two_temp), min(day_three_temp))
  yticks = np.arange(start=math.floor(overall_min_temp)-2, stop=math.ceil(overall_max_temp)+2.1)

  # The major xticks are only every four hours to prevent the labels from being too close together.
  xticks = []
  hours_xticks_labels = []
  for i in range (6):
    xticks.append(i*4)
    hours_xticks_labels.append(str(i*4) + ":00")
    if (len(hours_xticks_labels[i])) < 5:
      hours_xticks_labels[i] = "0" + hours_xticks_labels[i]
  xticks.append(24)
  hours_xticks_labels.append("00:00")

  plt.minorticks_on()
  plt.xlim = (0, 24)
  plt.ylim = (overall_min_temp-2, overall_max_temp+2)

  plt.xlabel("Time", weight="bold", fontsize=15, labelpad=10)
  plt.ylabel("Temperature (" + "\u00b0" + "C)", weight="bold", fontsize=15) # "\u00b0" represents the degrees symbol (°)
  plt.xticks(ticks=xticks, labels=hours_xticks_labels)
  plt.yticks(yticks)

  plt.grid(which="major", axis="both", color="black", linestyle="-", linewidth=1, alpha=0.4)
  plt.grid(which="minor", axis="both", color="grey", linestyle="--", linewidth=1, alpha=0.3)
  plt.legend(loc="upper left", fontsize=12.5, shadow=True, bbox_to_anchor=(0.025, 0.975), facecolor="oldlace") # loc="upper left" positions the legend at the top-left corner of the axes. bbox_to_anchor=(0.025,0.975) makes this positioning more precise, placing the top-left corner of the legend 2.5% of the axes' total width to the right and 97.5% of the axes' total height upwards from the bottom-left corner of the axes. These values are essentially arbitrary, as I found them to best fit the legend on the figure through trial-and-error.

  plt.savefig("part1_question2.png")
  plt.show()

def part1_question3():
 
  figure, axes = plt.subplots(figsize=(7.5,7.5), facecolor="oldlace")
  plt.title("Average temperature from 29th to 31st December 2020", fontsize=13, weight="bold", pad=20)

  average_temp_day1 = statistics.mean(day_one_temp)
  average_temp_day2 = statistics.mean(day_two_temp)
  average_temp_day3 = statistics.mean(day_three_temp)

  bar_plot = plt.bar(["29th December 2020", "30th December 2020", "31st December 2020"], [average_temp_day1, average_temp_day2, average_temp_day3], color=("royalblue", "orange", "green"), linewidth=2, edgecolor="black")

  degrees_celsius_symbol = "\u00b0" + "C"
  plt.xlabel("Date", weight="bold", fontsize=15, labelpad=10)
  plt.ylabel("Temperature (" + degrees_celsius_symbol + ")", weight="bold", fontsize=15)

  for bar in bar_plot:
    height_of_bar = round(bar.get_height(), 2)
    num_of_decimal_places_of_height_of_bar = len(str(round(height_of_bar - math.floor(height_of_bar), 2))) - 2 # Although 'height_of_bar' should have 2 digits after the decimal point as it was set as a value rounded to 2 decimal places, the function 'round' omits any 0s at the end of the number to be returned, so the actual number of digits after the decimal point in 'height_of_bar' may be less than 2.

    # This if-else statement ensures that the text label on every bar has 2 digits after the decimal point, as this consistency is aesthetically pleasing.
    if num_of_decimal_places_of_height_of_bar == 2:
      average_temp_bar_text_label = str(height_of_bar) + degrees_celsius_symbol
    else:
      for i in range (2 - num_of_decimal_places_of_height_of_bar):
        average_temp_bar_text_label = str(height_of_bar) + "0" + degrees_celsius_symbol

    # Adds a text label on each bar to display the average temperature each day.
    plt.text(bar.get_x() + bar.get_width()/2, 0.25, average_temp_bar_text_label, horizontalalignment="center", verticalalignment="center", color="white", size=20, weight="bold")

  max_average_temp = max(average_temp_day1, average_temp_day2, average_temp_day3)
  yticks = np.arange(start=0, stop=math.ceil(max_average_temp) + 0.5, step=0.5)
  plt.yticks(yticks)

  plt.minorticks_on()
  axes.yaxis.set_minor_locator(MultipleLocator(0.1)) # Sets the minor ticks on the y-axis to be 0.1 units apart.
  plt.tick_params(axis = "x", which = "both", bottom = False, top = False)

  plt.grid(which="minor", axis="y", color="grey", linestyle="--", linewidth=1, alpha=0.3)
  plt.grid(which="major", axis="y", color="black", linestyle="-", linewidth=1, alpha=0.4)
  labels = ["29th December 2020", "30th December 2020", "31st December 2020"]
  plt.legend(bar_plot, labels, loc="upper right", fontsize=12.5, shadow=True, bbox_to_anchor=(0.975,0.975), facecolor="oldlace") # loc="upper right" positions the legend at the top-right corner of the axes. bbox_to_anchor=(0.975,0.975) makes this positioning more precise, placing the top-right corner of the legend 97.5% of the axes' total width to the right and 97.5% of the axes' total height upwards from the bottom-left corner of the axes. These values are essentially arbitrary, as I found them to best fit the legend on the figure through trial-and-error.

  plt.savefig("part1_question3.png")
  plt.show()

def part1_question4():

  plt.figure(figsize=(7.5,7.5), facecolor="oldlace")

  plt.title("Range of temperature from 29th to 31st December 2020", fontsize=13, weight="bold", pad=20)
  
  min_temp_day1 = min(day_one_temp)
  max_temp_day1 = max(day_one_temp)
  range_temp_day1 = max_temp_day1 - min_temp_day1

  min_temp_day2 = min(day_two_temp)
  max_temp_day2 = max(day_two_temp)
  range_temp_day2 = max_temp_day2 - min_temp_day2

  min_temp_day3 = min(day_three_temp)
  max_temp_day3 = max(day_three_temp)
  range_temp_day3 = max_temp_day3 - min_temp_day3

  bar_plot = plt.bar(["29th December 2020", "30th December 2020", "31st December 2020"], [range_temp_day1, range_temp_day2, range_temp_day3], color=("royalblue", "orange", "green"), bottom=[min_temp_day1, min_temp_day2, min_temp_day3], linewidth=2, edgecolor="black")

  list_of_temp_ranges = [range_temp_day1, range_temp_day2, range_temp_day3]
  list_of_min_values = [min_temp_day1, min_temp_day2, min_temp_day3]
  list_of_max_values = [max_temp_day1, max_temp_day2, max_temp_day3]
  index = 0
  degrees_celsius_symbol = "\u00b0" + "C"
  for bar in bar_plot:
    # We canot use 'bar' to specify an index as 'bar' represents a 'bar' object, i.e. a bar in the bar graph, not a number.
    current_day_temp_range = list_of_temp_ranges[index]
    range_label = str(round(current_day_temp_range,2)) + degrees_celsius_symbol
    min_label = str(list_of_min_values[index]) + degrees_celsius_symbol
    max_label = str(list_of_max_values[index]) + degrees_celsius_symbol

    # Adds a text label on each bar to display the range of temperatures each day.
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_y() + current_day_temp_range/2, range_label, horizontalalignment="center", verticalalignment="center", color="white", size=20, weight="bold")

    # Adds a text label on each bar to display the minimum temperature each day.
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_y() + 0.3, min_label, horizontalalignment="center", verticalalignment="center", color="white", size=15, weight="bold")

    # Adds a text label on each bar to display the maximum temperature each day.
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_y() + current_day_temp_range - 0.35, max_label, horizontalalignment="center", verticalalignment="center", color="white", size=15, weight="bold")

    index += 1

  plt.xlabel("Date", weight="bold", fontsize=15, labelpad=10)
  plt.ylabel("Temperature (" + degrees_celsius_symbol + ")", weight="bold", fontsize=15)

  overall_max_temp = max(max_temp_day1, max_temp_day2, max_temp_day3)
  overall_min_temp = min(min_temp_day1, min_temp_day2, min_temp_day3)
  yticks = np.arange(start=math.floor(overall_min_temp)-2, stop=math.ceil(overall_max_temp)+3)
  plt.yticks(yticks)
  plt.minorticks_on()
  plt.xlim = (0, 24)
  plt.ylim = (overall_min_temp-1, overall_max_temp+1)

  plt.grid(which="major", axis="y", color="black", linestyle="-", linewidth=1, alpha=0.4)
  plt.minorticks_on()
  plt.tick_params(axis = "x", which = "both", bottom = False, top = False)
  plt.grid(which="minor", axis="y", color="grey", linestyle="--", linewidth=1, alpha=0.3)

  labels = ["29th December 2020", "30th December 2020", "31st December 2020"]
  plt.legend(bar_plot, labels, loc="upper right", fontsize=12.5, shadow=True, bbox_to_anchor=(0.975,0.975), facecolor="oldlace") # loc="upper right" positions the legend at the top-right corner of the axes. bbox_to_anchor=(0.975,0.975) makes this positioning more precise, placing the top-right corner of the legend 97.5% of the axes' total width to the right and 97.5% of the axes' total height upwards from the bottom-left corner of the axes. These values are essentially arbitrary, as I found them to best fit the legend on the figure through trial-and-error.

  plt.savefig("part1_question4.png")
  plt.show()

def part2_question1():

  figure, (day1_axes, day2_axes, day3_axes) = plt.subplots(3, figsize=(7.5,7.5), facecolor="oldlace")
      
  figure.suptitle("Rainfall from 29th to 31st December 2020", fontsize=15, weight="bold", x=0.5, y=0.965) # The 'x' and 'y' arguments set the x and y co-rodinates of the centre of the title, relative to a coordinate system of the figure where the width(x-axis) of the figure is 1 unit and the height(y-axis) of the figure is 1 unit.

  xvalues = [hour+0.5 for hour in range (24)] # The +0.5 is used to conform with the assumption that each item in the given data lists of rainfall represents the total rainfall over the duration of an hour, so we will plot each value at the middle of the correpsonding hour, i.e. at every hh:30, to allow for this fact.

  linewidth_for_plots = 3
  weight_for_subplot_titles = "bold"

  day1_axes.plot(xvalues, day_one_rainfall, "royalblue", linewidth=linewidth_for_plots)
  day1_axes.set_title("29th December 2020", weight=weight_for_subplot_titles)

  day2_axes.plot(xvalues, day_two_rainfall, "orange", linewidth=linewidth_for_plots)
  day2_axes.set_title("30th December 2020", weight=weight_for_subplot_titles)

  day3_axes.plot(xvalues, day_three_rainfall, "green", linewidth=linewidth_for_plots)
  day3_axes.set_title("31st December 2020", weight=weight_for_subplot_titles)

  plt.subplots_adjust(top=0.85, hspace=0.7)
  # top=0.85 adjusts the subplots so that there is a distance equivalent to 85% of the entire figure's height between the top edge of the top axes(day1_axes) and the bottom edge of the entire figure.
  # hspace=0.7 adjusts the subplots so that there is a distance equivalent to 70% of the average of all three subplot's heights between each subplot.

  max_rainfall = max(max(day_one_rainfall), max(day_two_rainfall), max(day_three_rainfall))
  yticks = np.arange(start=0, stop=math.ceil(max_rainfall)+0.1, step=1) # '+0.1' ensures that there is a tick at y=math.ceil(max_rainfall), as the np.arange() function does not include the stop number in the result if it is equal to the start value plus some multiple of the step value. Therefore, if we set stop=math.ceil(max_rainfall), then there would be no tick at y=max.ceil(max_rainfall) as this value is an integer greater than the start value, 0, so with a step of 1 it would lie perfectly as the final value in the range and therefore be omitted.

  # The major xticks are only every four hours to prevent the labels from being too close together.
  xticks = []
  hours_xticks_labels = []
  for i in range (6):
    xticks.append(i*4)
    hours_xticks_labels.append(str(i*4) + ":00")
    if (len(hours_xticks_labels[i])) < 5:
      hours_xticks_labels[i] = "0" + hours_xticks_labels[i]
  xticks.append(24)
  hours_xticks_labels.append("00:00")

  plots = (day1_axes, day2_axes, day3_axes)
  for plot in plots:
    plt.minorticks_on()
    plot.set(xlim=(0,24), ylim=(0,math.ceil(max_rainfall)))
    plot.set_xlabel("Time", weight="bold")
    plot.set_ylabel("Rainfall (cm)", weight="bold")
    plot.grid(which="major", axis="both", color="black", linestyle="-", linewidth=1, alpha=0.4)
    plot.grid(which="minor", axis="both", color="grey", linestyle="--", linewidth=1, alpha=0.3)

    plt.sca(plot) # This selects each axes individually before setting xticks and yticks because an axes object itself does not have the attributes 'xticks' and 'yticks'.
    plt.xticks(ticks=xticks, labels=hours_xticks_labels)
    plt.yticks(yticks)

  plt.savefig("part2_question1.png")
  plt.show()

def part2_question2():

  plt.figure(figsize=(7.5,7.5), facecolor="oldlace")
  plt.title("Rainfall from 29th to 31st December 2020", fontsize=17.5, weight="bold", pad=20)

  xvalues = [hour+0.5 for hour in range (24)] # The +0.5 is used to conform with the assumption that each item in the given data lists of rainfall represents the total rainfall over the duration of an hour, so we will plot each value at the middle of the correpsonding hour, i.e. at every hh:30, to allow for this fact.

  linewidth_for_plots = 3
  plt.plot(xvalues, day_one_rainfall, label="29th December 2020", color="royalblue", linewidth=linewidth_for_plots)
  plt.plot(xvalues, day_two_rainfall, label="30th December 2020", color="orange", linewidth=linewidth_for_plots)
  plt.plot(xvalues, day_three_rainfall, label="31st December 2020", color="green", linewidth=linewidth_for_plots)

  max_rainfall = max(max(day_one_rainfall), max(day_two_rainfall), max(day_three_rainfall))
  yticks = np.arange(start=0, stop=math.ceil(max_rainfall)+0.5, step=0.5)

  # The major xticks are only every four hours to prevent the labels from being too close together.
  xticks = []
  hours_xticks_labels = []
  for i in range (6):
    xticks.append(i*4)
    hours_xticks_labels.append(str(i*4) + ":00")
    if (len(hours_xticks_labels[i])) < 5:
      hours_xticks_labels[i] = "0" + hours_xticks_labels[i]
  xticks.append(24)
  hours_xticks_labels.append("00:00")

  plt.minorticks_on()
  plt.xlim = (0, 24)
  plt.ylim = (0, math.ceil(max_rainfall)+0.5)
  plt.xlabel("Time", weight="bold", fontsize=15, labelpad=10)
  plt.ylabel("Rainfall (cm)", weight="bold", fontsize=15)
  plt.xticks(ticks=xticks, labels=hours_xticks_labels)
  plt.yticks(yticks)

  plt.grid(which="major", axis="both", color="black", linestyle="-", linewidth=1, alpha=0.4)
  plt.grid(which="minor", axis="both", color="grey", linestyle="--", linewidth=1, alpha=0.3)
  plt.legend(loc="upper left", fontsize=12.5, shadow=True, bbox_to_anchor=(0.5, 0.975), facecolor="oldlace") # loc="upper left" positions the legend at the top-left corner of the axes. bbox_to_anchor=(0.5,0.975) makes this positioning more precise, placing the top-left corner of the legend 50% of the axes' total width to the right and 97.5% of the axes' total height upwards from the bottom-left corner of the axes. These arguments have the net effect of placing the legend near the middle(50%) of the axes in the horizontal direction, and near the top(97.5%) of the axes in the vertical direction, although the legend is slightly to the right as loc="upper left" pushes the legend to the right slightly. These values are essentially arbitrary, as I found them to best fit the legend on the figure through trial-and-error.

  plt.savefig("part2_question2.png")
  plt.show()

def part2_question3():

  figure, ax = plt.subplots(figsize=(7.5,7.5), facecolor="oldlace")

  plt.title("Total daily rainfall from 29th to 31st December 2020", fontsize=15, weight="bold", pad=20)

  total_rainfall_day1 = sum(day_one_rainfall)
  total_rainfall_day2 = sum(day_two_rainfall)
  total_rainfall_day3 = sum(day_three_rainfall)
  
  bar_plot = plt.bar(["29th December 2020", "30th December 2020", "31st December 2020"], [total_rainfall_day1, total_rainfall_day2, total_rainfall_day3], color=("royalblue", "orange", "green"), linewidth=2, edgecolor="black")

  plt.xlabel("Date", weight="bold", fontsize=15, labelpad=10)
  plt.ylabel("Rainfall (cm)", weight="bold", fontsize=15)

  max_total_rainfall = max(total_rainfall_day1, total_rainfall_day2, total_rainfall_day3)
  yticks = np.arange(start=0, stop=math.ceil(max_total_rainfall) + 1)
  plt.yticks(yticks)

  for bar in bar_plot:
    height_of_bar = bar.get_height()
    total_rainfall_bar_text_label = str(round(height_of_bar,2)) + "cm"

    # Adds a text label on each bar to display the total rainfall each day.
    plt.text(bar.get_x() + bar.get_width()/2, 0.45, total_rainfall_bar_text_label, horizontalalignment="center", verticalalignment="center", color="white", size=20, weight="bold")

  plt.grid(which="major", axis="y", color="black", linestyle="-", linewidth=1, alpha=0.4)

  plt.minorticks_on()
  ax.yaxis.set_minor_locator(MultipleLocator(0.1)) # MultipleLocator(0.1) sets the minor ticks on the y-axis to be 0.1 units apart.
  plt.tick_params(axis = "x", which = "both", bottom = False, top = False)
  plt.grid(which="minor", axis="y", color="grey", linestyle="--", linewidth=1, alpha=0.3)

  labels = ["29th December 2020", "30th December 2020", "31st December 2020"]
  plt.legend(bar_plot, labels, loc="upper right", fontsize=12.5, shadow=True, bbox_to_anchor=(0.96,0.96), facecolor="oldlace") # loc="upper right" positions the legend at the top-right corner of the axes. bbox_to_anchor=(0.96, 0.96) makes this positioning more precise, placing the top-right corner of the legend 96% of the axes' total width to the right and 96% of the axes' total height upwards from the bottom-left corner of the axes. These values are essentially arbitrary, as I found them to best fit the legend on the figure through trial-and-error.

  plt.savefig("part2_question3.png")
  plt.show()

def part2_question4():

  figure, ax = plt.subplots(figsize=(7.5,7.5), facecolor="oldlace")

  plt.title("Total daily rainfall from\n29th to 31st December 2020", fontsize=20, weight="bold", y=0.95, pad=5)

  total_rainfall_day1 = round(sum(day_one_rainfall),2)
  total_rainfall_day2 = round(sum(day_two_rainfall),2)
  total_rainfall_day3 = round(sum(day_three_rainfall),2)

  wedge_labels = [str(total_rainfall_day1) + "cm", str(total_rainfall_day2) + "cm", str(total_rainfall_day3) + "cm"]

  wedges, labels = plt.pie([total_rainfall_day1, total_rainfall_day2, total_rainfall_day3], labels=wedge_labels, textprops=dict(color="white", size=25, weight="bold"), colors=("royalblue", "orange", "green"), labeldistance=0.55, center=(2,2), startangle=157, radius=1.35, shadow=True, wedgeprops = {"linewidth":2, "edgecolor":"black" }) # The 'startangle' parameter determines the angle in degrees counterclockwise from the positive sense of the x-axis from where the first wedge of the pie chart begins. startangle=157 is an essentially arbitrary angle that presents the wedge labels in the most suitable manner, as determined by trial-and-error.

  ax.set_ylim(0,3.7) # This re-sizes the y-axis so that the pie chart best fits on the figure.
  
  for label in labels:
    label.set_horizontalalignment("center")

  legend_values = ["29th December 2020", "30th December 2020", "31st December 2020"]
  plt.legend(labels=legend_values, fontsize=18, shadow=True, bbox_to_anchor=(0.975,0.15), facecolor="oldlace") # bbox_to_anchor=(0.025,0.975) places the top-right corner of the legend 97.5% of the axes' total width to the right and 15% of the axes' total height upwards from the bottom-left corner of the axes. As the length of the x-axis is determined by the width of the pie chart, and the length of the y-axis is slightly larger than the height of the pie chart, this has the net effect of placing the legend near the bottom edge of the figure, at the middle of the x-axis. These values are essentially arbitrary, as I found them to best fit the legend on the figure through trial-and-error.

  plt.savefig("part2_question4.png")
  plt.show()

def part2_question5():

  plt.figure(figsize=(7.5,7.5), facecolor="oldlace")
  plt.title("Total rainfall from 29th to 31st December\n2020 grouped by time of day", fontsize=17.5, weight="bold", pad=17.5)

  total_rainfall_by_hour = {}
  for hour in range (24):
    total_rainfall_by_hour[hour] = round(day_one_rainfall[hour] + day_two_rainfall[hour] + day_three_rainfall[hour], 2)

  hours = list(total_rainfall_by_hour.keys())
  rainfall_per_hour = list(total_rainfall_by_hour.values())

  xvalues = [hour+0.5 for hour in range (24)] # The +0.5 is used to conform with the assumption that each item in the given data lists of rainfall represents the total rainfall over the duration of an hour, so we will plot each value at the middle of the correpsonding hour, i.e. at every hh:30, to allow for this fact.
  plt.plot(xvalues, rainfall_per_hour, color="tab:red", linewidth=3)

  plt.xlabel("Time", weight="bold", fontsize=15, labelpad=10)
  plt.ylabel("Rainfall (cm)", weight="bold", fontsize=15)

  max_rainfall_per_hour = max(rainfall_per_hour)
  yticks = np.arange(start=0, stop=math.ceil(max_rainfall_per_hour) + 0.5, step=0.5)

  hours_labels = []
  xticks = []
  for hour in range(int(len(hours)/4)):
    xticks.append(hour*4)
    # This if-else statement ensures that the label for the hour at each major tick is in the form hh:mm and not h:mm.
    if hours[hour]*4 > 9:
      hours_labels.append(str(hours[hour]*4) + ":00")
    else:
      hours_labels.append("0" + str(hours[hour]*4) + ":00")
  hours_labels.append("00:00")
  xticks.append(24)

  plt.minorticks_on()
  plt.xlim = (0, 24)
  plt.ylim = (0, max_rainfall_per_hour+2)
  plt.xticks(ticks=xticks, labels=hours_labels)
  plt.yticks(yticks)

  plt.grid(which="major", axis="both", color="black", linestyle="-", linewidth=1, alpha=0.4)
  plt.grid(which="minor", axis="both", color="grey", linestyle="--", linewidth=1, alpha=0.3)

  plt.savefig("part2_question5.png")
  plt.show()

"""Functions"""
part1_question1()
part1_question2()
part1_question3()
part1_question4()
part2_question1()
part2_question2()
part2_question3()
part2_question4()
part2_question5()
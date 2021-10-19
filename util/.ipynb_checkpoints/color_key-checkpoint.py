# C. Savonen 2021

import pandas as pd
import numpy as np
import random

# For making a legend
from matplotlib.patches import Patch
import matplotlib.pyplot as plt

def make_color_key(variable):
    """Creates color coding components for a pandas Series variable provided

    Args:
      variable: A pandas Series like metadata['exp_group']

    Returns:
      A dict with two entries: 
           'color_key_dict' has the dictionary of what group belongs to what color
           'color_key' has the pandas series variable recoded according to the 'color_key_dict'
    """
    # How many colors do we need?
    num_colors = len(variable.unique())
    
    # Retrieve this many colors
    colors = ["#"+''.join([random.choice('0123456789ABCDEF') for i in range(6)])
       for j in range(num_colors)]
    
    # Make color key dictionary for these groups
    color_key_dict = dict(zip(variable.unique(), colors))

    
    # Make into data frame where index is sample IDs
    color_key = pd.Series(variable.map(color_key_dict))
    
    return({"color_key_dict": color_key_dict, "color_key": color_key})


def make_legend(color_key_dict, title):
    """Creates color key legend for a dictionary provided 

    Args:
      color_key_dict: A dictionary obtained from make_color_key might look like metadata['refinebio_treatment']
      title: A string indicating the title for the legend.
    Returns:
      A legend on the plot that was last called.
    """

    # Set up based on color dictionary
    handles = [Patch(facecolor = color_key_dict[name]) for name in color_key_dict]
    
    # Make a legend for these color codes 
    plt.legend(handles, color_key_dict, title = title,
               bbox_to_anchor = (1, 1), bbox_transform = plt.gcf().transFigure, loc = 'upper right')
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 16:53:42 2017
@author: WANGQl
"""


import sys
from pandas import read_csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams


def plot_by_columns(datafile, fig_name):
    rcParams['axes.unicode_minus'] = False
    rcParams['xtick.direction'] = 'out'
    rcParams['ytick.direction'] = 'out'
    rcParams['font.sans-serif'] = ['STKaiti']
    rcParams['font.style'] = 'normal'
    rcParams['axes.edgecolor'] = 'k'
    rcParams['axes.linewidth'] = 1.0
    rcParams['axes.spines.right'] = True
    rcParams['xtick.major.size'] = 3.5
    rcParams['xtick.minor.width'] = 0.6
    rcParams['xtick.color'] = 'k'
    rcParams['pdf.fonttype'] = 42
    rcParams['ps.fonttype'] = 3
    rcParams['ps.usedistiller'] = False

    font1 = dict(family='STKaiti', color='red', weight='normal', size=12)

    df = read_csv(datafile
                     ,index_col=0
                     ,parse_dates=True)
    
    df[df==99999]=np.nan
    df = df.resample('3D').mean()
    title_list = df.columns.tolist()

    ax = df.plot(figsize=(12,10),
                 subplots=True,
                 linewidth=1.5,
                 sharex=False,
                 style='r-',
                 grid=True,
                 legend=False,
                 yticks=[],
                 title=title_list)
    plt.subplots_adjust(hspace=0.75)
    # plt.suptitle('ChaZhi', fontsize=16)
    for i in np.arange(0, 6):
        ax[i].set_xlabel('')
        ax[i].set_title(title_list[i], fontdict=font1)
    plt.savefig(fig_name, dpi=300, bbox_inches='tight')

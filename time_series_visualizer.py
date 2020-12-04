import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.) #✅
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=True, index_col='date')

# Clean data
bottom = df['value'] >= df['value'].quantile(0.025)
The_Top = df['value'] <= df['value'].quantile(0.975)
df = df[(bottom) & (The_Top)]


def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize = (30, 10))
    #  to modify the ticks, we will need to get axes object:
    ax = plt.subplot()
    plt.plot(
      df.index, 
      df.value,
      c = "r"
    )
    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019", fontsize = "16")
    plt.xlabel("Date", fontsize = "16")
    plt.ylabel("Page Views", fontsize = "16")
    ax.xaxis.set_major_locator(plt.MaxNLocator(9))

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar["year"] = pd.DatetimeIndex(df.index).year
    df_bar["month"] = pd.DatetimeIndex(df.index).month

    # Draw bar plot
    fig = plt.figure(figsize = (12, 10))
    sns.barplot(
    data = df_bar,
    x = "year",
    y = "value",
    hue = "month",
    ci = None,      # no bootstrapping will be performed, and error bars will not be drawn
    palette = "tab10"
    )
    plt.xlabel(
    "Years",
    fontsize = "16"
    )
    plt.ylabel(
    "Average Page Views",
    fontsize = "16"
    )
    plt.xticks(
    rotation = "vertical",
    fontsize = "16"
    )
    plt.yticks(fontsize = "16")
    plt.legend(
    loc = "upper left",
    title = "Months",
    title_fontsize = 16,
    fontsize = 16,
    labels = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    )
    
    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig = plt.figure(figsize = (15, 5))

    # how the values are distributed within a given year:
    plt.subplot(1, 2, 1)
    sns.boxplot(
      data = df_box,
      x = "year",
      y = "value"
    )
    plt.title("Year-wise Box Plot (Trend)")
    plt.xlabel("Year")
    plt.ylabel("Page Views")

    # how the values are distributed within a given months
    plt.subplot(1, 2, 2)
    sns.boxplot(
      data = df_box,
      x = "month",
      y = "value"
    )
    plt.title("Month-wise Box Plot (Seasonality)")
    plt.xlabel("Month")
    plt.ylabel("Page Views")
    locs, labels = plt.xticks()
    labels = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    plt.xticks(locs, labels)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

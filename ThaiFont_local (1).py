# This is an example of using Thai font in matplotlib.
# Only fonts available in your current computer can be chosen in this example.

import pandas as pd

import matplotlib as mpl
from matplotlib import font_manager
from matplotlib import pyplot as plt
mpl.use('tkagg')  

import seaborn as sns
sns.set()  # Set the seaborn style


# ======= STEP 1: Choose existing fonts =======

# Get the list of all available fonts
fpaths = font_manager.findSystemFonts()

# Print names of all fonts
print('\n===== Available fonts =====')
font_list = sorted([font_manager.get_font(i).family_name for i in fpaths])
_ = [ print(f"{i}. {a}") for i,a in enumerate(font_list) ]

# Ask user which font to use
# Ex: 'tahoma', 'TH Sarabun New'
font_num = input('\nSpecify the number of font you want to use or press Enter to use the default Tahoma\n>> ').strip()
font_name = 'tahoma' if font_num=='' else font_list[int(font_num)]


# ======= STEP 2: Set the font that supports Thai =======

# More font styles in https://matplotlib.org/stable/api/font_manager_api.html
params = {'font.family':font_name,
          'legend.fontsize':'x-large',
          'axes.labelsize':'x-large',
          'axes.titlesize':'x-large',
          'xtick.labelsize':'x-large',
          'ytick.labelsize':'x-large'}

# Update the default runtime configuration settings
plt.rcParams.update(params)


# ======= STEP 3: Display graph with Thai font =======

# Create a dummy dataframe with Thai font
df = pd.DataFrame( {'อายุ':[10, 30, 50, 20],
                    'ส่วนสูง':[100, 150, 145, 155]} )
print(df)

# Draw the graph
plt.figure(figsize=(10,5))
sns.scatterplot(x=df.iloc[:,0], y=df.iloc[:,1])
plt.show()

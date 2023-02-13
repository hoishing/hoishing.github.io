---
title: Using Chinese Characters in Matplotlib
tags: 
  - python
  - data science
---
###### date: 2019-04-21

When you try to display Chinese or other non-ascii characters in matplotlib, your characters may not be displayed properly, like following figure:

![Error displaying Chinese characters in matplotlib](https://i.imgur.com/pUSCY0B.png)

It is because the fonts used by matplotlib couldn’t decode the characters properly.

## The Fix

To fix it, we should add the appropriate fonts and update matplotlib font cache.

1. locate the matplotlib fonts folder:

```python
import matplotlib
print(matplotlib.matplotlib_fname())
```

this is the location of matplotlib config file, you will get something like `…/matplotlib/mpl-data/matplotlibrc`

The font folder is …/matplotlib/mpl-data/fonts/ttf , put your ttf file there.

2. Get ttf from ttc file (skip if you have ttf file already)

For macOS, the system Chinese fonts is Heiti, which is embed in a ttc file (ttc is a collection of multiple ttf files). Get the system ttc file in `/System/Library/Fonts/STHeiti Medium.ttc` Copy this file out and convert it to ttf. Here is an online ttc converter:

https://transfonter.org/ttc-unpack

3. Rebuild the Matplotlib Cache

```python
import matplotlib.font_manager
matplotlib.font_manager._rebuild()
```

restart your Jupyter / ipython kernel, then test if matplotlib can load your font or not by the `ttflist` function of the font manager

```python
[f for f in matplotlib.font_manager.fontManager.ttflist if 'Heiti' in f.name]
```

change ‘Heiti’ to your own font name. If you see your fonts object above. You are ready to use the new fonts.

4. Using Appropriate Fonts in Matplotlib

```python
matplotlib.rcParams['font.family'] = ['Heiti TC']
```

This will tell matplotlib to use the specific font as default, result as follow~

![map with Chinese characters enabled](https://i.imgur.com/kC6VQhw.png)

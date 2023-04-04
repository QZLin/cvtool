# CVTool

Provide some simple quick test function for opencv
All functions are wrapped in at most one level to make learning opencv through this project easier.  
[![CI](https://github.com/QZLin/cvtool/actions/workflows/cl.yml/badge.svg)](https://github.com/QZLin/cvtool/actions/workflows/cl.yml)

~~put `cvtool` folder to your project root path or add `cvtool` to python path~~  
(Deprecate, use setup.py)

## Install from source

1. clone repository  
   `git clone https://github.com/QZLin/cvtool.git`

2. install via pip  
   `pip install -e cvtool`

or

* install via pip+git  
  `pip install git+https://github.com/qzlin/cvtool`

## Functions

* wrapped template match

```python
import cv2 as cv
import cvtool

source = cv.imread('source.png')
template = cv.imread('template.png')

r: cvtool.tm.MatchResult = cvtool.tm.match(source, template, 0.9)

if r.matched:
    print(r.matched, r.pos, r.similarity)
```

# Acknowledgement

Free Pycharm License for opensource project  
[Licenses for Open Source Development - Community Support](https://jb.gg/OpenSourceSupport)
![JetBrains Logo (Main) logo](https://resources.jetbrains.com/storage/products/company/brand/logos/jb_beam.png)
![PyCharm logo](https://resources.jetbrains.com/storage/products/company/brand/logos/PyCharm.png)

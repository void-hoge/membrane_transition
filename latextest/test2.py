import matplotlib as matplotlib
matplotlib.use('pgf')
from matplotlib.backends.backend_pgf import FigureCanvasPgf
matplotlib.backend_bases.register_backend('png', FigureCanvasPgf)
from matplotlib import pyplot as plt

matplotlib.rc('pgf', texsystem='pdflatex')  # from running latex -v
preamble = matplotlib.rcParams.setdefault('pgf.preamble', [])
preamble = preamble+r'\usepackage{color}'
preamble = preamble+r'\usepackage{dashrule}'

ax = plt.plot((0, 1), (1, 2))[0].axes
ax.set_ylabel(r'Y $\;$ \textcolor{red}{\hdashrule[0.5ex]{3cm}{1pt}{1pt 0pt}}')
ax.set_xlabel(r'N $\;$ \textcolor{blue}{\rule[0.5ex]{3cm}{1pt}}')
plt.savefig('test.png')

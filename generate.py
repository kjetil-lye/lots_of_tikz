import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import matplotlib2tikz

# Generate some random plots and add them to a latex file
number_of_plots = 30

latex_code = ""
for plot_number in range(number_of_plots):
    X = np.random.normal(0, 1, 100)

    plt.plot(X)
    savename = 'img_tikz/plot_{plot_number}.tikz'.format(plot_number=plot_number)
    matplotlib2tikz.save(savename)

    latex_code += """
\\begin{{figure}}
\\input{{{savename}}}
\\caption{{Very interesting plot number {plot_number}}}
\\end{{figure}}""".format(
    savename=savename,
    plot_number=plot_number)
    
    plt.close('all')

with open("tikz_plots.tex", "w") as f:
    f.write(latex_code)
    

import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from skimage import color
matplotlib.use('Agg')

    
def trj2img(x, x_range, y_range, reduce_time=False):
    assert type(x) == np.ndarray, 'input x is required np.ndarray actual={}'.format(type(x))
    # batch, f_dim, seq
    def data_to_fig(x, y, shape=(64, 64), dpi=10):
        # make an agg figure

        # calc fig size
        figsize_px = np.array(shape)
        figsize_inch = figsize_px / dpi  # px/inch

        plt.style.use('dark_background')  # for tensorbaord style
        fig, ax = matplotlib.pyplot.subplots(figsize=figsize_inch, dpi=dpi)
        ax.scatter(x, y, c='white', marker='o')
        plt.xlim(x_range)
        plt.ylim(y_range)
        plt.axis("off")
        fig.canvas.draw()
        # grab the pixel buffer and dump it into a numpy array
        X = np.array(fig.canvas.renderer._renderer)[:, :, :3]
        X = color.rgb2gray(X).reshape(*shape, 1)  # to grayscale
        matplotlib.pyplot.close()
        matplotlib.rcParams.update(matplotlib.rcParamsDefault)  # reset style

        return X

    fig_lst = []
    if reduce_time:
        for xx in x:
            im = data_to_fig(xx[:,0], xx[:,1])
            fig_lst.append(im)
        return np.array(fig_lst).transpose(0, 3, 1, 2)  # batch, w, h, c => batch, c, h, w
        
    else:
        for xx in x:
            im = data_to_fig(xx[0], xx[1])
            fig_lst.append(im)
        return np.array(fig_lst).transpose(0,3,1,2)  # batch, w, h, c => batch, c, h, w

        

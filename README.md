# trj2img: convert from 2d trajectory (np.ndarray) to image (np.ndarray) for tensorbaord



### befor
2d trajectory np.ndarray[batch, 2, seq]

![input](https://github.com/MasanoriYamada/trj2img/blob/master/sample/input.png)


### oufter
image np.ndarray[batch, channel, w=64, h=64]

![ouput](https://github.com/MasanoriYamada/trj2img/blob/master/sample/output.png)

# How to use

plese see [example.ipynb](./example.ipynb)

```
trj2img(x, x_range, y_range, reduce_time=False)
x: np.ndarray (shape: [batch, 2, seq])
x_range: x value range (i.e. [-1,1])
y_range: y value range (i.e. [0, 1])
reduce_time: When True, display sequence overlaid on a single image 
```


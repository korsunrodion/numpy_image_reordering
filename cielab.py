from skimage import io, color

rgb = io.imread('test.jpg')
lab = color.rgb2lab(rgb)

fl = lab.reshape(lab.shape[0]*lab.shape[1], 3)
s = fl[fl[:,2].argsort()[::-1]].reshape(lab.shape[0], lab.shape[1], 3)
result = color.lab2rgb(s)
io.imsave('result.png', result)

import numpy
from PIL import Image

def generate_image(mb):
	x = ((1000 * 1000 / 3) * mb) ** 0.5
	x = int(x)

	if x > 10000:
		print("You can not generate such a large image")
		return False
		

	a = numpy.random.rand(x, x, 3) * 255
	im_out = Image.fromarray(a.astype('uint8')).convert('RGBA')
	im_out.save('generated.png', 'PNG')
	return True


mb = 50

generate_image(mb)
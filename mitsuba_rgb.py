import mitsuba as mi
import time

start = time.time()

mi.set_variant("cuda_ad_rgb")
scene = mi.load_file("input.xml")
image = mi.render(scene)
mi.util.write_bitmap("image.png", image)

end = time.time()
print(str(round(end - start, 2)) + " seconds")
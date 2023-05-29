import mitsuba as mi
import time

start = time.time()
print(mi.variants())
mi.set_variant("llvm_ad_rgb")
scene = mi.load_file("scene.xml")
image = mi.render(scene)
mi.util.write_bitmap("image.png", image)

end = time.time()
print(str(round(end - start, 2)) + " seconds")
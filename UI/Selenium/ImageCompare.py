import Image
from PIL import ImageChops, ImageStat

def CompareImages(image1,image2,diffImagePath):
    im1 = Image.open(image1)
    im2 = Image.open(image2)

    diff_img = ImageChops.difference(im2, im1)
    diff_img.convert('RGB').save(diffImagePath)
    stat = ImageStat.Stat(diff_img)
    # can be [r,g,b] or [r,g,b,a]
    sum_channel_values = sum(stat.mean)
    max_all_channels = len(stat.mean) * 100
    return sum_channel_values/max_all_channels

diff_ratio = CompareImages("C:/Users/GILTZ/Desktop/image1.jpg",
                           "C:/Users/GILTZ/Desktop/image2.jpg",
                           "C:/Users/GILTZ/Desktop/diff_img_file.jpg")
print(diff_ratio)




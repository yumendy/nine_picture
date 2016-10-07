from PIL import Image
import sys


class NinePictures(object):
    def __init__(self, file_path):
        self.image = Image.open(file_path)
        self.width, self.height = self.image.size
        self.cut_image()

    def cut_image(self):
        if self.width < self.height:
            self.cut_height()
        elif self.width > self.height:
            self.cut_width()

    def cut_height(self):
        box = (0, (self.height - self.width) / 2, self.width, (self.height + self.width) / 2)
        self.image = self.image.crop(box)

    def cut_width(self):
        box = ((self.width - self.height) / 2, 0, (self.height + self.width) / 2, self.height)
        self.image = self.image.crop(box)

    def process(self):
        length = (self.width if self.width < self.height else self.height) / 3
        left_list = [0, length, length * 2] * 3
        upper_list = [0] * 3 + [length] * 3 + [length * 2] * 3
        right_list = [length, length * 2, length * 3] * 3
        lower_list = [length] * 3 + [length * 2] * 3 + [length * 3] * 3

        box_list = zip(left_list, upper_list, right_list, lower_list)

        image_list = [self.image.crop(box) for box in box_list]

        return image_list

    def save_image(self):
        image_list = self.process()

        order_number = 1
        for image in image_list:
            image.save(str(order_number) + '.png', 'PNG')
            order_number += 1


if __name__ == '__main__':
    image_path = sys.argv[1]
    app = NinePictures(image_path)
    app.save_image()

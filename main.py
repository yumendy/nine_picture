from PIL import Image
import sys


class NinePictures(object):
    def __init__(self, file_path, mode):
        self.image = Image.open(file_path)
        self.width, self.height = self.image.size
        if mode == 'C':
            self.length = self.width if self.width < self.height else self.height
            self.cut_image()
        elif mode == 'F':
            self.length = self.width if self.width > self.height else self.height
            self.fill_image()

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

    def fill_image(self):
        new_image = Image.new(self.image.mode, (self.length, self.length), color='white')
        if self.width > self.height:
            self.fill_height(new_image)
        elif self.width < self.height:
            self.fill_width(new_image)

    def fill_height(self, new_image):
        new_image.paste(self.image, (0, (self.length - self.height) / 2))
        self.image = new_image

    def fill_width(self, new_image):
        new_image.paste(self.image, ((self.length - self.width) / 2, 0))
        self.image = new_image

    def process(self):
        length = self.length / 3
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
    image_mode = sys.argv[1]
    image_path = sys.argv[2]
    app = NinePictures(image_path, image_mode)
    app.save_image()

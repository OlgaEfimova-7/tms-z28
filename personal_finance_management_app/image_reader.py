import os
from unicodedata import decimal

import cv as cv
import numpy as np
from PIL import Image, ImageFilter, ImageEnhance
import pytesseract
import re
import cv2

# if __name__ == '__main__':

# class CommonTemplate:
#     def common_type_of_cheque(self, keywords, recognized_text):
#         list_of_products = []
#         for index_i, i in enumerate(recognized_text):
#             for j in keywords:
#                 if j in i.lower():
#                     list_of_products.append(i.lower())
#         print(list_of_products)
#
#
# class FirstTypeChequeTemplate(CommonTemplate):
#     def common_type_of_cheque(self, keywords, recognized_text):
#         super().common_type_of_cheque(keywords, recognized_text)
#         list_of_prices = []
#         for index_i, i in enumerate(recognized_text):
#             for j in keywords:
#                 if j in i.lower():
#                     list_of_prices.append(list(recognized_text[index_i + 1].split(' '))[-1])
#         print(list_of_prices)


# class SecondTypeChequeTemplate(CommonTemplate):
#     def common_type_of_cheque(self, keywords, recognized_text):
#         super().common_type_of_cheque(keywords, recognized_text)
#         list_of_prices = []
#         for index_i, i in enumerate(recognized_text):
#             for j in keywords:
#                 if j in i.lower():
#                     list_of_prices.append((list(recognized_text[index_i + 1].split('='))[-1].split(' '))[-1])
#         print(list_of_prices)
from personal_finance_management_app.models import InstitutionKeywords


def text_reader(image):
    """ recognise text from upload cheque"""
    recognized_text = pytesseract.image_to_string(Image.open(image), lang='rus')
    # print(recognized_text)
    return recognized_text



def cheque_parser(recognized_text, list_of_institutions, list_of_products):
    """ parse information from cheque"""
    time_and_date = re.search(r'\d\d-\d\d-20\d\d \d\d:\d\d', recognized_text)
    """ parse time and date"""
    list_of_strings_from_text = list(filter(lambda x: len(x) > 0 and x.isspace() is False, list(recognized_text.split('\n'))))
    """ transforms text into list of string without empty string and string of spaces"""
    name_of_institution = 0
    institution_keyword = 0
    list_of_parsed_products = []
    list_of_keywords_parsed_products = []
    list_of_prices = []
    """ searching of name of institution"""
    for index_i, i in enumerate(list_of_strings_from_text):
        for institution in list_of_institutions:
            if institution.lower() in i.lower():
                name_of_institution = i
                institution_keyword = institution
                break
    """ searching of cheque positions and prices """
    for index_i, i in enumerate(list_of_strings_from_text):
        for product in list_of_products:
            if product.lower() in i.lower():
                list_of_parsed_products.append(i)
                list_of_keywords_parsed_products.append(product)
                if index_i+1 < len(list_of_strings_from_text):
                    price_of_product = ((list(list_of_strings_from_text[index_i + 1].split('='))[-1].split(' '))[-1])
                else:
                    price_of_product = 0
                try:
                    list_of_prices.append(float(price_of_product))
                except ValueError:
                    list_of_prices.append(None)
                break
    try:
        return time_and_date.group(0), name_of_institution, list_of_parsed_products, \
               list_of_prices, institution_keyword, list_of_keywords_parsed_products
    except AttributeError:
        return None, name_of_institution, list_of_parsed_products, \
               list_of_prices, institution_keyword, list_of_keywords_parsed_products


# im = Image.open('Cheks/photo_2020-05-21 09.37.47 (1).jpeg')
# im.show()
# enh = ImageEnhance.Contrast(im)
# enh1 = enh.enhance(1.8)
# enh1.save('/Users/olga/PycharmProjects/personal_finance_management_app/Cheks/photo_contrast_2020-05-21 09.37.47 (1).jpeg')
# print(text_reader('Cheks/photo_contrast_2020-05-21 09.37.47 (1).jpeg'))


# black = (0,0,0)
# white = (255,255,255)
# threshold = (160,160,160)

# Open input image in grayscale mode and get its pixels.
# img = Image.open("Cheks/photo_2020-05-20 20.15.05.jpeg").convert("LA")
# pixels = img.getdata()
#
# newPixels = []
#
# # Compare each pixel
# for pixel in pixels:
#     if pixel < threshold:
#         newPixels.append(black)
#     else:
#         newPixels.append(white)

# # Create and save new image.
# newImg = Image.new("RGB",img.size)
# newImg.putdata(newPixels)
# newImg.save("Cheks/photo_improve_2020-05-20 20.15.05.jpeg")
# image = cv2.imread('Cheks/photo_improve_2020-05-20 20.15.05.jpeg', 0)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
# erosion = cv2.erode(image, kernel, iterations=10)
# cv2.imshow('erosion', erosion)
# print(pytesseract.image_to_string(erosion, lang='rus'))
# cv2.waitKey()
# # print(text_reader('Cheks/photo_improve_2020-05-20 20.15.05.jpeg'))


# img = Image.open('Cheks/photo_2020-05-20 20.15.05.jpeg')
# # one kind of emboss
# km = (
#      -2, -1,  0,
#      -1,  1,  1,
#       0,  1,  2
#       )
# k = ImageFilter.Kernel(
#     size=(3, 3),
#     kernel=km,
#     scale=sum(km),  # default
#     offset=0  # default
#     )
# img.filter(k).save(
#     '/Users/olga/PycharmProjects/personal_finance_management_app/Cheks/photo_filter_2020-05-20 20.15.05.jpeg')
# print(text_reader('Cheks/photo_filter_2020-05-20 20.15.05.jpeg'))


# # load the example image and convert it to grayscale
# image = cv2.imread('Cheks/photo_2020-05-20 20.15.05.jpeg')
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# # # check to see if we should apply thresholding to preprocess the
# # # image
# # # if args["preprocess"] == "thresh":
# gray = cv2.threshold(gray, 0, 250, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# # # make a check to see if median blurring should be done to remove
# # # noise
# # elif args["preprocess"] == "blur":
# # gray = cv2.medianBlur(gray, 3)
# # # write the grayscale image to disk as a temporary file so we can
# # # apply OCR to it
# filename = "{}.png".format(os.getpid())
# cv2.imwrite(filename, gray)
# text = pytesseract.image_to_string(Image.open(filename), lang='rus')
# os.remove(filename)
# print(text)
# # show the output images
# cv2.imshow("Image", image)
# cv2.imshow("Output", gray)
# cv2.waitKey(0)

# image = cv2.imread('Cheks/photo_2020-05-20 20.15.05.jpeg', 0)
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 1))
# # kernel = np.ones((5, 5), np.uint8)
# erosion = cv2.erode(image, kernel, iterations=10)
# opening = cv2.morphologyEx(image, cv2.MORPH_OPEN, kernel)
# closing = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
# result = 230 - closing
# cv2.imshow('erosion', erosion)
# # cv2.imshow('close', closing)
# # cv2.imshow('result', result)
# # cv2.imshow('opening', opening)
# print(pytesseract.image_to_string(erosion, lang='rus'))
# cv2.waitKey()

# # Path for Windows
# # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#
# # Read in image as grayscale
# image = cv2.imread('Cheks/photo_2020-05-20 20.15.05.jpeg',0)
# # Threshold to obtain binary image
# thresh = cv2.threshold(image, 220, 255, cv2.THRESH_BINARY)[1]
#
# # Create custom kernel
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
# # Perform closing (dilation followed by erosion)
# close = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
#
# # Invert image to use for Tesseract
# result = 255 - close
# cv2.imshow('thresh', thresh)
# cv2.imshow('close', close)
# cv2.imshow('result', result)
#
# # Throw image into tesseract
# print(pytesseract.image_to_string(result))
# cv2.waitKey()


# dict_of_stores_and_types_of_cheque = {'табак': 2, 'веста': 1, 'евроторг': 2, 'белвиплесден': 2, 'парфюм': 2, 'патио': 2}
# text = text_reader('Cheks/korona.jpeg')
# print(text)
# list_of_strings_from_text = list(filter(lambda x: len(x) > 0 and x.isspace() is False, list(text.split('\n'))))
# print(list_of_strings_from_text)
# name_of_store = 0
# time_and_date = re.search(r'\d\d-\d\d-20\d\d \d\d:\d\d', text)
# address = re.search(r'г\..+', text)
# print(address.group(0))
# print(time_and_date.group(0))
# keywords_of_products = ['хлопья', 'молоко', 'пиво', 'оливки', 'сыр', 'шоколад', 'чай', 'сметана', 'лимон', 'хна',
#                             'носки', 'зубная паста', 'салфетки', 'акустическая']
# for j, k in dict_of_stores_and_types_of_cheque.items():
#     for index_i, i in enumerate(list_of_strings_from_text):
#         if j in i.lower():
#             name_of_store = i.lower()
#             if k == 1:
#                 FirstTypeChequeTemplate().common_type_of_cheque(keywords_of_products, list_of_strings_from_text)
#                 break
#             elif k == 2:
#                 SecondTypeChequeTemplate().common_type_of_cheque(keywords_of_products, list_of_strings_from_text)
#                 break
# time_and_date = re.search(r'\d\d-\d\d-20\d\d \d\d:\d\d', text)

import cv2
import matplotlib.pyplot as plt
import json
import os

IMAGE_PATH = "./marchantia" 

def get_image_path():
    image_list = os.listdir(path = IMAGE_PATH)
    image_path_list = list(map(lambda i: IMAGE_PATH + "/" + i, image_list))
    return image_path_list

def get_path_from_json(json_file):
    try :
        print(json_file)
        with open(json_file, mode = "r", encode = "utf-8") as f :
            print(type(f))
            data = json.load(f)
            print(type(data))
            text = json.loads(data)
            text_len = len(text)
        return text , text_len
    except :
        print("Error")

def to_grayscale(path):
    image = cv2.imread(path)
    grayed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    return grayed_image

def main() :
    image_path_list = get_image_path()
    for image_path in image_path_list :
        print(image_path)
        grayed_image = to_grayscale(image_path)
        cv2.imshow(image_path, grayed_image)
        cv2.waitKey(0)
       # cv2.destroyAllWindows()


if __name__ == "__main__" :
    main()



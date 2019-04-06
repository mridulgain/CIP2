#simulate color filter array output
import sys
import cv2
import numpy as np

def colorFilter(input_img, filter):
    try:
        height, width = input_img.shape[:2]
        print("image resolution :", width ,"x" ,height)
        filter_dim = len(filter)
        img = np.zeros((height,width), dtype=np.uint8)
        for i in range(0,height,filter_dim):
            for j in range(0, width,filter_dim):
                #cell1 = np.uint8(160)
                for k in range(filter_dim):
                    for l in range(filter_dim):                              
                        img[i+k][j+l] = input_img[i+k][j+l][filter[k][l]]
        cv2.imshow("Input", input_img)
        cv2.imshow("Output", img)
        cv2.waitKey()
        cv2.imwrite("mosaiced.ppm", img);
    except AttributeError:
        print("Invalid file. Please check the file name you have entered") 

if __name__ == "__main__":
    try:
        img = cv2.imread(sys.argv[1])
        bayer_filter = [#considering bgr image
            [2 , 1],#R=2 G=1
            [1, 0]  #G=1 B=0
        ]           
        colorFilter(img, bayer_filter)
    except IndexError:
        print("error : please provide file name as command line argument")
        print("try : python", sys.argv[0], "<image_file_name>")

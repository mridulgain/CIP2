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
            print("processing row : ", i , end="\r")
            for j in range(0, width,filter_dim):
                #cell1 = np.uint8(160)
                for k in range(filter_dim):
                    for l in range(filter_dim):                              
                        img[i+k][j+l] = input_img[i+k][j+l][filter[k][l]]
                        #print(img[i+k][j+l])
        return img
    except AttributeError:
        print("Invalid file. Please check the file name you have entered") 

if __name__ == "__main__":
    try:
        input_img = cv2.imread(sys.argv[1])
        bayer_filter = [#considering bgr image
            [2, 1],#R=2 G=1
            [1, 0]  #G=1 B=0
        ]
        out_img = colorFilter(input_img, bayer_filter)
        cv2.imshow("Input", input_img)
        cv2.imshow("Output", out_img)
        cv2.waitKey(0)
        cv2.imwrite("mosaiced.pgm", out_img);
    except IndexError:
        print("error : please provide file name as command line argument")
        print("try : python", sys.argv[0], "<image_file_name>")

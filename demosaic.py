#demosaic a filter output
import sys
import cv2
import numpy as np

def demosaic(img, filter):
    #nearest neighbour interpolation
    try:
        height, width = img.shape[:2]
        print("image resolution :", width ,"x" ,height)
        filter_dim = len(filter)
        out_img = np.zeros((height,width,3), dtype=np.uint8)
        for i in range(0,height,filter_dim):
            print("processing row : ", i , end="\r")
            for j in range(0, width,filter_dim):
                #img[row][col]
                count = np.zeros(3)
                pixel = np.zeros(3)
                for k in range(filter_dim):
                    for l in range(filter_dim):
                        pixel[filter[k][l]] += img[i+k][j+l]
                        count[filter[k][l]] += 1
                #avg 
                pixel = np.uint(pixel/count)
                #assigning values
                for k in range(filter_dim):
                    for l in range(filter_dim):
                        temp = img[i+k][j+l]
                        #print(temp)
                        out_img[i+k][j+l] = pixel
                        out_img[i+k][j+l][filter[k][l]] = temp
        return out_img
    except AttributeError:
        print("Invalid file. Please check the file name you have entered") 


if __name__=="__main__":
    try:
        img = cv2.imread(sys.argv[1], 0)#reading grayscale
        print(img.shape)
        bayer_filter = [#considering bgr image
            [2, 1],#R=2 G=1
            [1, 0]  #G=1 B=0
        ]
        out_img = demosaic(img, bayer_filter)
        cv2.imshow("Input", img)
        cv2.imshow("Demosaiced", out_img)
        cv2.imwrite("demosaiced.ppm", out_img)
        cv2.waitKey(0)
    except IndexError:
        print("error : please provide file name as command line argument")
        print("try : python", sys.argv[0], "<image_file_name>")
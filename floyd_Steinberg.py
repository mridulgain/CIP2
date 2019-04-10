#standard error diffusion using Floyd-Steinberg's algo
import sys
import cv2
import numpy as np

def floyd_Steinberg(img):
    try:
        height, width = input_img.shape[:2]
        print("image resolution :", width ,"x" ,height)
        out_img = np.copy(img)
        thres = 128
        for row in range(height):
            print("Processing row :",row , end="\r")
            for col in range(width):
                current_pixel = out_img[row][col]
                out_img[row][col] = 0 if out_img[row][col] < thres else 255
                err = (int(current_pixel) - int(out_img[row][col]))/16
                print(err)
                if row+1 < height:
                    new_val = out_img[row+1][col] + err*5
                    out_img[row+1][col] = np.uint8(new_val) if new_val < 255 else 255
                if row+1 < height and col-1 >=0:
                    new_val = out_img[row+1][col-1] + err*3
                    out_img[row+1][col-1] = np.uint8(new_val) if new_val < 255 else 255
                if col+1 < width:
                    new_val = out_img[row][col+1] + err*7
                    out_img[row][col+1] = np.uint8(new_val) if new_val < 255 else 255
                if col+1 < width and row+1 < height:
                    new_val = out_img[row+1][col+1] + err*1
                    out_img[row+1][col+1] = np.uint8(new_val) if new_val < 255 else 255
        return out_img
    except:
        print("e")

if __name__ == "__main__":
    try:
        input_img = cv2.imread(sys.argv[1], 0)
        out_img = floyd_Steinberg(input_img)
        cv2.imshow("Input", input_img)
        cv2.imshow("Output", out_img)
        cv2.waitKey(0)
        cv2.imwrite("mosaiced.pgm", out_img)
    except IndexError:
        print("error : please provide file name as command line argument")
        print("try : python", sys.argv[0], "<image_file_name>")
    except cv2.error:
        print("Invalid image file")

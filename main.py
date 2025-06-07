import pyautogui
import keyboard



def main():

    while True:

        # Take a screenshot 
        sc = pyautogui.screenshot()

        # Checking Pixel for Start
        main_pixel = sc.getpixel((214, 500))


        p1 = sc.getpixel((372, 700)) 
        p2 = sc.getpixel((343, 705))
        p3 = sc.getpixel((393, 742))
        p4 = sc.getpixel((396, 741))
        p5 = sc.getpixel((358, 764))
        p6 = sc.getpixel((226, 690))
        p7 = sc.getpixel((233, 713))
        p8 = sc.getpixel((244, 718))
        
        if main_pixel[0] == 255:             
            if p1[0] != 255 or p2[0] != 255 or p3[0] != 255 or p4[0] != 255 or p5[0] != 255 or p6[0] != 255 or p7[0] != 255 or p8[0] != 255:                      
                pyautogui.press("space")


        if keyboard.is_pressed("q"):
            break


if __name__ == "__main__":
    main()
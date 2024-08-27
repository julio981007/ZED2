import cv2
import numpy
import sys
import keyboard

def main():
    # Open the ZED camera
    cap = cv2.VideoCapture(1)
    
    # fourcc = cv2.VideoWriter_fourcc(*format)	# fourcc 값 지정
    out = cv2.VideoWriter('ZED2_output.mp4', fourcc, fps, (width,height))	# VideoWriter 객체 생성
    
    if not cap.isOpened():
        print('Camera open failed!')
        sys.exit()
    
    if not out.isOpened():
        print('File open failed!')
        cap.release()
        sys.exit()

    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, fps)
    
    print('Width : ', cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    print('Height : ', cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    print('FPS : ', cap.get(cv2.CAP_PROP_FPS))
    
    while True:
        # 'Enter' 키가 눌리면 루프 종료
        if keyboard.is_pressed('enter'):
            print("[INFO] Terminating processes...")
            break
        
        # Get a new frame from camera
        retval, frame = cap.read()
        
        if not retval:
            print('Image read failed!')
            break
        
        out.write(frame)
        
        # Extract left and right images from side-by-side
        left_right_image = numpy.split(frame, 2, axis=1)
        # Display images
        # cv2.imshow("frame", frame)
        # cv2.imshow("right", left_right_image[0])
        # cv2.imshow("left", left_right_image[1])
        # cv2.imwrite("frame.png", frame)
        # cv2.imwrite("right.png", left_right_image[0])
        # cv2.imwrite("left.png", left_right_image[1])
        # break
    
    cap.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    width = 1280 * 2
    height = 720
    fps = 60
    fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
    
    main()
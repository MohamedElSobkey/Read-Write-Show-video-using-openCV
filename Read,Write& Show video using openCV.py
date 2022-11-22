# import opencv
import cv2

#open your laptop camera
cap = cv2.VideoCapture(0)

#use any fourcc type to improve quality for the saved video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#Video settings
#20.0 frame each sec
#(640,480) are hight & width

out = cv2.VideoWriter('output.mp4',fourcc, 20.0, (640,480))
#check if the camera is opened
print(cap.isOpened())
#while loop to read all frames
while (cap.isOpened()) :
    #read all frames if ret is TRUE it means that there is a frames to process   
    ret , frame = cap.read()
    #if ret is true   
    if ret == True :
        #get the frame width
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        #get the frame height
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        
        #save your video 
        out.write(frame)
        #convert frames from BGR2GRAY  
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
        #show the frames
        cv2.imshow('frame', gray)
       #if u pressed q close the window and break
        if cv2.waitKey(1) & 0xFF == ord('q') :
            break 
        #it will enter here if the ret = false and break the code 
    else  : 
        break 
    
#close the camera after u finish the running process    
cap.release()
#release your video after u save it
out.release() 



# pwd to know where the video saved


    

       
        
        
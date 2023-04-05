import cv2
cap= cv2.VideoCapture(0)
tracker = cv2.TrackerMOSSE_create() # tracker used 
none,img = cap.read()
bbox = cv2.selectROI("tracking",img,False)
tracker.init(img,bbox)                                     
def drawbox(img,bbox):
   x,y,a,b = int(bbox[0]),int(bbox[1]),int(bbox[2]),int(bbox[3])

   cv2.rectangle(img,(x,y),((x+a),(y+b)),(0,0,255),3,1)
while True:
  
   none,img = cap.read()

   none,bbox = tracker.update(img)

   if none:
      drawbox(img,bbox)
      cv2.putText(img,"status :tracking",(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
   else:
      cv2.putText(img,"status : lost",(50,50),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,225),2)

   
   cv2.imshow("tracking",img)

   if cv2.waitKey(1) & 0xFF == ord('w'):
      break
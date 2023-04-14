import cv2
from detection import AccidentDetectionModel
import numpy as np
import os
import time
import datetime
import pandas as pd

#model = AccidentDetectionModel(r"C:\Users\home\Documents\python\model_crash.json",r"C:\Users\home\Documents\python\model_weights.h5")
model = AccidentDetectionModel(r"C:\Users\home\Documents\python\model1.json",r"C:\Users\home\Documents\python\model1.h5")
font = cv2.FONT_HERSHEY_SIMPLEX

import time



                
def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        #time.sleep(1)
        time_sec -= 1


def startapplication():
   
    #video = cv2.VideoCapture(r"C:\Users\home\Documents\python\caught-on-camera-car-thrown-in-the-air-after-crash-in-horrifying-crash_xIoY10m3.mp4")
    #video = cv2.VideoCapture(r"C:\Users\home\Documents\python\assets\videoplayback_CBeYsFuN.mp4")
    video=cv2.VideoCapture(r"C:\Users\home\Documents\python\assets\Car_Crashes_and_Dangerous_Driving_06_BeamNG_Drive_from100s_to120s.mp4")
    #video = cv2.VideoCapture(r"C:\Users\home\Documents\python\assets\karma on the road #shorts.mp4")
    screenshot_counter = 0
    while True:
        ret, frame = video.read()
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        roi = cv2.resize(gray_frame, (250, 250))

        pred, prob = model.predict_accident(roi[np.newaxis, :, :])
       
        
        data_file = r"C:\\Users\\home\\Documents\\python\data\\accidentoccurrencedb.csv"

        if os.path.isfile(data_file):
            # If the file exists, read in the existing data
            df = pd.read_csv(data_file)
        else:
            # If the file does not exist, create an empty dataframe with the appropriate column names
            df = pd.DataFrame(columns=['timestamp', 'prediction'])
    



        if(pred == "Accident"):
            prob = (round(prob[0][0]*100, 2))
            cv2.rectangle(frame, (0, 0), (280, 40), (0, 0, 0), -1)
            if prob>90:   

                cv2.putText(frame, pred+" "+str(prob), (20, 30), font, 1, (255, 255, 0), 2)
                now = datetime.datetime.now()
                
                # Format the timestamp as a string
                timestamp = now.strftime("%Y-%m-%d_%H-%M")
                output_dir = fr"C:\Users\home\Documents\python\data\footage_{timestamp}"
                
                if not os.path.exists(output_dir):
                    os.makedirs(output_dir)
                    # create a new row with the timestamp and prediction values
                    new_row = {'timestamp': timestamp, 'prediction': pred}
                    # append the new row to the dataframe
                    df = df.append(new_row, ignore_index=True)
                    df.to_csv(r"C:\\Users\\home\\Documents\\python\\data\\accidentoccurrencedb.csv",index=False)

                    print(df)


                screenshot_counter += 1
                image_path = os.path.join(output_dir, f"frame{screenshot_counter}_{timestamp}.jpg")
                cv2.imwrite(image_path, frame)
                
                        
        else:
            cv2.putText(frame,"No Accident"+" ", (20, 30), font, 1, (255, 255, 0), 2)

       
        if cv2.waitKey(33) & 0xFF == ord('q'):
            return
        cv2.imshow('Video', frame)  


if __name__ == '__main__':
    startapplication()


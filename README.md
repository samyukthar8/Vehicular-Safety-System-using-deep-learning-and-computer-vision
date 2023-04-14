# Vehicular-Safety-System-using-Deep-Learning-and-Computer-Vision
The project predominantly focuses on instantaneously obtaining evidence of accidents instantaneously which enables identifying the perpetrators even in cases of hit-and-run accidents.The video is parsed and on detection of an accident in the frame, it is instantaneously stored in a folder with that timestamp.Later on, the details can be queried.
![image](https://user-images.githubusercontent.com/63106738/232092677-3a497797-e5a8-4d5d-af96-31a4074fbff0.png)
![image](https://user-images.githubusercontent.com/63106738/232092749-1848057d-435c-4917-beca-234d7ac24650.png)
![image](https://user-images.githubusercontent.com/63106738/232092794-04922ac3-be58-4c73-8816-619badc29877.png)
![image](https://user-images.githubusercontent.com/63106738/232092870-b12665b1-15f8-477d-b8e3-528d0bbea634.png)
![image](https://user-images.githubusercontent.com/63106738/232096602-71bc279a-7424-4485-bf17-b10a60c03422.png)

 
 PROCEDURE TO RUN THE PROJECR:
 1)Train the model:ipynb file
 2)run detect.py
 3)pickle the model:crash_model_pickler.py
 4)run camera.py specify the video path of that to be analysed
 5)querydb.py to create csv file of specific footage wrt timestamp
NOTE1:The dataset used to train the model is taken from:
https://www.kaggle.com/datasets/ckay16/accident-detection-from-cctv-footage
NOTE2: Wherever file paths are specified, change to your location.


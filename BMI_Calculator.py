height = input('Please enter your height(cm)')
weight = input('Please enter your weight(kg)')
height = int(height)
weight = int(weight)
height = height/100
BMI = weight / height / height
if BMI < 18.5:
    print ('you are too skinny')
elif 18.5 <= BMI < 24:
    print ('your weight is normal')
else:
    print ('you are overweight')
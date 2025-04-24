weight=float(input('Enter your weight: (kg)'))
height=float(input('Enter your height to 2 d.p : (m)'))

BMI=weight/height**2
print(f'Your Body Mass index is {BMI}')
category=float(input(' Now Enter your BMI'))

if 18.5 > category:
    print('You are underweight')
elif 18.5 <= category <=24.9:
    print('You are normal weight')
elif 25.0 <= category <=29.9:
    print('You are overweight')
elif 30.0 <= category <=34.9:
    print('You are in obesity class 1 and moderately obese')
elif 34.9 <= category <=39.9:
    print('You are severely obese and in obesity class 2')
elif category >=40:
    print('You are extremely and morbidly obese, in the highest class being class 3 ')
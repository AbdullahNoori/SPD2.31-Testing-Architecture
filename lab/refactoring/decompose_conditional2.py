# By Kami Bigdely
# Decompose conditional
# Reference: https://www.healthline.com/health/high-cholesterol/levels-by-age

# Blood test analysis program
total_cholesterol = 70
ldl = 30
triglyceride = 120

good_level = total_cholesterol < 200 and ldl < 100 and triglyceride < 150
mid_level = 200 < total_cholesterol > 240 or ldl > 160 or triglyceride <= 200
bad_level = 200 < total_cholesterol < 240 or 130 < ldl < 160 or 150 <= triglyceride < 200

if good_level:
    # good level
    print('*** Good level of cholestrol ***')
elif mid_level:
    # High cholestrol level
    print('*** High cholestrol level ***')
    print('start taking pills such as statins')
    print('start TLC diet')
elif bad_level:
    #TLC_diet
    print('*** Borderline to moderately elevated ***')
    print("Start TLC diet")
    print("Under this meal plan, only 7 percent of your daily calories \nshould come from saturated fat.")
    print('Some foods help your digestive tract absorb less cholesterol. For example,\nyour doctor may encourage you to eat more:')
    print('oats, barley, and other whole grains.')
    print('fruits such as apples, pears, bananas, and oranges.')
else:
    print('Error: unhandled case.')


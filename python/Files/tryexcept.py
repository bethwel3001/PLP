try:
    # print("Hello Vs Code!")
    file = open("example.txt", "r")
    data = file.read()
    print("The data is:", data )
except:
    print("Sorry, the file is invalid.")

# 'This code shows the importance of having meaningful errors in our applications, the end user can understand the error in an app'
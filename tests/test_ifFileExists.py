#tests if file exists
if os.path.exists("temporaryText.txt"):
    print("return_value:", os.path.exists("temporaryText.txt"))
    print("file exists")
else:
    print("return_value:", os.path.exists("temporaryText.txt"))
    print('file doesn t exist')    
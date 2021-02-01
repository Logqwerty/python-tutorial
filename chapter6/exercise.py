str = 'X-DSPM-Confidence: 0.8475'

index = str.find(': ')
floatStr = str[index+1:]
floatNum = float(floatStr)
print(type(floatNum))
print(floatNum)

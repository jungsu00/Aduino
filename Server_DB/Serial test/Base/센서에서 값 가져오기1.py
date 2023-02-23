#      -- 아트멜 스튜디오에서 센서값이 "temperature : "으로 나오게 설정하고
#         라즈베리파이에서 "temperature"라고 써져 있는 문장을 따오는 방식 --

# while True:
#     data = ser.readline().decode()
#     if "temperature:" in data:   
#         temperature = int(data.split(":")[1])
#         temperatureValue = temperature
#         dC.insertSensor1(temperatureValue)
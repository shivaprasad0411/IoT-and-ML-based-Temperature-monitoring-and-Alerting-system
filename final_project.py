import conf, json, math, statistics, time
# import Bolt class and SMS from boltiot
from boltiot import Bolt, Sms

# declare bolt using parameters, API key and device Id
mybolt = Bolt(conf.API_KEY,conf.DEVICE_ID)

# declare SMS using bolt library with parameters of Twilio 
sms = Sms(conf.SID,conf.AUTH_TOKEN,conf.TO_NUMBER,conf.FROM_NUMBER)
history_data = []

# function to compute the bounds to detect anomaly using Machine learning
def compute_bounds(history_data,frame_size,mul_factor):
        if len(history_data) < frame_size:
                return None
        if len(history_data) > frame_size:
                del history_data[:len(history_data)-frame_size]
        # taking mean of all data points
        mean = statistics.mean(history_data)
        var = 0
        # calculating variance of data
        for data in history_data:
                var += math.pow((data-mean),2)
        # calculating z-factor val
        z_val = mul_factor * math.sqrt(var / frame_size)
        # finding boundary values
        u_bound = history_data[frame_size-1] + z_val
        l_bound = history_data[frame_size-1] - z_val
        return [u_bound,l_bound]

while True:
        # reading input from temperature sensor
        response = mybolt.analogRead("A0")
        data = json.loads(response)
        if data["success"] != 1:
                print("Error occured while retriving the data")
                print("Retrying after 10 seconds")
                time.sleep(10)
                continue

        sensor_val = 0
        try:
                sensor_val = float(data['value'])
        except Exception as e:
                print("Error occured while parsing the response: ",e)

        # converting analog input to degree celcius
        sensor_val = (100 * sensor_val) / 1024
        print("The value of temperature in degree celsius:",sensor_val)
        # computing the bounds for the temperature
        bounds = compute_bounds(history_data,conf.FRAME_SIZE,conf.MUL_FACTOR)

        if not bounds:
                req_datapoints = conf.FRAME_SIZE - len(history_data)
                print("Not enough data points to compute Z-score. Need ",req_datapoints-1,"more data points.\n")
                history_data.append(sensor_val)
                time.sleep(10)
                continue
        print("Lower bound : {}, Upper bound : {}\n".format(bounds[1],bounds[0]))

        try:
                # checking for anomaly using the bound values
                if sensor_val > bounds[0] :
                        print("The temperature has increased suddenly.Sending an sms to alert.")
                        # sending sms alert
                        response = sms.send_sms("Alert!! Temperature has increased suddenly.\n The present value of temperature is {}".format(sensor_val))
                        print("The reponse is :",response)
                        # switching on the Buzzer
                        response1 = mybolt.digitalWrite("0","HIGH")
                        response1 = json.loads(response1)
                        if response1["success"] != 1:
                                print("Error while switching on the buzzer")
                        else :
                                print("Switched on the buzzer to alert")

                elif sensor_val < bounds[1] :
                        print("The temperature has decreased suddenly. Sending an sms to alert")
                        response = sms.send_sms("Alert!! Temperature has decreased suddenly.\n The present value of temperature is {}".format(sensor_val))
                        print("The reponse is :",response)
                        response1 = mybolt.digitalWrite("0","HIGH")
                        response1 = json.loads(response1)
                        if response1["success"] != 1:
                                print("Error while switching on the buzzer")
                        else :
                                print("Switched on the buzzer to alert")
                else :
                        history_data.append(sensor_val)

        except Exception as e:
                print("Error has occured :",e)
        time.sleep(10)
        mybolt.digitalWrite("0","LOW")

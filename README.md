# IoT and ML based Temperature Monitoring and Alerting system
The idea of this project is to monitor the temperature and alerting by sending SMS, when there is sudden changes in the temperature and also displaying the real time temperature on the cloud using which temperature is predicted based on ML models.

## Requirements
- Python
- boltiot

## Accessing the Digital Ocean Droplet
- If you are using Mac OS or Linux, then you can execute the commands on terminal by ssh into the server's IP using following command by replacing the server_ip with your servers IP address,
```
ssh root@server_ip
ssh root@139.59.69.14
```
- If you are using Windows OS, you need to install PuTTY to execute the ssh commands, click [here](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) and choose the windows package according to your windows architecture.
- After installing, open the program and enter the Server's IP address in place of Host name (IP address) in the program and click open.

![putty](https://user-images.githubusercontent.com/92375412/172379515-70f12595-ae8d-4d22-bd3c-353a5ae35ec3.png)

- After clicking on open, enter the host as "root" and enter the password you have created while creating the droplet on digital ocean platform.

![login](https://user-images.githubusercontent.com/92375412/172381401-bb5e1446-f46b-45a8-8d92-264530fdf224.png)

## Steps to execute the python code
- Inside the shell create a directory and add the files, "conf.py" and "final_project.py" in the directory by copying the code from the repository,
```
sudo nano mkdir final_project
cd final_project
sudo nano conf.py
sudo nano final_project.py
```

- before executing the python file "final_project.py", make sure to run the following commands to install packages
```
sudo apt-get update
sudo pip3 install boltiot
sudo pip3 install pyOpenSSL ndg-httpsclient pyasn1
sudo pip3 install 'requests[security]'
```
- Don't forget to link the bolt wifi module to the bolt cloud and replace your own credentials in the "conf.py" file before executing the python file and run the following command to monitor the temperature,
```
sudo python3 final_project.py
```

![final_project](https://user-images.githubusercontent.com/92375412/172387831-685db429-521d-48f8-bfac-189fb7beabe2.png)




# Cyber/WebDev Project
This Project aims to utilise web technologies (Django, VueJS) and other Python libraries to create a web interface that detects 
devices on your local network, showing information such as:

1. IP Address
2. Mac Address
3. Device Vendor
4. Mobile (True/False)
5. Ports Open

In addition the project will also search for most recent vulnerabilities and provide alerts if it detects your local devices is 
vulnerable to such vulnerability. If a vulnerability is detected, information provided will include:

1. CVE number
2. CVSS score
3. Vulnerability Description

The project will also attempt to scan for some common applications on the local device that runs this project, providing similar 
information as above if a vulnerability is detected. Some applications currently being integrated includes:

1. Postgres
2. Mongo
3. Microsoft Office packages (Word, Excel, Powerpoint etc)
4. TeamViewer
5. VNC
6. Zoom
7. More will be added

The project also explores a Microsoft PC configuration dataset in an attempt to use it to provide real time feedback on malware 
infection probability for devices connected on the localnetwork. This is currently in the Jupiter Notebook. Investigation routes 
includes, observing the features, encoding the features where necessary with common techniques like one-hot encoding and feature encoding.
A simple fully connected neural network (NN) is currently being used but still needs to be tuned, traditional ML algorithms will also be 
investigated with.

Lastly the local device behaviour (RAM consumption, CPU usage, etc) will also be in a NN to help determine anomolies on local device.

# Running the prject

To run the web UI:

1. Start the Django project:
   python manage.py 
2. Start the Vue CLI project:
   npm run serve
3. Run the network scanning script:
   From the Django project (where manage.py resides): python manage.py runscript scan
   
Navigate to 127.0.0.8080 for the web UI

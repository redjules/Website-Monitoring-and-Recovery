# Website Monitoring and Recovery

Overview of the project:

<img width="373" alt="image" src="https://github.com/user-attachments/assets/8b76368c-601a-4e13-a20d-353a63ca38c7">


- Create a server on a cloud platform

I have created a Linode server with Debian 11 distribution:

<img width="443" alt="image" src="https://github.com/user-attachments/assets/0cd6eea7-26cd-434d-819d-c6ca689bf2b3">

And add SSH key with this command:

<img width="438" alt="image" src="https://github.com/user-attachments/assets/9f2da3ec-222d-427d-a98f-b35570a9b887">


<img width="468" alt="image" src="https://github.com/user-attachments/assets/0c3d2efb-4b7e-43ac-95e7-0e934c018f6d">


<img width="468" alt="image" src="https://github.com/user-attachments/assets/efa62e96-a98c-45c2-a6eb-58c1c8035345">


We take the ssh root:

<img width="468" alt="image" src="https://github.com/user-attachments/assets/1e3cdf0f-9308-4a05-96f5-1c469bcd9987">

- Install Docker and run a Docker container on the remote server
  
  I have used the following commands to install Docker Engine on Debian:
  
  <img width="468" alt="image" src="https://github.com/user-attachments/assets/ed8df8b3-4e05-454c-a90a-542c7922af3f">
  

  <img width="468" alt="image" src="https://github.com/user-attachments/assets/c6b076b8-4bd0-4781-adbb-14c0032b9d79">
  

  <img width="468" alt="image" src="https://github.com/user-attachments/assets/9e47107a-2875-49ae-9f26-f1497c7a2f25">
  

  <img width="468" alt="image" src="https://github.com/user-attachments/assets/01ca4f4d-09e4-4e79-ac85-20d880747069">

To accesss the public address I have used the Public IP from Linode and port 8080:

<img width="468" alt="image" src="https://github.com/user-attachments/assets/39ba48f6-0c20-43f3-a4fa-2205805f55d5">

Also you cna access using the reverse DNS:

<img width="468" alt="image" src="https://github.com/user-attachments/assets/64038c73-d5f3-4b33-9375-c2efad59b8bf">


- Write a Python script that monitors the website by accessing and validating the HTTP response
 I have used VScode and created th monitor-website.py file:

  <img width="468" alt="image" src="https://github.com/user-attachments/assets/00de4d41-6083-4d4e-9818-33d235e577fe">

- Write a Python script that sends an email notification when website is down

  <img width="350" alt="image" src="https://github.com/user-attachments/assets/3123a39c-e7eb-48d2-b269-3e8335609e17">

- Write a Python script that automatically restarts the application & server the app is down

  The final code is attached to this repo




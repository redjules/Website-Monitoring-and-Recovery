# Website Monitoring and Recovery

Overview of the project:

<img width="373" alt="image" src="https://github.com/user-attachments/assets/8b76368c-601a-4e13-a20d-353a63ca38c7">


- Create a server on a cloud platform

I have created a Linode server with Debian 11 distribution:

<img width="443" alt="image" src="https://github.com/user-attachments/assets/0cd6eea7-26cd-434d-819d-c6ca689bf2b3">

with IP:

<img width="468" alt="image" src="https://github.com/user-attachments/assets/efa62e96-a98c-45c2-a6eb-58c1c8035345">



And add SSH key with this command:

<img width="481" alt="Screenshot 2024-10-08 at 17 49 30" src="https://github.com/user-attachments/assets/56eb9890-b0fd-4a91-b037-aefd3a66ce09">


and fill it with the content of this command:

<img width="384" alt="Screenshot 2024-10-08 at 17 49 40" src="https://github.com/user-attachments/assets/477365f1-9790-43bf-8b4f-fd046d160a9c">


We take the ssh root:

<img width="468" alt="image" src="https://github.com/user-attachments/assets/1e3cdf0f-9308-4a05-96f5-1c469bcd9987">

- Install Docker and run a Docker container on the remote server
  
  I have used the following commands to install Docker Engine on Debian:
  
  <img width="468" alt="image" src="https://github.com/user-attachments/assets/ed8df8b3-4e05-454c-a90a-542c7922af3f">
  

To access the public address I have used the Public IP from Linode and port 8080:

<img width="468" alt="image" src="https://github.com/user-attachments/assets/39ba48f6-0c20-43f3-a4fa-2205805f55d5">

Also you can access using the reverse DNS:

<img width="468" alt="image" src="https://github.com/user-attachments/assets/64038c73-d5f3-4b33-9375-c2efad59b8bf">


- Write a Python script that monitors the website by accessing and validating the HTTP response
 I have used VScode and created the monitor-website.py file:

  <img width="468" alt="image" src="https://github.com/user-attachments/assets/00de4d41-6083-4d4e-9818-33d235e577fe">

- Write a Python script that sends an email notification when website is down:

- We can use less secure app access:

  ![Screenshot 2024-10-08 at 17 57 41](https://github.com/user-attachments/assets/de98c6e0-fcdc-40b0-9379-ec5e3d85aefa)


or App passwords to allow email notifications:

![Screenshot 2024-10-08 at 17 58 21](https://github.com/user-attachments/assets/71d5b96d-ef2a-425f-98d2-7e82a146e9c8)

Updated code:

![Screenshot 2024-10-08 at 17 58 53](https://github.com/user-attachments/assets/3891ea1f-9e30-4c89-8a5d-46fedca00949)

and resulting email notification:

  <img width="350" alt="image" src="https://github.com/user-attachments/assets/3123a39c-e7eb-48d2-b269-3e8335609e17">

- Write a Python script that automatically restarts the application & server the app is down

  The final code is attached to this repo

  I have used the library Paramiko, that allows making SSH connections (client or server) and the library linode_api4.
  Linode_api4 can give us LinodeClient that will make it possible for python to connect to linode and needs a linode token.

  We create an API token in Linode for that:

  ![Screenshot 2024-10-08 at 18 17 31](https://github.com/user-attachments/assets/91130757-2a29-4e63-ba41-7884c0923f80)




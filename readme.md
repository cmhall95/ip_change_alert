# IP Address Check and Notification

## About
Over the past few months I've gotten into self-hosting some services on a home server machine and occasionally like to access it when I'm away from home without exposing too many ports to the open internet and creating a large potential attack surface on my home network. With my current setup I host a Wireguard VPN that I can connect to using my phone, but my ISP gives out dynamic IP addresses and I wanted to create a process that will monitor my public IP and provide an email alert if that changes so I can always have the current value if I need to connect while away. 

Requesting a static IP from my ISP would be another option, but I'm currently in an apartment with at least a couple moves I can already see in my future so I feel like this will be a longer lasting solution that also comes with the benefit of being able to add emails to the list so any friends or family that I create VPN profiles for will also be able to self-service updating their Wireguard config files in the event they need to connect to the Minecraft server I host while I'm not available to assist them directly.

I chose to include the timestamps of the first and most recent observations of an IP address in the event I want to dive into any analytics at a later date, though I can foresee issues if an IP address ever gets reused.

## Setup
If you'd like to use this script you will need to create two files and place them in the same directory:

1. `.env` that will store the credentials for the sender email. I used a newly created gmail account with an app password. Google provides official documentation for setting this up.
    ```csv
    sender_email=
    app_password=
    ```
2. `recipient_emails.txt` which will contain a list of all recipients, one line per email with no delimeter. Example shown below
    ```txt
    recipient1@domain.com
    recipient2@domain.com
    ```
import os

print("Initialising Setup..")
os.system("dnf -y install dnf-plugins-core")
print("Configuring the Repository...")
os.system("dnf config-manager \
    --add-repo \
    https://download.docker.com/linux/fedora/docker-ce.repo")

os.system("dnf install docker-ce --nobest -y")
print("Starting the Services...")
os.system("systemctl start docker")

print("Congratulations !!!")
print("Docker has been installed in your System")

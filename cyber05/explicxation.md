# Explanation of the Subject

## Chapter II: Introduction

The subject introduces the OSI model, which is a conceptual framework used to understand network interactions in seven layers. Each layer has its own vulnerabilities and risks. The focus here is on the network layer, where routers (default gateways) direct traffic. If a network node can impersonate the gateway, it can control, intercept, modify, or block traffic. This is known as ARP spoofing, which can be used maliciously or legitimately (e.g., redirecting users to a registration page in public networks).

## Chapter III: Mandatory Part

The project involves creating a program called "inquisitor" that performs ARP poisoning and monitors FTP traffic. Key requirements include:

- **Platform**: Linux
- **Parameters**: IP and MAC addresses for source and target
- **Protocol**: IPv4 only
- **Error Handling**: Must handle all input errors and not crash unexpectedly
- **Testing**: Must include tests using the FTP protocol

The program must:

- Perform ARP poisoning in both directions (full duplex)
- Restore ARP tables when the attack is stopped (e.g., via CTRL+C)
- Display filenames exchanged between an FTP client and server in real-time

## Chapter IV: Bonus Part

An optional enhancement includes a verbose mode (-v) that shows all FTP traffic, including login details. This bonus will only be assessed if the mandatory part is perfect.

## Documentation and Resources

To successfully complete this project, you should familiarize yourself with the following topics and resources:

### ARP Spoofing and Poisoning:

- [ARP Spoofing - Wikipedia](https://en.wikipedia.org/wiki/ARP_spoofing)
- [ARP Poisoning - OWASP](https://owasp.org/www-community/attacks/ARP_Spoofing)

### OSI Model:

- [OSI Model - Wikipedia](https://en.wikipedia.org/wiki/OSI_model)
- [Understanding the OSI Model - Cisco](https://www.cisco.com/c/en/us/support/docs/osi-model/osi-model.html)

### Libpcap Library:

- [Libpcap Documentation](https://www.tcpdump.org/manpages/pcap.3pcap.html)
- [Libpcap Tutorial](https://www.tcpdump.org/pcap.html)

### Docker and Containers:

- [Docker Documentation](https://docs.docker.com/)
- [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/)
- [Docker Compose Documentation](https://docs.docker.com/compose/)

### Makefile:

- [GNU Make Manual](https://www.gnu.org/software/make/manual/make.html)
- [Makefile Tutorial](https://makefiletutorial.com/)

### FTP Protocol:

- [FTP - Wikipedia](https://en.wikipedia.org/wiki/File_Transfer_Protocol)
- [RFC 959 - FTP](https://tools.ietf.org/html/rfc959)

### Programming Languages:

#### Python:

- [Python Libpcap Bindings](https://pypi.org/project/pylibpcap/)
- [Scapy Documentation](https://scapy.readthedocs.io/en/latest/)

#### C/C++:

- [Libpcap Programming in C](https://www.tcpdump.org/pcap.html)

## Steps to Implement the Project

### Setup Environment:

- Create a Dockerfile and docker-compose.yaml to set up the environment.
- Write a Makefile to automate the setup and execution.

### Develop the Program:

- Implement ARP poisoning using libpcap.
- Ensure the program handles errors gracefully and restores ARP tables on exit.
- Capture and display FTP filenames in real-time.

### Testing:

- Write test cases to validate the program using FTP connections.
- Ensure the program works as expected in various scenarios.

### Bonus Implementation:

- Add a verbose mode to capture and display all FTP traffic, including login details.
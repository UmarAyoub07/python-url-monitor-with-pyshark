import pyshark

def print_http(packet):
    try:
        if packet.http.request_uri:
            print('\n', '*'*50)
            print('New Request: ', packet.ip.dst)
            print('HTTP request URI: ', packet.http.request_uri)
            print('*'*50, '\n')
    except AttributeError:
        pass

def monitor_url(interface='eth0'):
    capture = pyshark.LiveCapture(interface=interface, bpf_filter='tcp port 80 or tcp port 443')

    print("Monitoring URLs on interface:", interface)

    for packet in capture.sniff_continuously():
        print_http(packet)

if __name__=='__main__':
    monitor_url()
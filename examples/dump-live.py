import sys

from impacket.ImpactDecoder import EthDecoder
import pcapy


if __name__ == '__main__':
    if len(sys.argv) <= 3:
        print("usage: dump-live PATH INTERFACE LIMIT")
        sys.exit(1)

    path = sys.argv[1]
    interface = sys.argv[2]
    limit = int(sys.argv[3])

    r = pcapy.open_live(interface, 2**16, True, 1000)
    w = r.dump_open(path)

    def decode_ethernet_payload(header, data):
        w.dump(header, data)
        print(EthDecoder().decode(data))

    r.loop(limit, decode_ethernet_payload)
    w.close()

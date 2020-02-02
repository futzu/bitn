#!/usr/bin/env python

from bitn import BitBin
import sys

PACKET_SIZE=188
SYNC_BYTE=b'\x47'
NON_PTS_STREAM_IDS=[188,190,191,240,241,242,248]

def parse_tsfile(tsfile):
    packetnum=0
    with open(tsfile,'rb') as tsdata:
        while tsdata:
            if tsdata.read(1)==SYNC_BYTE: 
                packet =tsdata.read(PACKET_SIZE - 1)
                if packet: 
                    parse_tspacket(packet,packetnum)
                    packetnum+=1
                else: break
            else: return 

def parse_tspacket(packet,packetnum):
    three_bytes=BitBin(packet[:3])
    tei=three_bytes.asflag(1)
    pusi=three_bytes.asflag(1)
    ts_priority=three_bytes.asflag(1)
    pid=three_bytes.asint(13)
    if pusi: parse_pes(packet,packetnum)

def parse_pes(packet,packetnum): 
    bb=BitBin(packet[3:])
    if bb.asint(24)==1 and bb.asint(8) not in NON_PTS_STREAM_IDS :
        PES_packet_length=bb.asint(16)
        if bb.asint(2)==2:
            bb.asint(6)
            if bb.asint(2) in[2,3]:
                bb.asint(14)
                if bb.asint(4) in[2,3]:
                    to33=bb.asint(3)<<30
                    bb.asflag(1)
                    to30=bb.asint(15) << 15
                    bs.asflag(1)
                    to15=bb.asint(15)
                    d=to33+to30+to15
                    print(f' PTS {d/90000:.6f} on Packet {packetnum}')


if __name__=='__main__':
    try: parse_tsfile(sys.argv[1])
    except: pass

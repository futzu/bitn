#!/usr/bin/env python

from bitslicer9k import Slicer9k
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
    three_bytes=Slicer9k(packet[:3])
    tei=three_bytes.asflag(1)
    pusi=three_bytes.asflag(1)
    ts_priority=three_bytes.asflag(1)
    pid=three_bytes.asint(13)
    if pusi: parse_pes(packet,packetnum)

def parse_pes(packet,packetnum): 
    bs=Slicer9k(packet[3:])
    if bs.asint(24)==1 and bs.asint(8) not in NON_PTS_STREAM_IDS :
        PES_packet_length=bs.asint(16)
        if bs.asint(2)==2:
            bs.asint(6)
            if bs.asint(2) in[2,3]:
                bs.asint(14)
                if bs.asint(4) in[2,3]:
                    to33=bs.asint(3)<<30
                    bs.asflag(1)
                    to30=bs.asint(15) << 15
                    bs.asflag(1)
                    to15=bs.asint(15)
                    d=to33+to30+to15
                    print(f' PTS {d/90000:.6f} on Packet {packetnum}')


if __name__=='__main__':
    try: parse_tsfile(sys.argv[1])
    except: pass

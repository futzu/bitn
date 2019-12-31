# bitslicer9k
Super fast super easy bitslicing. Perfect for mpeg transport streams.

### Instead of this 
```python3
   from struct import unpack
     
    sync,two_bytes,one_byte = unpack('>BHB', packet[:4])
    tei = two_bytes >> 15 
    pusi = two_bytes >> 14 & 0x1
    ts_priority = two_bytes >>13 & 0x1
    pid = two_bytes & 0x1fff
    scramble = one_byte >>6
    afc = (one_byte & 48) >> 4
    count = one_byte & 15
```

### Use bitslicer9k and do this 
```python3
    from bitslicer9k import BitSlicer9k
    
    header= BitSlicer9k(packet[:4])
    sync=header.slice(8)
    tei=header.boolean(1)
    pusi=header.boolean(1)
    ts_priority=header.boolean(1)
    pid=header.slice(13)
    scramble=header.slice(2)
    afc=header.slice(2)
    count=header.slice(4)
    ```

# bitslicer9k
Super fast super easy bitslicing. Perfect for mpeg transport streams.
* bitshift speed with out the bitshift complexity.

#### I used to do this
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
#### Now I use bitslicer9k and do this
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
#### Install
```python3
pip install bitslicer9k
```

#### Help(BitSlicer9k)
```

Help on class BitSlicer9k in module bitslicer9k:

class BitSlicer9k(builtins.object)
 |  BitSlicer9k(bites)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, bites)
 |      From bytes to bits
 |  
 |  boolean(self, num_bits=1)
 |      returns one bit as True or False
 |  
 |  hexed(self, num_bits)
 |      return the hex value of a bitslice
 |  
 |  slice(self, num_bits)
 |      Starting at self.idx of self.bits, slice off num_bits of bits.
 |  
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |  
 |  __dict__
 |      dictionary for instance variables (if defined)
 |  
 |  __weakref__
 |      list of weak references to the object (if defined)

```

#### Usage
  *  Parse  a SCTE 35 splice information section from a hex encoded string

```python3

>>> from bitslicer9k import BitSlicer9k   
    

>>> bites= bytes.fromhex( 'FC302F000000000000FFFFF00506FEAEF17C4C0019021743554549480000077F9F0808000000002CA56C97110000C4876A2E')


>>> class Splice_Info_Section:    
        def __init__(self,bs):
            self.table_id =bs.hexed(8)
            self.section_syntax_indicator = bs.boolean(1)
            self.private = bs.boolean(1)
            self.reserved=bs.slice(2)
            self.section_length = bs.slice(12)
            self.protocol_version = bs.slice(8)
            self.encrypted_packet =  bs.boolean(1)
            self.encryption_algorithm =bs.slice(6)
            self.pts_adjustment = self.time_90k(bs.slice(33))
            self.cw_index = bs.hexed(8)
            self.tier = bs.hexed(12)
            self.splice_command_length = bs.slice(12)
            self.splice_command_type = bs.slice(8)
               
        def time_90k(k):
            t= k/90000.0    
            return f'{t :.6f}'


>>> bs=BitSlicer9k(bites)

>>> sps=Splice_Info_Section(bs)

>>> vars(sps)
{'table_id': '0xfc', 'section_syntax_indicator': False, 'private': False, 'reserved': 3, 
'section_length': 47, 'protocol_version': 0, 'encrypted_packet': False, 'encryption_algorithm': 0, 
'pts_adjustment': '0.000000', 'cw_index': '0xff', 'tier': '0xfff', 'splice_command_length': 5, 
'splice_command_type': 6}

>>> 

```

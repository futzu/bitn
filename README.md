# Bit Slicer 9k
* Super fast bitslicing. 
* bitshift speed without bitwise complexity.

#### Install
```python3
pip install bitslicer9k
```

#### Help(Slicer9k)
```
Help on class Slicer9k in module bitslicer9k:

class Slicer9k(builtins.object)
 |  Slicer9k(bites)
 |  
 |  Methods defined here:
 |  
 |  __init__(self, bites)
 |      From bytes to bits
 |  
 |  as90k(self, num_bits)
 |      return bitslice as 90k time
 |  
 |  asdecodedhex(self, num_bits)
 |      return decoded hex of a bitslice
 |  
 |  asflag(self, num_bits=1)
 |      returns one bit as True or False
 |  
 |  ashex(self, num_bits)
 |      return the hex value of a bitslice
 |  
 |  asint(self, num_bits)
 |      Starting at self.idx of self.bits, slice off num_bits of bits.
 |  
 |  ----------------------------------------------------------------------

```


 I used to do this
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
 Now I use bitslicer9k and do this
```python3
    from bitslicer9k import Slicer9k
    
    header= Slicer9k(packet[:4])
    sync=header.asint(8)
    tei=header.asflag(1)
    pusi=header.asflag(1)
    ts_priority=header.asflag(1)
    pid=header.asint(13)
    scramble=header.asint(2)
    afc=header.asint(2)
    count=header.asint(4)
```

#### Example Usage
  *  Parse  a SCTE 35 splice information section from a hex encoded string

```python3

>>> from bitslicer9k import Slicer9k   
    

>>> bites= bytes.fromhex( 'FC302F000000000000FFFFF00506FEAEF17C4C0019021743554549480000077F9F0808000000002CA56C97110000C4876A2E')


>>> class Splice_Info_Section:    
        def __init__(self,bs):
            self.table_id =bs.ashex(8)
            self.section_syntax_indicator = bs.asflag(1)
            self.private = bs.asflag(1)
            self.reserved=bs.asint(2)
            self.section_length = bs.asint(12)
            self.protocol_version = bs.asint(8)
            self.encrypted_packet =  bs.asflag(1)
            self.encryption_algorithm =bs.asint(6)
            self.pts_adjustment = bs.as90k(33)
            self.cw_index = bs.ashex(8)
            self.tier = bs.ashex(12)
            self.splice_command_length = bs.asint(12)
            self.splice_command_type = bs.asint(8)
      

>>> bs=Slicer9k(bites)

>>> sps=Splice_Info_Section(bs)

>>> vars(sps)

{'table_id': '0xfc', 'section_syntax_indicator': False, 'private': False, 'reserved': 3, 'section_length': 47,
'protocol_version': 0, 'encrypted_packet': False, 'encryption_algorithm': 0, 'pts_adjustment': '0.000000', 
'cw_index': '0xff', 'tier': '0xfff', 'splice_command_length': 5, 'splice_command_type': 6, 'descriptor_loop_length': 25}

>>> 

```

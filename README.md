# bitn.BitBin
* Super fast bitslicing. 
* bitshift speed without bitwise complexity.
# bitn.NBin    (__New!__)
* the __reverse__ bitn.BitBin
* Encodes values to bytes

#### Install
```python3
pip install bitn
```

#### Help(BitBin)
```
NAME
    bitn

CLASSES
    builtins.object
        BitBin
        NBin
    
    class BitBin(builtins.object)
     |  bitn.Bitbin takes a byte string and
     |  converts it to a integer, a very large integer
     |  if needed. A 1500 bit integer is no problem.
     |  several methods are available for slicing off bits.
     |  
     |  Methods defined here:
     |  
     |  __init__(self, bites)
     |  
     |  as90k(self, num_bits)
     |      Returns num_bits
     |      of bits as 90k time
     |  
     |  asascii(self, num_bits)
     |      Returns num_bits
     |      as bytes decoded to ascii
     |  
     |  asflag(self, num_bits=1)
     |      Returns one bit as True or False
     |  
     |  ashex(self, num_bits)
     |      Returns the hex value
     |      of num_bits of bits
     |  
     |  asint(self, num_bits)
     |      Starting at self.idx of self.bits,
     |      slice off num_bits of bits.
     |  
     |  forward(self, num_bits)
     |      Advances the start point
     |      forward by num_bits
     |  
     |  negative_shift(self, num_bits)
     |      negative_shift is called instead of
     |      throwing a negative shift count error.
     |  
     |  ----------------------------------------------------------------------
    
    
    class NBin(builtins.object)
     |  bitn.NBin is
     |  the reverse BitBin.
     |  Encodes data to integers
     |  and then bytes
     |  
     |  Methods defined here:
     |  
     |  __init__(self)
     |  
     |  add_90k(self, pts, bit_len=33)
         |      Converts 90k  float timestamps
     |      to an int and appends it to nbits
     |      via self.add_int
     |  
     |  add_flag(self, flg)
     |      add_flag takes a boolean
     |      value and adds it as an integer
     |      to self.nbits via self.add_int
     |  
     |  add_hex(self, hex_str, bit_len)
     |      add_hex converts a
     |      hex encoded string to an int
     |      and appends it to self.nbits
     |      via self.add_int
     |  
     |  add_int(self, int_bits, bit_len)
     |      left shift nbits and append new_bits
     |  
     |  forward(self, num)
     |      Currently just an alias to reserve
     |  
     |  nbits2bites(self)
     |      nbits2bites converts
     |      the int self.nbits to bytes as self.bites
     |      and sets self.nbits  and self.idx to 0
     |  
     |  reserve(self, num)
     |      reserve sets 'num'  bits to 1
     |      and appends them to self.nbits
     |      via self.add_int
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
 Now I use bitn and do this
```python3
    from bitn import BitBin
    
    header= BitBin(packet[:4])
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

>>> from bitn import BitBin   
    

>>> bites= bytes.fromhex('FC302F000000000000FFFFF00506FEAEF17C4C0019021743554549480000077F9F0808000000002CA56C97110000C4876A2E')

>>> class Splice_Info_Section:

        def __init__(self,bitbin):
            self.table_id =bitbin.ashex(8)
            self.section_syntax_indicator = bitbin.asflag(1)
            self.private = bitbin.asflag(1)
            self.reserved=bitbin.asint(2)
            self.section_length = bitbin.asint(12)
            self.protocol_version = bitbin.asint(8)
            self.encrypted_packet =  bitbin.asflag(1)
            self.encryption_algorithm =bitbin.asint(6)
            self.pts_adjustment = bitbin.as90k(33)
            self.cw_index = bitbin.ashex(8)
            self.tier = bitbin.ashex(12)
            self.splice_command_length = bitbin.asint(12)
            self.splice_command_type = bitbin.asint(8)
      

>>> bitbin=BitBin(bites)

>>> sps=Splice_Info_Section(bitbin)

>>> vars(sps)

{'table_id': '0xfc', 'section_syntax_indicator': False, 'private': False, 'reserved': 3, 'section_length': 47,
'protocol_version': 0, 'encrypted_packet': False, 'encryption_algorithm': 0, 'pts_adjustment': '0.000000', 
'cw_index': '0xff', 'tier': '0xfff', 'splice_command_length': 5, 'splice_command_type': 6, 'descriptor_loop_length': 25}

>>> 

```


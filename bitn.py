class BitBin:
    def __init__(self,bites):
        '''
        From bytes to bits
        '''
        if not isinstance(bites,bytes):
            raise TypeError('bites needs to be type bytes')
        self.bitsize = self.idx = (len(bites)*8)
        self.bits=int.from_bytes(bites,byteorder='big')

    def as90k(self,num_bits):
        '''
        Returns num_bits 
        of bits as 90k time
        ''' 
        return f'{ (self.asint(num_bits)/90000):.6f}'
          
    def asint(self,num_bits):
        '''
        Starting at self.idx of self.bits, 
        slice off num_bits of bits.
        ''' 
        if num_bits > self.idx:
            raise ValueError(f'reading {num_bits - self.idx} bits too many')
        else:
            self.idx =  self.idx-num_bits
            return (self.bits >> (self.idx)) & ~(~0 << num_bits)
             
    def ashex(self,num_bits):
        '''
        Returns the hex value 
        of num_bits of bits
        '''
        return hex(self.asint(num_bits))
   
    def asdecodedhex(self,num_bits):
        '''
        Returns num_bits of bits 
        from hex decoded to bytes 
        '''
        k= self.asint(num_bits)
        return bytearray.fromhex(hex(k)[2:]).decode()   
                
    def asflag(self,num_bits=1):
        '''
        Returns one bit as True or False
        '''
        return  self.asint(num_bits) == 1

    def forward(self,num_bits):
        '''
        Advances the start point 
        forward by num_bits
        '''
        self.idx -= num_bits
        if self.idx < 0:
            self.idx = 0
                
    def rewind(self,num_bits):
        '''
        Rewinds the start point 
        back by num_bits
        '''  
        self.idx += num_bits
        if self.idx > self.bitsize:
            self.idx = self.bitsize

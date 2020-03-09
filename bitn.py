class BitBin:
    def __init__(self,bites):
        '''
        From bytes to bits.
        '''
        lb=len(bites) << 3
        self.bitsize =  lb
        self.idx = lb
        self.bits = int.from_bytes(bites,byteorder='big')

    def as90k(self,num_bits):
        '''
        Returns num_bits 
        of bits as 90k time
        '''
        t = (self.asint(num_bits)/90000.00)
        return f'{t:.06f}'
          
    def asint(self,num_bits):
        '''
        Starting at self.idx of self.bits, 
        slice off num_bits of bits.
        ''' 
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
        k = self.asint(num_bits)
        return bytearray.fromhex(hex(k)[2:]).decode()   
                
    def asflag(self,num_bits=1):
        '''
        Returns one bit as True or False
        '''
        self.idx -= num_bits
        return  (self.bits >> self.idx) & 1 == 1

    def forward(self,num_bits):
        '''
        Advances the start point 
        forward by num_bits
        '''
        self.idx -= num_bits
                
    def rewind(self,num_bits):
        '''
        Rewinds the start point 
        back by num_bits
        '''  
        self.idx += num_bits
        if self.idx > self.bitsize:
            self.idx = self.bitsize

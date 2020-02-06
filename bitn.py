class BitBin:
    def __init__(self,bites):
        '''
        From bytes to bits
        '''
        if not isinstance(bites,bytes):
            raise TypeError('bites needs to be type bytes')
        self.idx=(len(bites)*8)
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
        bitslice= (self.bits >> (self.idx-num_bits)) & ~(~0 << num_bits)
        self.forward(num_bits)
        return bitslice 

        
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
        return  self.asint(num_bits) ==1


    def forward(self,num_bits):
        '''
        Advances the start point 
        forward by num_bits
        '''
        self.idx -=num_bits
        
        
    def rewind(self,numbits):
        '''
        Rewinds the start point 
        back by num_bits
        '''
        self.idx +=num_bits
        return bitslice as 90k time
        ''' 
    
        return f'{ (self.asint(num_bits)/90000):.6f}'

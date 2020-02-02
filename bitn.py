class BitBin:
    def __init__(self,bites):
        '''
        From bytes to bits
        '''
        if not isinstance(bites,bytes):
            raise TypeError('bites needs to be type bytes')
        self.idx=(len(bites)*8)
        self.bits=int.from_bytes(bites,byteorder='big')
           
    def asint(self,num_bits):
        '''
        Starting at self.idx of self.bits, slice off num_bits of bits.
        ''' 
        bitslice= (self.bits >> (self.idx-num_bits)) & ~(~0 << num_bits)
        self.idx -=num_bits
        return bitslice 
        
    def ashex(self,num_bits):
        '''
        return the hex value of a bitslice
        '''
        return hex(self.asint(num_bits))
        
    def asdecodedhex(self,num_bits):
        '''
        return decoded hex of a bitslice
        '''
        k= self.asint(num_bits)
        return bytearray.fromhex(hex(k)[2:]).decode()   
        
    def asflag(self,num_bits=1):
        '''
        returns one bit as True or False
        '''
        return  self.asint(num_bits) ==1


    def as90k(self,num_bits):
        '''
        return bitslice as 90k time
        ''' 
    
        return f'{ (self.asint(num_bits)/90000):.6f}'

import sys


class BitBin:
    """
    bitn.Bitbin takes a byte string and
    converts it to a integer, a very large integer
    if needed. A 1500 bit integer is no problem.
    several methods are available for slicing off bits.
    """

    def __init__(self, bites):
        self.bites = bites
        self.bitsize = self.idx = len(bites) << 3
        self.bits = int.from_bytes(bites, byteorder="big")

    def as90k(self, num_bits):
        """
        Returns num_bits
        of bits as 90k time
        """
        ninetyk = self.asint(num_bits) / 90000.00
        return round(ninetyk, 6)

    def asint(self, num_bits):
        """
        Starting at self.idx of self.bits,
        slice off num_bits of bits.
        """
        if self.idx >= num_bits:
            self.idx -= num_bits
            return (self.bits >> (self.idx)) & ~(~0 << num_bits)
        else:
            self.negative_shift(num_bits)

    def ashex(self, num_bits):
        """
        Returns the hex value
        of num_bits of bits
        """
        return hex(self.asint(num_bits))

    def asdecodedhex(self, num_bits):
        """
        Returns num_bits of bits
        from hex decoded to bytes
        """
        k = self.asint(num_bits)
        return bytearray.fromhex(hex(k)[2:]).decode()

    def asflag(self, num_bits=1):
        """
        Returns one bit as True or False
        """
        return self.asint(num_bits) & 1 == 1

    def forward(self, num_bits):
        """
        Advances the start point
        forward by num_bits
        """
        self.idx -= num_bits

    def negative_shift(self, num_bits):
        """
        negative_shift is called instead of
        throwing a negative shift count error.
        """
        print(
            f"{num_bits} bits requested, but only {self.idx} bits left.",
            file=sys.stderr,
        )
        print(f"self.bites:\n{self.bites}", file=sys.stderr)
        sys.exit()

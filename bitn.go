package bitn

import (
	"encoding/hex"
	"fmt"
	"log"
	"math/big"
)

// Bitn converts bytes to a list of bits.
type Bitn struct {
	idx  uint
	bits string
}

// Load raw bytes and convert to bits
func (b *Bitn) Load(bites []byte) {
	i := new(big.Int)
	i.SetBytes(bites)
	b.bits = fmt.Sprintf("%b", i)
	b.idx = 0
}

// Chunk slices bitcount of bits and returns it as a uint64
func (b *Bitn) Chunk(bitcount uint) uint64 {
	j := new(big.Int)
	d := b.idx + bitcount
	j.SetString(b.bits[b.idx:d], 2)
	b.idx = d
	//fmt.Printf("bitidx: %v\n", b.idx)
	return j.Uint64()
}

// AsUInt64 is a wrapper for Chunk
func (b *Bitn) AsUInt64(bitcount uint) uint64 {
	asuint64 := b.Chunk(bitcount)
	return asuint64
}
// AsUInt8 is a  uint8 wrapper for Chunk
func (b *Bitn) AsUInt8(bitcount uint) uint8 {
	asuint8 := uint8(b.Chunk(bitcount))
	return asuint8
}
// AsUInt16 is a uint16 wrapper for Chunk
func (b *Bitn) AsUInt16(bitcount uint) uint16 {
	asuint16 := uint16(b.Chunk(bitcount))
	return asuint16
}
// AsUInt32 is a uint32 wrapper for Chunk
func (b *Bitn) AsUInt32(bitcount uint) uint32 {
	asuint32 := uint32(b.Chunk(bitcount))
	return asuint32
}

// AsBool slices 1 bit and returns true for 1 , false for 0
func (b *Bitn) AsBool() bool {
	var bitcount uint
	bitcount = 1
	boo := (b.Chunk(bitcount) == 1)
	return boo
}

// AsFloat slices bitcount of bits and returns as float64
func (b *Bitn) AsFloat(bitcount uint) float64 {
	asfloat := float64(b.Chunk(bitcount))
	return asfloat
}

// As90k is AsFloat / 90000.00
func (b *Bitn) As90k(bitcount uint) float64 {
	as90k := b.AsFloat(bitcount) / 90000.00
	return as90k
}

// AsHex slices bitcount of bits and returns as hex string
func (b *Bitn) AsHex(bitcount uint) string {
	ashex := fmt.Sprintf("%#x", b.Chunk(bitcount))
	return ashex
}

// AsDeHex slices bitcount of bits and returns as hex string
func (b *Bitn) AsDeHex(bitcount uint) []byte {
	ashex := fmt.Sprintf("%x", b.Chunk(bitcount))
	asdehex, err := hex.DecodeString(ashex)
	if err != nil {
		log.Fatal(err)
	}
	return asdehex
}

// Forward advances b.idx by bitcount
func (b *Bitn) Forward(bitcount uint) {
	b.idx += bitcount
}



type Nbin struct {
	Bites big.Int
}

// Add bytes to NBin.Bites for encoding
func (nb *Nbin) AddBytes(str string, nbits uint) {
	t := new(big.Int)
	t.SetBytes([]byte(str))
	o := nb.Bites.Lsh(&nb.Bites, nbits)
	nb.Bites = *nb.Bites.Add(o, t)
}

// Add64 left shift NBin.Bites by nbits and add uint64 val
func (nb *Nbin) Add64(val uint64, nbits uint) {
	t := new(big.Int)
	t.SetUint64(val)
	o := nb.Bites.Lsh(&nb.Bites, nbits)
	nb.Bites = *nb.Bites.Add(o, t)
}

// Add32 left shift NBin.Bites by nbits and add uint32 val
func (nb *Nbin) Add32(val uint32, nbits uint) {
	u := uint64(val)
	nb.Add64(u, nbits)
}

// Add16 left shift NBin.Bites by nbits and add uint16 val
func (nb *Nbin) Add16(val uint16, nbits uint) {
	u := uint64(val)
	nb.Add64(u, nbits)
}

// Add8 left shift NBin.Bites by nbits and add uint8 val
func (nb *Nbin) Add8(val uint8, nbits uint) {
	u := uint64(val)
	nb.Add64(u, nbits)
}

// AddFlag left shift NBin.Bites by 1 and add bool val
func (nb *Nbin) AddFlag(val bool) {
	if val == true {
		nb.Add64(1, 1)
	} else {
		nb.Add64(0, 1)
	}
}

// Add90k left shift NBin.Bites by nbits and add val as ticks
func (nb *Nbin) Add90k(val float64, nbits uint) {
	u := uint64(val * float64(90000.0))
	nb.Add64(u, nbits)
}

// AddHex64 left shift NBin.Bites by nbits and add hex string as uint64
func (nb *Nbin) AddHex64(val string, nbits uint) {
	u := new(big.Int)
	_, err := fmt.Sscan(val, u)
	if err != nil {
		fmt.Println("error scanning value:", err)
	} else {
		fmt.Println(u.Uint64())
		nb.Add64(u.Uint64(), nbits)
	}
}


// Reserve num bits by setting them to 1
func (nb *Nbin) Reserve(num int) {

    	for i := 0; i < num; i++ {
		nb.Add64(1, 1)
    }
}
        

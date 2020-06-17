package gobit

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

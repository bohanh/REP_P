package main;

import (
	"math/big"
	"fmt"
)

func fib(n uint64) *big.Int {
	if n < 2 {
		return big.NewInt(int64(n))
	}
	a, b := big.NewInt(0), big.NewInt(1)
	for n--; n > 0; n-- {
		a.Add(a, b)
		a, b = b, a
	}
	return b
}

func main() {
	fmt.Println(fib(100))
}
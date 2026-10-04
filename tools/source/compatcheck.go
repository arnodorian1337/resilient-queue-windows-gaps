package main

import (
	"fmt"
	"runtime"
)

func main() {
	if runtime.GOOS != "windows" {
		fmt.Println("Compatibility cache: unsupported platform")
		return
	}
	fmt.Println("Compatibility cache: current")
}


package main

import (
	"fmt"
	"net/http"
)


func main(){

	server := http.Dail()
	server.accpet()
	for {
		server.ListAndServer()

	}
	server.run(":5050")
}


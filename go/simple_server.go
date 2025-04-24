package main

import (
    "fmt"
    "log"
    "net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
    fmt.Fprintln(w, "Hello from Go!")
}

func main() {
    http.HandleFunc("/", handler)
    fmt.Println("Server starting at http://localhost:8080")
    log.Fatal(http.ListenAndServe(":8080", nil))
}

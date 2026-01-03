// *Summary: Lamport Timestamps are a logical clock that can be used to order events in a distributed system.
// *Ideally in production environment, you would want to use a message bus to handle this, but we just mimic this behaviour here.
package main

import (
	"fmt"
	"sync"
)

type Message struct {
	SenderID  string
	Timestamp int
	Data      string
}

type Process struct {
	ID      string
	counter int
	mu      sync.Mutex
}

func NewProcess(id string) *Process {
	return &Process{ID: id, counter: 0}
}

func (p *Process) LocalEvent() {
	p.mu.Lock()
	defer p.mu.Unlock()
	p.counter++
	fmt.Printf("Process %s: Local event at timestamp %d\n", p.ID, p.counter)
}

func (p *Process) SendMessage(data string) Message {
	p.mu.Lock()
	defer p.mu.Unlock()
	p.counter++
	msg := Message{
		Data:      data,
		Timestamp: p.counter,
		SenderID:  p.ID,
	}
	fmt.Printf("Process %s: Sent message %s at timestamp %d\n", p.ID, msg.Data, msg.Timestamp)
	return msg
}

func (p *Process) ReceiveMessage(message Message) {
	p.mu.Lock()
	defer p.mu.Unlock()

	if message.Timestamp > p.counter {
		p.counter = message.Timestamp
	}

	p.counter++

	fmt.Printf("Process %s: Received message %s from %s at timestamp %d\n", p.ID, message.Data, message.SenderID, p.counter)
}

func TestConcurrentSends() {
	A := NewProcess("A")
	B := NewProcess("B")
	C := NewProcess("C")

	A.counter = 5
	B.counter = 5
	C.counter = 5

	msgAtoB := A.SendMessage("A->B")
	msgBtoC := B.SendMessage("B->C")
	msgCtoA := C.SendMessage("C->A")

	C.ReceiveMessage(msgAtoB)

	B.ReceiveMessage(msgAtoB)
	A.ReceiveMessage(msgCtoA)

	C.ReceiveMessage(msgBtoC)

	fmt.Printf("\nFinal state: A=%d, B=%d, C=%d\n", A.counter, B.counter, C.counter)
}

func main() {
	A := NewProcess("A")
	B := NewProcess("B")
	C := NewProcess("C")

	A.LocalEvent()

	msg1 := A.SendMessage("Hello from A")
	B.ReceiveMessage(msg1)

	msg2 := B.SendMessage("Hello from B")
	C.ReceiveMessage(msg2)

	msg3 := C.SendMessage("Hello from C")
	A.ReceiveMessage(msg3)

	fmt.Printf("\nFinal state: A=%d, B=%d, C=%d\n", A.counter, B.counter, C.counter)

	TestConcurrentSends()
}

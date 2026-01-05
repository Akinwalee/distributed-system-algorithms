## Lamport Timestamps from first Principles

Hardware variations, software and OS delays, as well as accumulated drifts are some of the prominent reasons why “time” is different from one machine to the other. An implication of this is that no two computers necessarily have the same timestamp at a particular instance in time.

In modern systems where computation is done across multiple different computers, this is a big problem.


Suppose Alice and Bob are friends. Alice lives in Paris and Bob in London, chatting in their WhatsApp DM. Alice’s phones 2 seconds faster and Bob’s is 2 seconds slow.

> Alice sends a joke: “_Why did the functions stop calling each other_”

Alice’s local time: `1:00:05`

> Then immediately, Alice sends the punchline: “_Because they had too many arguments_”

Alices’ local time: `1:00:06`

> Bob receives the joke and punchline and: “_LOL!_”

Bob’s local time: `1:00:03`


In the chat history, the system tries to order all events by timestamp:
- Bob’s “LOL!” At time `1:00:03`
- Alices joke at time `1:00:05`
- Alice’s punchline at time `1:00:06`

According to the timestamp alone, the history makes no sense. Bob's response appears to come before Alice's joke, even though Bob's response was causally dependent on receiving Alice's messages.

**To put the problem a bit formally:**

In a single computer, the CPU clock tells us that Event A happened before Event B without confusion. In a distributed system, clocks on different servers are not universally synchronous. If Server A sends a message at `10:00:01` and Server B receives it at `10:00:00` (according to its own clock), thereby leading to confusion that can break the system because an effect happened before it’s cause.

Instead of relying on the physical clocks, the American computer scientist and 2013 Turing Award winner, Leslie Lamport proposed a logical clock algorithm.

### The Lamport Algorithm

Lamport defined the “Happened-Before” relation (`->`) as follows:
1. If `a` and `b` are in the same process and `a` comes before `b`, then `a -> b`
2. If `a` is the sending of `a` message and `b` is the receipt of that message, then `a -> b`
3. If `a -> b` and `b -> c`, then `a -> c`

In other words, the happened-before relation is the smallest relation that satisfies program partial order, message causality, and transitive closure.


Casuality here means possible influence. That is, event `a` is casual to event `b` if information from `a` could have affected `b`.
Transitive closure is the extension of causality. That is, if event `a` can influence event `b`, and event `b` can influence event `c`, then `a` can influence `c` (this means exactly the same as the transitivity and closure properties from your maths class).



### The Algorithm Rules

The Lamport algorithm defines 3 kinds of events, tying to 3 rules:

#### Rule 1: Local Events

Whenever a process performs an internal action (doing a calculation, writing to disk…), it increments it’s local timestamp counter:

```nginx
timestamp = timestamp + 1
```

#### Rule 2: Sending a Message

When a process sends a message, it first increments its local counter and the attaches that value to the message:

```nginx
timestamp = timestamp + 1
```

**Payload:** `Message(data, timestamp = timestamp)`

#### Rule 3: Recieving a Message

When a process receives a message with a timestamp `T`, it must update its own local counter to ensure that it’s future events have a higher timestamp than the past event it just received:

```nginx
timestamp = max(timestamp, T) + 1
```

If an event `a` happened before event `b`, then the Lamport timestamp of a will be less than that of `b`: `timestamp(a) < timestamp(B)`.


### Applying Lamport Timestamps to Our Example

Instead of looking at their phone’s clock, WhatsApp uses a logical clock (the Lamport timestamp).

> Alice sends the joke
She increments her counter from 0 to 1
The final message sent is: Message(Joke, timestamp = 1)

> Alice sends the punchline
She increments her counter from 1 to 2
The final message sent is: Message(Punchline, timestamp = 2)

> Bob receives the joke
Bob’s current counter is 0 but received Message(Joke, timestamp = 1)
Bob updates his timestamp: timestamp = max(0, 1) + 1 = 2

> Bob receives the punchline
Bob’s current counter is 2 and he receives Message(Punchline, timestamp = 2)
Bob updates his timestamp: timestamp = max(2, 2) + 1 = 3

> Bob sends his reaction
He increments his counter from 3 to 4
The final message sent is: Message(Response, timestamp = 4)

Even though Bob’s physical clock was behind, the Lamport algorithm forced his clock to jump ahead and record the events correctly.


### Python implementation 

[Here's an implemnetation in Python](implementation.py)


This logical timestamp helps keep things in order and it’s used to:
- Ensure that a “”Delete” operation doesn’t happened before the “Insert” operation in a districbuted database.
- Track which commit came after another in a distributed history management system like Git.
- Make sure that a player is “hit” only after a bullet is “fired” in a video game.
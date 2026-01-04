import threading
import queue


class LamportClock:
    def __init__(self, node_id: str):
        self.value = 0
        self.node_id = node_id
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.value += 1
            return self.value
        
    def update(self, timestamp):
        with self.lock:
            self.value = max(self.value, timestamp) + 1
            return self.value
        
    def __str__(self) -> str:
        return f"{self.node_id} at Time: {self.value}"
        
    
def process(node_id: str, queues: dict, actions: list):
    clock = LamportClock(node_id)
    my_queue = queues[node_id]

    for action in actions:
        if action['type'] == 'send':
            timestamp = clock.increment()
            message = {
                "data": action['data'],
                "timestamp": timestamp
            }
            print(f"{clock} sennding: {message.get('data')}")
            queues[action['to']].put(message)

        elif action['type'] == 'receive':
            message = my_queue.get()
            clock.update(message['timestamp'])
            print(f"{clock} received: {message.get('data')} sent at time {message.get('timestamp')}")
        
        elif action['type'] == 'local':
            clock.increment()
            print(f"{clock} performed local action: {action.get('data', '')}")


if __name__ == '__main__':
    alice_actions = [
    {'type': 'local', 'data': 'computing the number of stars in the universe...'},
    {'type': 'send', 'to': 'Bob', 'data': 'Why did the functions stop calling each other?'},
    {'type': 'send', 'to': 'Bob', 'data': 'Because they had too many arguments'}
    ]

    bob_actions = [
        {'type': 'receive'},
        {'type': 'local', 'data': 'solving climate change...'},
        {'type': 'receive'},
        {'type': 'send', 'to': 'Alice', 'data': 'LOL!'}
    ]

    queues = {
        "Alice": queue.Queue(),
        "Bob": queue.Queue()
    }

    alice_thread = threading.Thread(target=process, args=("Alice", queues, alice_actions))
    bob_thread = threading.Thread(target=process, args=("Bob", queues, bob_actions))

    alice_thread.start()
    bob_thread.start()
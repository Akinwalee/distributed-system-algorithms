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
        
    
def process(node_id: str, queues: dict, peer_id: str):
    clock = LamportClock(node_id)
    my_queue = queues[node_id]

    clock.increment()
    print(f"{clock} performed local action")

    if node_id == 'Alice':
        for msg in ["Why did the functions stop calling one another?","Because they had too many arguments"]:
            timestamp = clock.increment()
            message = {
                "data": msg,
                "timestamp": timestamp
            }
            print(f"{clock} sennding: {message.get('data')}")
            queues[peer_id].put(message)

    if node_id == 'Bob':
        message = my_queue.get()
        clock.update(message['timestamp'])
        print(f"{clock} received: {message.get('data')} sent at time {message.get('timestamp')}")

        message = my_queue.get()
        clock.update(message['timestamp'])
        print(f"{clock} received: {message.get('data')} sent at time {message.get('timestamp')}")


queues = {
    "Alice": queue.Queue(),
    "Bob": queue.Queue()
}

first_thread = threading.Thread(target=process, args=("Alice", queues, "Bob"))
second_thread = threading.Thread(target=process, args=("Bob", queues, "Alice"))

first_thread.start()
second_thread.start()
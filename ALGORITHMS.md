# 98 Distributed System Algorithms

## Core Consensus & Coordination

- [ ] 1. **Paxos** - Consensus algorithm for achieving agreement among distributed nodes despite failures.
- [ ] 2. **Raft** - Leader-based consensus protocol that is easier to understand than Paxos.
- [ ] 3. **Gossip Protocol** - Nodes periodically share state information to propagate updates efficiently.
- [ ] 4. **Two-Phase Commit** - Ensures atomic commitment across distributed transactions.
- [ ] 5. **Three-Phase Commit** - Improved 2PC to reduce blocking in case of failures.
- [ ] 6. **Vector Clocks** - Mechanism to capture causality between events in distributed systems.
- [x] 7. **Lamport Timestamps** - Logical clocks that order events in a distributed system.
- [ ] 8. **Chandy-Lamport Snapshot** - Algorithm to record a consistent global state of a distributed system.
- [ ] 9. **Bullying Algorithm** - Leader election algorithm based on node IDs.
- [ ] 10. **Ring Algorithm** - Leader election algorithm where nodes form a logical ring.
- [ ] 11. **Bully Election Algorithm** - Alternative leader election strategy to handle failures.

## P2P & DHT Protocols

- [ ] 12. **Chord** - Structured P2P protocol using consistent hashing.
- [ ] 13. **Pastry** - Scalable distributed hash table (DHT) for routing in P2P networks.
- [ ] 14. **Kademlia** - Efficient DHT protocol using XOR metric for node distance.
- [ ] 15. **Tapestry** - Overlay network for scalable routing in distributed systems.
- [ ] 16. **Salsa** - Structured overlay for distributed object location.

## Data Processing & Storage

- [ ] 17. **MapReduce** - Distributed computation framework for processing large datasets.
- [ ] 18. **Spark RDDs** - Resilient distributed datasets for fault-tolerant parallel processing.
- [ ] 19. **Merkle Trees** - Data structure for efficient verification of distributed data.

## Byzantine & Fault Tolerance

- [ ] 20. **Byzantine Fault Tolerance (BFT)** - Consensus protocol tolerant to malicious nodes.
- [ ] 21. **Practical BFT (PBFT)** - Optimized BFT protocol for practical distributed systems.
- [ ] 22. **Zab** - Atomic broadcast protocol used by ZooKeeper for consistency.

## Replication Strategies

- [ ] 23. **Quorum-based Replication** - Ensures consistency by requiring a quorum of nodes for operations.
- [ ] 24. **Chain Replication** - High-throughput replication protocol using chains.
- [ ] 25. **Primary-Backup Replication** - One node acts as primary, others as backups for reliability.
- [ ] 26. **Read-One Write-All** - Writes go to all replicas, reads from one for simplicity.
- [ ] 27. **Quorum Reads/Writes** - Reads and writes require a majority to ensure consistency.
- [ ] 28. **Viewstamped Replication** - Replication protocol similar to Paxos for high availability.
- [ ] 29. **Raft Log Replication** - Leader replicates logs to followers for fault tolerance.

## CRDTs & Eventual Consistency

- [ ] 30. **CRDTs** - Conflict-free replicated data types for eventual consistency.
- [ ] 31. **G-Set CRDT** - Grow-only set that ensures eventual consistency.
- [ ] 32. **OR-Set CRDT** - Observed-remove set that allows additions and removals.
- [ ] 33. **Logoot** - CRDT for collaborative text editing.
- [ ] 34. **Bayou** - Weakly consistent replicated database with eventual consistency.
- [ ] 35. **Anti-Entropy Protocol** - Reconciles divergent replicas to achieve eventual consistency.

## Mutual Exclusion & Locking

- [ ] 36. **Skeen's Algorithm** - Total ordering of messages in distributed systems.
- [ ] 37. **Ricart-Agrawala Algorithm** - Mutual exclusion using message passing.
- [ ] 38. **Maekawa's Algorithm** - Mutual exclusion using voting subsets.
- [ ] 39. **Token Ring Mutual Exclusion** - Distributed mutual exclusion using a circulating token.
- [ ] 40. **Lease-based Locking** - Locks with timeouts to prevent indefinite blocking.
- [ ] 41. **Deterministic Locking** - Prevents deadlocks using deterministic lock ordering.

## Transaction & Commit Protocols

- [ ] 42. **Paxos Commit** - Extends Paxos for distributed transaction commits.
- [ ] 43. **Chain-based Atomic Commit** - Commit protocol using a chain of nodes.

## Group Communication

- [ ] 44. **Virtual Synchrony** - Ensures consistent group communication among nodes.
- [ ] 45. **Atomic Broadcast** - Ensures all nodes deliver messages in the same order.
- [ ] 46. **Reliable Broadcast** - Guarantees message delivery to all nodes despite failures.
- [ ] 47. **Total Order Broadcast** - Delivers messages to all nodes in identical order.
- [ ] 48. **FIFO Broadcast** - Messages from a sender are delivered in order sent.
- [ ] 49. **Causal Broadcast** - Messages delivered respecting causal dependencies.
- [ ] 50. **Reliable Multicast** - Ensures all intended recipients get a message reliably.

## Membership & Failure Detection

- [ ] 51. **Dynamic Membership** - Handles nodes joining or leaving a distributed system.
- [ ] 52. **ZooKeeper Atomic Broadcast (ZAB)** - Protocol for reliable coordination and consistency.
- [ ] 53. **Gossip-style Membership** - Nodes learn about others using periodic gossip messages.
- [ ] 54. **Heartbeat Failure Detection** - Detects failed nodes by periodic heartbeat messages.
- [ ] 55. **SWIM Protocol** - Scalable weakly-consistent infection-style process group membership.
- [ ] 56. **Ring-based Failure Detection** - Monitors nodes in a ring topology for failures.

## Advanced Consensus

- [ ] 57. **Vector Consensus** - Consensus that preserves vector timestamps for causality.
- [ ] 58. **Egalitarian Paxos (EPaxos)** - Leaderless consensus for low-latency replication.
- [ ] 59. **Paxos Lease** - Leader leases using Paxos for dynamic leadership.

## Load Distribution

- [ ] 60. **Consistent Hashing** - Distributes keys uniformly across nodes to handle scaling.

## Information Dissemination

- [ ] 61. **Epidemic Algorithms** - Probabilistic methods for information dissemination.
- [ ] 62. **Flooding Algorithm** - Simple message propagation to all nodes.
- [ ] 63. **Random Walk Algorithm** - Message propagation via random walks in a network.
- [ ] 64. **Scuttlebutt Protocol** - Peer-to-peer gossip protocol for anti-entropy.

## Message Ordering

- [ ] 65. **Message Ordering with Sequencers** - Central sequencer enforces message order.

## Snapshots & Recovery

- [ ] 66. **Atomic Snapshot** - Captures consistent distributed state atomically.
- [ ] 67. **Checkpointing** - Records periodic system states for recovery.
- [ ] 68. **Rollback Recovery** - Restores system to previous checkpoint after failure.
- [ ] 69. **Raft Snapshotting** - Compresses logs by periodically taking snapshots.

## Clock & Time Synchronization

- [ ] 70. **Hybrid Logical Clocks** - Combines logical and physical clocks for causality.
- [ ] 71. **Google Spanner TrueTime** - Globally synchronized clock for strong consistency.
- [ ] 72. **Vector Clock Compression** - Efficiently encodes vector clocks to reduce size.

---

## Additional 28 Algorithms

## Advanced Consensus & Coordination

- [ ] 73. **Multi-Paxos** - Optimized Paxos variant for multiple consensus rounds with stable leader.
- [ ] 74. **Fast Paxos** - Reduces message delays in Paxos by allowing coordinators to bypass leaders.
- [ ] 75. **Flexible Paxos** - Generalizes quorum requirements for different phases of Paxos.
- [ ] 76. **Mencius** - Multi-leader consensus protocol for high throughput.
- [ ] 77. **HoneyBadgerBFT** - Asynchronous BFT consensus with optimal resilience.
- [ ] 78. **Tendermint** - Byzantine consensus protocol used in blockchain systems.
- [ ] 79. **Hotstuff** - Linear-view-change BFT protocol with improved efficiency.

## Advanced Replication

- [ ] 80. **Active Replication** - All replicas execute operations simultaneously.
- [ ] 81. **Passive Replication** - Primary executes, then updates backups.
- [ ] 82. **State Machine Replication** - Replicas maintain identical state machines.
- [ ] 83. **Replicated State Machine** - Deterministic state machines replicated across nodes.
- [ ] 84. **Multi-Primary Replication** - Multiple nodes can accept writes simultaneously.

## Distributed Transactions

- [ ] 85. **Calvin** - Deterministic database with distributed transaction support.
- [ ] 86. **Percolator** - Distributed transaction system built on Bigtable.
- [ ] 87. **MVCC (Multi-Version Concurrency Control)** - Transaction isolation using versioning.
- [ ] 88. **Optimistic Concurrency Control** - Validates transactions at commit time.
- [ ] 89. **Snapshot Isolation** - Provides consistent view of data for transactions.

## Clock & Causality

- [ ] 90. **Dotted Version Vectors** - Compact causality tracking for concurrent updates.
- [ ] 91. **Interval Tree Clocks** - Dynamic causality tracking without prior knowledge of participants.
- [ ] 92. **Matrix Clocks** - Captures transitive causality information.

## Load Balancing & Partitioning

- [ ] 93. **Range Partitioning** - Divides data by key ranges across nodes.
- [ ] 94. **Hash Partitioning** - Distributes data using hash functions.
- [ ] 95. **Virtual Nodes (VNodes)** - Improves load distribution in consistent hashing.
- [ ] 96. **Rendezvous Hashing** - Minimal disruption hashing for distributed caches.

## Coordination Services

- [ ] 97. **Lock Service (Chubby)** - Google's distributed lock service for coordination.
- [ ] 98. **Lease Protocol** - Time-bound resource reservation in distributed systems.

- [ ] 99. **Gossip-based Aggregation** - Computes distributed aggregates (sum, average, count) using gossip protocols without centralized coordination.
- [ ] 100. **Conflict-free Replicated JSON (Automerge)** - CRDT-based algorithm for collaborative editing of JSON documents with automatic conflict resolution.
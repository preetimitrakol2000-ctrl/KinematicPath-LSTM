# KinematicPath-LSTM

A pure Python data structuring pipeline engineered to handle chaotic trajectory tracking signals. This framework bypasses standard array limits, packaging sequence paths into an explicit **Doubly Linked List** to maintain clean historical vectors for downstream kinematics prediction engines.

## ⚡ Data Structure Properties
* **Data Layout:** Bi-directional Doubly Linked List tracking spatial locations.
* **Time Complexity:** Constant-time $O(1)$ coordinate insertions and historical data deletions.

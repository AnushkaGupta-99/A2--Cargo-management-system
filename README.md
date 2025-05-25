# A2--Cargo-management-system
Galactic Cargo Management System (GCMS)
This project implements an efficient cargo bin packing system for interstellar logistics using two classical algorithms:

Compact Fit Algorithm (CFA): Used for Blue and Yellow cargo. It assigns an object to the bin with the smallest sufficient remaining capacity. In case of ties, Blue selects the least bin ID, and Yellow selects the greatest bin ID.

Largest Fit Algorithm (LFA): Used for Red and Green cargo. It assigns an object to the bin with the largest remaining capacity. In case of ties, Red selects the least bin ID, and Green selects the greatest bin ID.

All operations are implemented using AVL trees to ensure logarithmic time complexity for insertion, deletion, and querying. The system avoids Python dictionaries and sets to maintain the required space and time complexity constraints.


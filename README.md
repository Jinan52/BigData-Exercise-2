# Big Data – Exercise 2

**Q1: Is your change in the mapper or in the reducer?**

The change was made in the **Mapper**.

The Mapper was modified to:
- Convert all words to lowercase using `lower()`.
- Remove trailing commas and periods using `rstrip(',.')`.
- Count words in a case-insensitive manner.

The Reducer remains unchanged.

**Q2: Please provide your code on GitHub.**

The code is included in this repository:
- `mapper_ex2.py`
- `reducer_ex2.py`

**Testing:** The updated MapReduce job was executed successfully on Amazon EMR using Hadoop Streaming.

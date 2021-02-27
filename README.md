# Frequency-Counting-Hash-Table
<i>Make School CS 1.2: Assignment 3</i>

This project was created with Python 3.7.4.

This project uses a hash table to implement a word-frequency counting program. My implementation uses chaining (with linked lists) in the event of collisions. My hash function calculates the index for a word based on the number of consonants in that word. This project works with any text file that contains letter-only words (no apostrophes). Words are counted on a case-insensitive basis, and punctuation is ignored. When run, this program counts the number of occurrences of each word in the input file (provided by the user when prompted) and prints all of the words with their frequencies.

For example, a text file that contains these lines:

`I write, erase, rewrite`
`Erase again, and then`
`A poppy blooms.`

would generate this output:
`a: 1`
`i: 1`
`and: 1`
`again: 1`
`erase: 2`
`then: 1`
`write: 1`
`blooms: 1`
`poppy: 1`
`rewrite: 1`

## Genomic coverage calculation from NGS data project

### By Jason Cole

---
#### Approach
The approach used reads from the lines of the NGS reads file and passes each line to a function which builds out two different important dictionaries: 
1. (pair_map) The keys for this dictionary are common prefixes found in the reads file.  The values are arrays of tuple pairs representing the start and end of each sequence that is tied to that prefix key.
2. (coverage_map) The keys to this dictionary is a tuple pairing of the start and end of each unique genetic sequence.  The value is the number of times that
the pair has been encountered in the file

After these two data structures are built, they are passed into another function to process the lines of the loci.csv file and determine the coverage for each loci in the file and write it to the loci.csv file.
This is done by getting the prefix of a loci getting all pairs associated with that prefix from the pair map.  Each pair associated with that prefix is then retreived from the coverage map to get its coverage count if the loci
falls within the bounds of the pair.  The count is added until all pairs associated with the loci prefix have been exhausted.  The count and loci are then
written to the loci.csv file.

The optimizations implemented were the use of dictionaries to access data, which provide O(1) access to data for a known key,
and preprocessing the reads into such dictionaries with the aid of a determined prefix of each read.  When coverage is searched for
with a loci, instead of having to loop through all reads data, the reads associated with a given prefix are isolated and processed.

---
#### Testing

To run unit tests, in the terminal from the main project folder run `python tests.py`

---
#### Performance Analysis

The time to read all lines in each file is O(n) where n is the number of lines.  The time to write to a file is also O(n).

The time to calculate coverage is n * k, where n is the number of lines in loci.csv and
k is the number of pairs associated with that loci's prefix.

The total calculation time is `(n reads) + (n loci) * (k pairs)`
# Plagiarism Detection

This is a command-line program that performs plagiarism detection using a N-tuple comparison algorithm allowing for synonyms in the text.

It takes in 3 required arguments, and one optional.

1. File name for a list of synonyms
2. Input file 1
3. Input file 2
4. (optional) the number N, the tuple size.  If not supplied, the default is N=3.


The synonym file has lines each containing one group of synonyms.  For example a line saying "run
sprint jog" means these words should be treated as equal.
The input files should be declared plagiarized based on the number of N-tuples in file1 that appear in
file2, where the tuples are compared by accounting for synonyms as described above.  For example,
the text ";go for a run" has two 3-tuples, ["go for a", "for a run"] both of which appear in the text "go for
a jog".
The output of the program should be the percent of tuples in file1 which appear in file2.  So for the
above example, the output would be one line saying "100%".  In another example, for texts "go for a
run" and "went for a jog" and N=3 we would output "50%" because only one 3-tuple in the first text
appears in the second one.


## Examples
```
% python3 run.py --files tests/test1/file1.txt tests/test1/file2.txt --synonyms tests/test1/syns.txt

100.0
```
```
% python3 run.py --files tests/test1/file1.txt tests/test1/file2.txt --synonyms tests/test1/syns.txt --tuple_size 3

100.0
```

```
% python3 run.py --files tests/test1/file1.txt  --synonyms tests/test1/syns.txt

usage: run.py [-h] -f FILES FILES -s SYNONYMS [-t TUPLE_SIZE]
run.py: error: argument -f/--files: expected 2 argument(s)

```

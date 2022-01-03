# Countdown Solver

## Numbers Game Example

- Target: 666
- Selected Cards: 25 50 75 100 3 6

```
$ python3 numbers.py 952 25 50 75 100 3 6
> Found: ((((75 * 3) * (100 + 6)) - 50) / 25) = 952
> Completed in 1.20 seconds
```

## Letters Game Example

Selected Letters: "U B C E D M I U G"

```
$ python3 letters.py ubcedmiug
> BUDGIE (6)
> Completed in 1.88 seconds
```
## Use a different word list

```
$ python3 resources/dictionaryHelper.py <myWords.txt>
> Initializing new dictionary

$ python3 letters.py ubcedmiug
> MUG (3)
> Completed in 0.00 seconds
```
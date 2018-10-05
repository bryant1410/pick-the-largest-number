# Pick the Largest Number

Experiments around the paper [Pick the Largest Number](https://fermatslibrary.com/s/pick-the-largest-number#email-newsletter),
shared by Fermat's Library on Oct 2, 2018 (original author is Cover, 1987).

## Install dependencies

1. Use Python 3.3+
2. Install packages:

```bash
pip install -r requirements.txt
```

## Run

```bash
./sample.py
```

Output:

```
Number of samples: 1000000
Player 1 and 2 use U(0, 1): 0.66704
Player 1 use N(0, 1) and Player 2 use U(0, 1): 0.705782
Player 1 use U(0, 1) and Player 2 use N(0, 1): 0.556756
Player 1 and 2 use N(0, 1): 0.666947
Player 1 use U(100, 200) and Player 2 use N(0, 1): 0.500008
Player 1 use U(100, 200) and Player 2 use C(0, 1): 0.500099
Player 1 use U(1, 2) and Player 2 use N(0, 1): 0.522461
Player 1 use U(1, 2) and Player 2 use C(0, 1): 0.517601
```

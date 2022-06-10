import random
import time

# Test to see if max() or if > + assignment faster
from typing import Optional

max_length = 3
new_length = 4
assigned_length = 4
n_trials = 100000

t1 = time.perf_counter()
for _ in range(n_trials):
    if new_length > max_length:
        assigned_length = new_length
    # I thought maybe it wouldn't do anything if it knows assigned_length = new_length so I added next line
    # assigned_length = max_length  <-- with this line: Method one took 0.01371079997625202 seconds.
t2 = time.perf_counter()

t3 = time.perf_counter()
for _ in range(n_trials):
    assigned_length = max(new_length, max_length)
t4 = time.perf_counter()

print(f"Method one took {t2 - t1} seconds.")
print(f"Method two took {t4 - t3} seconds.")

# Method one took 0.009921699995175004 seconds.
# Method two took 0.01988040001015179 seconds.

# ----------------------------------------------------------------------------------------
#
# --------  Testing speed of if statement versus removal of data from bitmap list --------
#
# ----------------------------------------------------------------------------------------

bitmap = [0] * 128
bitmap[50] = 5  # something random

t1 = time.perf_counter()

# nevermind, this isn't relevant to the code so I won't finish it... I'll keep it though in case I change my mind
# せっかくかっこいい分割のあれを作ったのに、すぐ消しちゃってももったいない


# ----------------------------------------------------------------------------------------
#
# --------  Testing if typehinting slows down code --------
#
# ----------------------------------------------------------------------------------------

iteration_number = 10000

t1 = time.perf_counter()
for _ in range(iteration_number):
    test_bitmap: list[Optional[int]] = [None] * 128
    test_bitmap[50]: int = 1
    test_bitmap[75]: int = 1
    test_bitmap[100]: int = 1
    x: int = test_bitmap[50]
    z: int = test_bitmap[75]
    y: int = test_bitmap[100]
t2 = time.perf_counter()

t3 = time.perf_counter()
for _ in range(iteration_number):
    test_bitmap = [None] * 128
    test_bitmap[50] = 1
    test_bitmap[75] = 1
    test_bitmap[100] = 1
    x = test_bitmap[50]
    z = test_bitmap[75]
    y = test_bitmap[100]
t4 = time.perf_counter()

print(f"Method one took {t2 - t1} seconds.")
print(f"Method two took {t4 - t3} seconds.")

# Method one took 0.014400099986232817 seconds.
# Method two took 0.007223499997053295 seconds.
# Darn.

# ----------------------------------------------------------------------------------------
#
# --------  Testing if "if dict.get()" is faster than "if in dict" --------
#
# ----------------------------------------------------------------------------------------

d = {}
iteration_number = 10000000
for c in 'abcdefghijklkmnopqrstuvwxyz':
    d[c] = random.random()

counter = 0
t1 = time.perf_counter()
for _ in range(iteration_number):
    if 'z' in d:
        counter += 1
    if 'A' in d:
        counter += 1
t2 = time.perf_counter()

counter = 0
t3 = time.perf_counter()
for _ in range(iteration_number):
    if d.get('z'):
        counter += 1
    if d.get('A'):
        counter += 1
t4 = time.perf_counter()

print(f"Method one took {t2 - t1} seconds.")
print(f"Method two took {t4 - t3} seconds.")

# Method one took 0.0012396000092849135 seconds.
# Method two took 0.0015241000219248235 seconds.

# increased iteration number
# Method one took 1.692932199977804 seconds.
# Method two took 2.047657100018114 seconds.

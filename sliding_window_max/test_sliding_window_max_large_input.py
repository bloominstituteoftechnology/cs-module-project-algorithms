import time
import unittest
from sliding_window_max import sliding_window_max

in_path = "/Users/ekselan/Documents/GitHub/CS1/Algorithms/sliding_window_max/input.txt"
out_path = "/Users/ekselan/Documents/GitHub/CS1/Algorithms/sliding_window_max/output.txt"

class Test(unittest.TestCase):
    def test_sliding_window_max_large_input(self):
        arr = []
        k = 1000

        with open(in_path) as file:
            for line in file:
                arr.append(int(line.strip()))

        expected = []

        with open(out_path) as file:
            for line in file:
                expected.append(int(line.strip()))

        start_time = time.time()
        answer = sliding_window_max(arr, k)
        end_time = time.time()
        print(f"RUNTIME: {end_time - start_time} seconds")

        self.assertTrue((end_time - start_time) < 1)
        self.assertEqual(answer, expected)


if __name__ == '__main__':
    unittest.main()

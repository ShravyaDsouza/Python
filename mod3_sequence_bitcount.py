def sequence_digit(n: int) -> int:
    # Count number of 1-bits and take modulo 3
    return n.bit_count() % 3

def main():
    import sys
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        print(sequence_digit(n))

if __name__ == "__main__":
    main()

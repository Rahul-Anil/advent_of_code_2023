import os


def read_input(path: str) -> str:
    with open(path) as f:
        return f.read()


def p1(inp: str) -> int:
    p1 = 0
    for line in inp.splitlines():
        p1_digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                p1_digits.append(c)
        p1 += int(p1_digits[0] + p1_digits[-1])
    print(f"p1: {p1}")


def p2(inp: str) -> int:
    p2 = 0
    num_as_text = [
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for line in inp.splitlines():
        p2_digits = []
        for i, c in enumerate(line):
            if c.isdigit():
                p2_digits.append(c)
            for d, val in enumerate(num_as_text):
                if line[i:].startswith(val):
                    p2_digits.append(str(d + 1))
        p2 += int(p2_digits[0] + p2_digits[-1])
    print(f"p2: {p2}")


def sample() -> None:
    inp1 = read_input("sample.txt")
    p1(inp1)
    inp2 = read_input("sample2.txt")
    p2(inp2)
    pass


def main() -> None:
    sample()
    print(f"MAIN")
    inp = read_input("d1.txt")
    p1(inp)
    p2(inp)


if __name__ == "__main__":
    main()

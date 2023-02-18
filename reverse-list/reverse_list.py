from collections import OrderedDict
import random
import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser(description="Generate Reverse List Dataset")
    parser.add_argument("--input_path", type=str, default="objects.json")
    parser.add_argument("--dataset_size", type=int, default=10)
    parser.add_argument("--objects_in_sample", type=int, default=5)
    parser.add_argument("--data_dir", type=str, default=".")
    parser.add_argument("--file_name", type=str, default="reverse_list")
    args = parser.parse_args()
    
    with open(args.input_path, 'r') as f:
        objects = json.load(f)

    used = {}
    samples = []
    for _ in range(args.dataset_size):
        q = "Reverse the sequence \""
        while True:
            sequence = random.choices(objects, k=args.objects_in_sample)
            if tuple(sequence) not in used:
                used[tuple(sequence)] = True
                break
        q += ", ".join(sequence) + "\"."
        a = ", ".join(sequence[::-1])

        samples.append(OrderedDict([("question", q), ("answer", a)]))

    with open(os.path.join(args.data_dir, args.file_name) + '.json', 'w') as f:
        json.dump(samples, f, indent=4)


if __name__ == "__main__":
    main()

from names_dataset import NameDataset
from collections import OrderedDict
import random
import argparse
import json
import os


def main():
    parser = argparse.ArgumentParser(description="Generate Last Letter Concatenation Dataset")
    parser.add_argument("--random_seed", type=int, default=0)
    parser.add_argument("--dataset_size", type=int, default=10)
    parser.add_argument("--names_in_sample", type=int, default=4)
    parser.add_argument("--data_dir", type=str, default=".")
    parser.add_argument("--file_name", type=str, default="last_letter_concatenation")
    args = parser.parse_args()

    nd = NameDataset()
    name_list = nd.get_top_names(n=int(args.dataset_size * args.names_in_sample / 2),
                                 country_alpha2='US')
    name_list = name_list['US']['M'] + name_list['US']['F']
    random.Random(args.random_seed).shuffle(name_list)

    samples = []
    for i in range(args.dataset_size):
        q = "Take the last letters of each words in \""
        a = ""
        for j in range(args.names_in_sample):
            k = i*args.names_in_sample + j
            q += name_list[k]
            a += name_list[k][0]
            if j != (args.names_in_sample-1):
                q += " "
        q += "\" and concatenate them."

        dic = OrderedDict()
        dic["question"] = q
        dic["answer"] = a
        samples.append(dic)

    with open(os.path.join(args.data_dir, args.file_name) + '.json', 'w') as f:
        json.dump(samples, f, indent=4)


if __name__ == "__main__":
    main()

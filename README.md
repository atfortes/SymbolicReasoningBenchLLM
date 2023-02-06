# Synthetic Data Generation for Language Models

This repository is dedicated to generating datasets for various language modeling tasks. Our goal is to provide an implementation for the generation of datasets that are not public or do not have an official implementation, and to make it easy for people to create and reproduce them.

We encourage contributions and feedback to make this repository a valuable resource for the community. If you have any questions or suggestions, please feel free to open an issue or submit a pull request.

## Make Your Pull Requests (PRs)
If you want to contribute, we encourage you to make a PR to this repository according to the following guidelines.

### Directory Structure
Each PR should include the code and markdown description in a subdirectory.
An example subdirectory tree is as follows:

```
└── DataGenLM
    └── <Your PR directory>: Dataset name
        ├── example.json (Optional)
        ├── README.md
        ├── requirements.txt
        └── <Your code>
```

Please exclude large data files in the PR as they take up too much space. Instead, describe the method to acquire the data in your `README.md` and optionally provide a small generation example. See the `coin-flip` and `last-letter-concatenation` subdirectories for an example.

### Task Description (README.md)
Please include the following sections in your README to help its better use:

+ **Dataset Name**: Serves as the markdown title.
+ **Authors**: Your name(s), contact (email), and url to your homepage(s) (if available).
+ **Task Description**: A short paragraph to briefly introduce what the dataset and corresponding task is about.
+ **Running Commands**: Instructions for generating the dataset.
+ **Reference**: Proper citation information for the dataset (if applicable).

### Environment Requirements (requirements.txt)
Please include the necessary packages in the file for generating the dataset.

### Contributors
<a href="https://github.com/atfortes/SyntheticDataGenerationLab/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=atfortes/SyntheticDataGenerationLab" />
</a>

# Coin Flip

## Authors

**Armando Fortes**

Homepage: https://atfortes.github.io/

Contact: fmq22@mails.tsinghua.edu.cn

Acknowledgement: Dataset generation code was adapted from [Kojima et al. (2022)](https://github.com/kojima-takeshi188/zero_shot_cot/blob/main/create_dataset_for_symbolic_reasoning.py).

## Task Description

This task requires the model to determine if a coin remains heads up after one or more individuals either flip or do not flip it. For instance, the input "A coin is heads up. Phoebe flips the coin. Osvaldo does not flip the coin. Is the coin still heads up?" should receive the response "no".

## Running Commands

You can run `python coin_flip.py --help` to see the usage of all the supported configurations. Using the default configuration as presented in the following command will reproduce the snippet at `example.json`. 

```bash
python coin_flip.py 
```

## Reference
```bibtex
@article{Wei2022ChainOT,
  title={Chain of Thought Prompting Elicits Reasoning in Large Language Models},
  author={Jason Wei and Xuezhi Wang and Dale Schuurmans and Maarten Bosma and Ed Huai-hsin Chi and Quoc Le and Denny Zhou},
  journal={ArXiv},
  year={2022},
  volume={abs/2201.11903}
}
```

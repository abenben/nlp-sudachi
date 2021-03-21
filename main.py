from sudachipy import tokenizer
from sudachipy import dictionary


def main():
    tokenizer_obj = dictionary.Dictionary().create()
    mode = tokenizer.Tokenizer.SplitMode.C
    for m in tokenizer_obj.tokenize("もうこれで満足だという時は、すなわち衰える時である。", mode):
        print(m.surface(), m.part_of_speech())


if __name__ == "__main__":
    main()

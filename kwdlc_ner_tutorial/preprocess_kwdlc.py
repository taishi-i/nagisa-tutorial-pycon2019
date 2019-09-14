import os
import sys
import glob
import random

import bs4
import nagisa


def load_kwdlc(dir_path):
    files = glob.glob(dir_path+"/*/*", recursive=True)

    data = []
    words = []
    postgas = []

    position2ne = {}

    for fn in files:
        with open(fn, "r") as f:
            for line in f:
                line = line.strip()
                first_char = line[0]

                if first_char == "+":
                    soup = bs4.BeautifulSoup(line, "html.parser")
                    num_tags = len(soup.contents)
                    for i in range(num_tags):
                        if str(type(soup.contents[i])) == "<class 'bs4.element.Tag'>":
                            if "ne" == soup.contents[i].name:
                                target = soup.contents[i].attrs["target"]
                                netype = soup.contents[i].attrs["type"]

                                position2ne[len(words)] = [target, netype]

                elif first_char == "#" or first_char == "*":
                    None

                elif line == "EOS":
                    # process
                    if len(position2ne) > 0:
                        positions = position2ne.keys()
                        for position in positions:
                            target = position2ne[position][0]
                            netype = position2ne[position][1]

                    data.append([words, postgas, position2ne])

                    # reset
                    words = []
                    postgas = []
                    position2ne = {}

                else:
                    tokens = line.split()
                    surface = tokens[0]
                    words.append(surface)

                    postag = "_".join(tokens[3:4])
                    postgas.append(postag)

    return data, position2ne


def write_kwdlc_as_single_file(filename, data, position2ne):

    with open(filename, "w") as f:
        for line in data:
            words, postgas, position2ne = line

            nes = [v[0] for k, v in sorted(position2ne.items(), key=lambda x:x[0])]
            nes = list(reversed(nes))

            tags = [v[1] for k, v in sorted(position2ne.items(), key=lambda x:x[0])]
            tags = list(reversed(tags))

            if len(nes) == 0:
                None

            else:
                ne_tags = []

                ne = nes.pop()
                tag = tags.pop()
                ne_target_char = ne[0]

                partical = []
                for word in words:
                    first_char = word[0]
                    if first_char == ne_target_char:

                        if word in ne:
                            partical.append(word)

                            if "".join(partical) == ne:

                                for i, word in enumerate(partical):
                                    if i == 0:
                                        ne_tags.append("B-"+tag)
                                    elif i == len(partical) - 1:
                                        ne_tags.append("E-"+tag)
                                    else:
                                        ne_tags.append("M-"+tag)

                                if len(nes) > 0:
                                    ne = nes.pop()
                                    tag = tags.pop()
                                    ne_target_char = ne[0]

                                partical = []

                            else:
                                ne_target_char = ne[len("".join(partical))]

                        else:
                            partical = []
                            ne_tags.append("O")

                    else:
                        partical = []
                        ne_tags.append("O")

                for word, postag, ne_tag in zip(words, postgas, ne_tags):
                    f.write("\t".join([word, ne_tag])+"\n")
                f.write("EOS\n")


def write_file(filename, X, Y):
    with open(filename, "w") as f:
        for x, y in zip(X, Y):
            for word, tag in zip(x, y):
                f.write("\t".join([word, tag])+"\n")
            f.write("EOS\n")


def main():
    # load KNP files
    dir_path = sys.argv[1]
    dir_path = os.path.join(dir_path, "dat/rel")
    data, position2ne = load_kwdlc(dir_path)

    # write a file
    fn_out = "data/kwdlc.txt"
    write_kwdlc_as_single_file(fn_out, data, position2ne)

    # divide kwdlc.txt into trainset, devset, testset
    random.seed(1234)
    fn_in = "data/kwdlc.txt"
    fn_out_train = "data/kwdlc.train"
    fn_out_dev = "data/kwdlc.dev"
    fn_out_test = "data/kwdlc.test"
    train_data = 0.9
    dev_data = 0.05
    test_data = 0.05

    X, Y = nagisa.utils.load_file(fn_in)
    indice = [i for i in range(len(X))]
    random.shuffle(indice)

    num_train = int(train_data * len(indice))
    num_dev = int(dev_data * len(indice))
    num_test = int(test_data * len(indice))

    train_X = [X[i] for i in indice[:num_train]]
    train_Y = [Y[i] for i in indice[:num_train]]
    write_file(fn_out_train, train_X, train_Y)

    dev_X = [X[i] for i in indice[num_train:num_train+num_dev]]
    dev_Y = [Y[i] for i in indice[num_train:num_train+num_dev]]
    write_file(fn_out_dev, dev_X, dev_Y)

    test_X = [X[i] for i in indice[num_train+num_dev:num_train+num_dev+num_test]]
    test_Y = [Y[i] for i in indice[num_train+num_dev:num_train+num_dev+num_test]]
    write_file(fn_out_test, test_X, test_Y)


if __name__ == "__main__":
    main()

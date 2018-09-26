#implements a parser for a meassy csv file that always have the same format
# written in an ad hoc fashion with a bit of hard coding
# will refactor as need arises

def _extractMatrixOfInterest(filename):
    with open(filename) as csvfile, open("data_matrix.csv","w") as matrixfile:
        extract = False
        all_lines = csvfile.readlines()
        for line in all_lines:
            if line.strip("\n").split(",") == ['"DataType:"', '"Median"\r']:
                extract = True
            elif line.strip("\n").split(",") == ['\r']:
                extract = False
            elif extract:
                matrixfile.write(line)

if __name__ == "__main__":
    _extractMatrixOfInterest("Lx200.csv")
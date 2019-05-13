def make_all_caps(in_filename, out_filename):
    """Convert all characters in 'in_filename' to caps and save to 'out_filename'.

    Parameters:
        in_filename (string): Name of the file from which to read the data.
        out_filename (string): Name of the file to which the data is to be saved.

    Preconditions:
        The files can be opened for reading and writing.
    """
    fin = open(in_filename, 'r')
    fout = open(out_filename, 'w')
    for line in fin:
        fout.write(line.upper())
    fin.close()
    fout.close()

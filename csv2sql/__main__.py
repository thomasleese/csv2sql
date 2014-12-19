import argparse
import csv
import sys


def read_csv(file=sys.stdin):
    """Read CSV data from the file."""
    return csv.reader(file)


def _filter_sql_column(x):
    if x == "NULL":
        return x
    else:
        return "\"{}\"".format(x)

def _write_sql_row(table, row, file):
    if row:
        sql = ", ".join(map(_filter_sql_column, row))
        print("INSERT INTO {} VALUES ({})".format(table, sql), file=file)


def write_sql(table, rows, file=sys.stdout):
    """Write out SQL to a file."""
    for row in rows:
        _write_sql_row(table, row, file)


def main():
    parser = argparse.ArgumentParser(description="Convert CSV from stdin to SQL INSERT statements on stdout.")
    parser.add_argument("table", help="SQL table name")
    parser.add_argument("infile", nargs="?", type=argparse.FileType("r"), default=sys.stdin, help="file to read CSV from")
    parser.add_argument("-o", "--outfile", type=argparse.FileType("w"), default=sys.stdout, help="file to write SQL to")
    args = parser.parse_args()

    write_sql(args.table, read_csv(args.infile), args.outfile)


if __name__ == "__main__":
    main()

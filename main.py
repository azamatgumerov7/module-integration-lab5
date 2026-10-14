from input_module import read_all_arrays
from processing import check_arrays
from output import print_results


def main():
    arrays = read_all_arrays()
    results = check_arrays(arrays)
    print_results(results)


if __name__ == "__main__":
    main()
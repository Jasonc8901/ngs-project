import csv


def process_loci(pair_map, coverage_map):
    with open('data/data/loci.csv', 'r') as loci_read_file:
        loci_lines = loci_read_file.readlines()

    write_file = create_csv_write_file('./data/data/loci')

    for loci_line in loci_lines:
        count, loci = get_loci_coverage(coverage_map, pair_map, loci_line)

        write_file.writerow([loci, str(count)])


def process_reads():
    coverage_map = {}
    pair_map = {}

    with open('data/data/reads.csv', 'r') as reads_file:
        for read in reads_file:
            build_maps(coverage_map, pair_map, read)

        return pair_map, coverage_map


def get_loci_coverage(coverage_map, pair_map, loci_line):
    count = 0
    loci = loci_line.split(',')[0]
    loci_prefix = loci[:-4]
    pair_list = pair_map.get(loci_prefix)

    if pair_list is None:
        if loci == 'position':
            return 'coverage', loci
        else:
            return '0', loci

    for pair in pair_list:
        minimum, maximum = (int(val) for val in pair)

        # adds up coverage count for each pair sharing the prefix of the loci with values containing the loci position
        if int(minimum) <= int(loci) < maximum:
            count += coverage_map.get((pair[0], pair[1]))

    return count, loci


def build_maps(coverage_map, pair_map, read):
    start, length = read.split(',')
    start_prefix = start[:-4]

    if start_prefix not in pair_map:
        pair_map[start_prefix] = []

    try:
        start = int(start)
        length = int(length)
    except ValueError:
        return

    end = str(start + length)

    if (start, end) not in coverage_map:
        pair_map[start_prefix] += [(start, end)]  # sets all pairs for each common prefix
        coverage_map[(start, end)] = 1
    else:
        coverage_map[(start, end)] += 1  # gets the number of times each pair appears in read


def create_csv_write_file(file_name):
    file_path = f'{file_name}.csv'
    file = open(file_path, 'w', newline='')
    return csv.writer(file)


if __name__ == '__main__':
    print('Processing reads')
    pair_map, coverage_map = process_reads()
    print('Processing loci coverage')
    process_loci(pair_map, coverage_map)
    print('Operation completed')


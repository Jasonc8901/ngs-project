import unittest
from main import build_maps, get_loci_coverage


class TestNGS(unittest.TestCase):
    def test_build_read_maps(self):
        reads = ['101891952,151\n', '148529640,139\n', '148529640,139\n']
        coverage_map, pair_map = {}, {}

        for read in reads:
            build_maps(coverage_map, pair_map, read)

        self.assertEqual(pair_map, {'10189': [(101891952, '101892103')], '14852': [(148529640, '148529779')]})
        self.assertEqual(coverage_map, {(101891952, '101892103'): 1, (148529640, '148529779'): 2})

    def test_coverage_calculation(self):
        pair_map = {'10189': [(101891952, '101892103')], '14852': [(148529640, '148529779')]}
        coverage_map = {(101891952, '101892103'): 1, (148529640, '148529779'): 2}
        reads = ['101891955,', '101891951,']
        count, loci = get_loci_coverage(coverage_map, pair_map, reads[0])

        self.assertEqual(count, 1)

        count, loci = get_loci_coverage(coverage_map, pair_map, reads[1])

        self.assertEqual(count, 0)


if __name__ == '__main__':
    unittest.main()
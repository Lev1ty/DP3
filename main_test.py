import unittest
import main

class TestMain(unittest.TestCase):
    def test_failed_file_creation(self):
        memo = main.complete_name1
        with self.assertRaises(FileNotFoundError):
            main.complete_name1 = ''
            main.file_creation()
        main.complete_name1 = memo
    def test_success_file_creation(self):
        main.file_creation()
    def test_temp_average_is_1(self):
        class SensorData:
            def get_temp1(self):
                return 1
        self.assertEqual(main.temp_average(SensorData(), 0), 1)

if __name__ == "__main__":
    unittest.main()
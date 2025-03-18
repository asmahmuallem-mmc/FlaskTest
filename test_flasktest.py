import unittest
import os
from FlaskTest import app
from plot_utils import generate_plot, generate_table

class FlaskTestCase(unittest.TestCase):
    def setUp(self):
        # Set up the test client
        self.app = app.test_client()
        self.app.testing = True

    def test_home_get(self):
        # Test the home page with GET request
        response = self.app.get('/')
        print("GET / response status code:", response.status_code)
        print("GET / response data:", response.data[:100])  # Print first 100 characters of response data
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'State Distribution', response.data)

    def test_home_post(self):
        # Test the home page with POST request
        response = self.app.post('/', data=dict(state='California'))
        print("POST / response status code:", response.status_code)
        print("POST / response data:", response.data[:100])  # Print first 100 characters of response data
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Plot for California', response.data)

    def test_generate_plot(self):
        # Test the generate_plot function
        plot_path = generate_plot('California')
        print("Generated plot path:", plot_path)
        self.assertIsNotNone(plot_path)
        self.assertTrue(os.path.exists(plot_path))
        
        # Check that the plot file contains expected content
        with open(plot_path, 'r') as f:
            content = f.read()
            print("Plot file content (first 100 characters):", content[:100])  # Print first 100 characters of content
            self.assertIn('California', content)
            self.assertIn('<div id="', content)  # Check for Plotly div

    def test_generate_table(self):
        # Test the generate_table function
        columns = ['CensusTract', 'State', 'County', 'Urban', 'Pop2010', 'OHU2010']
        table_path = generate_table(columns)
        print("Generated table path:", table_path)
        self.assertIsNotNone(table_path)
        self.assertTrue(os.path.exists(table_path))
        
        # Check that the table file contains expected content
        with open(table_path, 'r') as f:
            content = f.read()
            print("Table file content (first 100 characters):", content[:100])  # Print first 100 characters of content
            for column in columns:
                self.assertIn(column, content)  # Check for column names in the table

if __name__ == '__main__':
    unittest.main(verbosity=2)
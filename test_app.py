def test_square_root(self):
    response = self.app.post('/', data=dict(num1=9, operation='sqrt'))
    self.assertIn(b'Result: 3.0', response.data)

def test_exponent(self):
    response = self.app.post('/', data=dict(num1=2, num2=3, operation='exponent'))
    self.assertIn(b'Result: 8.0', response.data)

from jnius.reflect import autoclass
import unittest

class MultipleSignatureTest(unittest.TestCase):
    def test_autoboxing_integer_arg(self):
        IntegerJClass = autoclass("java.lang.Integer")
        int1 = IntegerJClass(1)
        # on the next line, 1 should be autoboxed to java.lang.Integer
        self.assertEqual(0, int1.compareTo(1))

    def test_autoboxing_boolean_arg(self):
      BooleanJClass = autoclass("java.lang.Boolean")
      boolTrue = BooleanJClass(True)
      # on the next line, True should be autoboxed to java.lang.Boolean
      self.assertEqual(0, boolTrue.compareTo(True))
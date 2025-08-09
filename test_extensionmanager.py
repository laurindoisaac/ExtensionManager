# test_extensionmanager.py
"""
Tests for ExtensionManager module.
"""

import unittest
from extensionmanager import ExtensionManager

class TestExtensionManager(unittest.TestCase):
    """Test cases for ExtensionManager class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ExtensionManager()
        self.assertIsInstance(instance, ExtensionManager)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ExtensionManager()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

# test_securityaudit.py
"""
Tests for SecurityAudit module.
"""

import unittest
from securityaudit import SecurityAudit

class TestSecurityAudit(unittest.TestCase):
    """Test cases for SecurityAudit class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SecurityAudit()
        self.assertIsInstance(instance, SecurityAudit)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SecurityAudit()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

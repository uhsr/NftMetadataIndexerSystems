# test_nftmetadataindexersystems.py
"""
Tests for NftMetadataIndexerSystems module.
"""

import unittest
from nftmetadataindexersystems import NftMetadataIndexerSystems

class TestNftMetadataIndexerSystems(unittest.TestCase):
    """Test cases for NftMetadataIndexerSystems class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = NftMetadataIndexerSystems()
        self.assertIsInstance(instance, NftMetadataIndexerSystems)
        
    def test_run_method(self):
        """Test the run method."""
        instance = NftMetadataIndexerSystems()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()

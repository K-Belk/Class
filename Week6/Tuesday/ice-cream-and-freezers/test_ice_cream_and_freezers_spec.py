import unittest
from ice_cream_and_freezers import IceCream, Freezer


class TestIceCreamAndFreezers(unittest.TestCase):

    def setUp(self) -> None:
        self.freezer = Freezer()
        self.chocolate = IceCream(6, "chocolate")
    
    def test_add_to_freezer(self):
        """Adds Ice Cream to the inventory when add_inventory is called"""
        self.assertEqual(len(self.freezer.inventory), 0)
        self.freezer.add_inventory(self.chocolate)
        self.assertEqual(len(self.freezer.inventory), 1)
    
    def test_remove_from_freezer(self):
        """Removes Ice Cream from the inventory when remove_inventory is called"""
        self.freezer.add_inventory(self.chocolate)
        self.assertEqual(len(self.freezer.inventory), 1)
        self.freezer.remove_inventory(self.chocolate)
        self.assertEqual(len(self.freezer.inventory), 0)

    def test_lets_do_the_time_warp(self):
        """Lets do the time warp and jump the time ahead 4"""
        self.assertEqual(self.freezer.time, 0)
        time_jump = 4
        self.freezer.time_warp(time_jump)
        self.assertEqual(self.freezer.time, time_jump)

    def test_sets_start_time(self):
        """When added to freezer inventory the ice cream start time should be set"""
        self.freezer.time_warp(4)
        self.freezer.add_inventory(self.chocolate)
        self.assertEqual(self.chocolate.start_time, 4)

    def test_status_watery(self):
        """Check what the status is with a time of 0 """
        self.freezer.add_inventory(self.chocolate)
        self.assertEqual(self.freezer.check_batch(self.chocolate), 'watery' )

    def test_status_almost(self):
        """Check what the status is with a time of 3 """
        self.freezer.add_inventory(self.chocolate)
        self.freezer.time_warp(3)
        self.assertEqual(self.freezer.check_batch(self.chocolate), 'almost_ready' )
        
    def test_status_ready(self):
        """Check what the status is with a time of 6 """
        self.freezer.add_inventory(self.chocolate)
        self.freezer.time_warp(6)
        self.assertEqual(self.freezer.check_batch(self.chocolate), 'ready' )
        
    def test_status_freezer_burned(self):
        """Check what the status is with a time of 8 """
        self.freezer.add_inventory(self.chocolate)
        self.freezer.time_warp(8)
        self.assertEqual(self.freezer.check_batch(self.chocolate), 'freezer_burned' )

    def test_inventory_check(self):
        """Checks the entire inventory"""
        self.freezer.add_inventory(self.chocolate)
        mint = IceCream(8, 'mint')
        self.freezer.time_warp(6)
        self.freezer.add_inventory(mint)
        inventory_check = self.freezer.check_inventory()
        self.assertEqual(inventory_check, [['chocolate', 'ready'], ['mint', 'almost_ready']])

if __name__ == '__main__':
    unittest.main()

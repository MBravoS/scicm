import scicm
import pytest

class Test_errors:
    def test_crop_badvminvmax(self):
        with pytest.raises(ValueError):
            scicm.tools.crop(scicm.cm.Stone,0.6,0.4)

import scicm
import pytest

class Test_errors:
    # Test if scicm.tools functions raise the appropiate errors
    
    # Test scicm.tools.crop raises error with vmin,vmax in the wrong order
    def test_error_crop_0(self):
        with pytest.raises(ValueError):
            scicm.tools.crop(scicm.cm.Stone,0.6,0.4)
    # Test scicm.tools.crop raises error with vmin,vmax outside of allowed values
    def test_error_crop_1(self):
        with pytest.raises(ValueError):
            scicm.tools.crop(scicm.cm.Stone,0,2)
    # Test scicm.tools.crop raises error if an undefined colour map is given
    def test_error_crop_2(self):
        with pytest.raises(ValueError):
            scicm.tools.crop('gibberish',0.2,0.8)
    def test_error_crop_3(self):
        with pytest.raises(TypeError):
            scicm.tools.crop(3,0.2,0.8)
    # Test scicm.tools.crop raises error if colour map name is not a string
    def test_error_crop_2(self):
        with pytest.raises(TypeError):
            scicm.tools.crop(0,0.2,0.8,8)


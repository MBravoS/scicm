import scicm
import pytest

class Test_crop:
    # Test if scicm.tools.crop functions raise the appropiate errors
    
    # Test scicm.tools.crop raises error with vmin,vmax in the wrong order
    def test_0(self):
        with pytest.raises(ValueError):
            scicm.tools.crop(scicm.cm.Stone,0.6,0.4)
    # Test scicm.tools.crop raises error with vmin,vmax outside of allowed values
    def test_1(self):
        with pytest.raises(ValueError):
            scicm.tools.crop(scicm.cm.Stone,0,2)
    # Test scicm.tools.crop raises error if an undefined colour map is given
    def test_2(self):
        with pytest.raises(ValueError):
            scicm.tools.crop('gibberish',0.2,0.8)
    def test_3(self):
        with pytest.raises(TypeError):
            scicm.tools.crop(3,0.2,0.8)
    # Test scicm.tools.crop raises error if colour map name is not a string
    def test_2(self):
        with pytest.raises(TypeError):
            scicm.tools.crop(0,0.2,0.8,8)

class Test_stitch:
    # Test if scicm.tools.stitch functions raise the appropiate errors
    
    # Test scicm.tools.stitch raises error with cmapinlist not being a list
    def test_0(self):
        with pytest.raises(TypeError):
            scicm.tools.stitch(scicm.cm.Stone,np.array([[0.2,0.4],[0.2,0.4]]),[0.5])
    # Test scicm.tools.stitch raises error with cmapinlist being less than two elements
    def test_1(self):
        with pytest.raises(ValueError):
            scicm.tools.stitch([scicm.cm.Stone],np.array([[0.2,0.4],[0.2,0.4]]),[0.5])
    # Test scicm.tools.stitch raises error if an undefined colour map is given
    def test_2(self):
        with pytest.raises(ValueError):
            scicm.tools.stitch([scicm.cm.Stone,scicm.cm.Stone],np.array([[0.2,0.4]]),[0.5])
    #def test_3(self):
    #    with pytest.raises(TypeError):
    #        scicm.tools.stitch(3,0.2,0.8)
    ## Test scicm.tools.stitch raises error if colour map name is not a string
    #def test_2(self):
    #    with pytest.raises(TypeError):
    #        scicm.tools.stitch(0,0.2,0.8,8)


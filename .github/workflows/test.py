import scicm
import pytest
import numpy as np

class Test_crop:
    # Test if scicm.tools.crop raises the appropiate errors
    
    # Test scicm.tools.crop raises error with vmin,vmax in the wrong order
    def test_crop_0(self):
        with pytest.raises(ValueError):
            scicm.tools.crop(scicm.cm.Stone,0.6,0.4)
    # Test scicm.tools.crop raises error with vmin,vmax outside of allowed values
    def test_crop_1(self):
        with pytest.raises(ValueError):
            scicm.tools.crop(scicm.cm.Stone,0,2)
    # Test scicm.tools.crop raises error if an undefined colour map is given
    def test_crop_2(self):
        with pytest.raises(ValueError):
            scicm.tools.crop('gibberish',0.2,0.8)
    def test_crop_3(self):
        with pytest.raises(TypeError):
            scicm.tools.crop(3,0.2,0.8)
    # Test scicm.tools.crop raises error if colour map name is not a string
    def test_crop_4(self):
        with pytest.raises(TypeError):
            scicm.tools.crop(0,0.2,0.8,8)

class Test_stitch:
    # Test if scicm.tools.stitch raises the appropiate errors
    
    # Test scicm.tools.stitch raises error with cmapinlist not being a list
    def test_stitch_0(self):
        with pytest.raises(TypeError):
            scicm.tools.stitch(scicm.cm.Stone,np.array([[0.2,0.4],[0.2,0.4]]),[0.5])
    # Test scicm.tools.stitch raises error with cmapinlist being less than two elements
    def test_stitch_1(self):
        with pytest.raises(ValueError):
            scicm.tools.stitch([scicm.cm.Stone],np.array([[0.2,0.4],[0.2,0.4]]),[0.5])
    # Test scicm.tools.stitch raises error with vlims is the wrong shape
    def test_stitch_2(self):
        with pytest.raises(ValueError):
            scicm.tools.stitch([scicm.cm.Stone,scicm.cm.Stone],
                                np.array([[0.2,0.4]]),[0.5])
    # Test scicm.tools.stitch raises error with vlims outside of allowed values
    def test_stitch_3(self):
        with pytest.raises(ValueError):
            scicm.tools.stitch([scicm.cm.Stone,scicm.cm.Stone],
                                np.array([[0.4,0.2],[0.2,0.4]]),[0.5])
    def test_stitch_4(self):
        with pytest.raises(ValueError):
            scicm.tools.stitch([scicm.cm.Stone,scicm.cm.Stone],
                                np.array([[0.2,0.4],[0.2,1.4]]),[0.5])
    # Test scicm.tools.stitch raises error with tpoints outside of allowed values
    def test_stitch_5(self):
        with pytest.raises(ValueError):
            scicm.tools.stitch([scicm.cm.Stone,scicm.cm.Stone,scicm.cm.Stone],
                                np.array([[0.2,0.4],[0.2,0.4],[0.2,0.4]]),[0.7,0.3])
    def test_stitch_6(self):
        with pytest.raises(ValueError):
            scicm.tools.stitch([scicm.cm.Stone,scicm.cm.Stone,scicm.cm.Stone],
                                np.array([[0.2,0.4],[0.2,0.4],[0.2,0.4]]),[0.3,1.3])
    # Test scicm.tools.stitch raises error with name_newcmap not being a string
    def test_stitch_7(self):
        with pytest.raises(TypeError):
            scicm.tools.stitch([scicm.cm.Stone,scicm.cm.Stone],
                                np.array([[0.2,0.4],[0.2,0.4]]),[0.5],name_newcmap=5)
    # Test scicm.tools.crop raises error if an undefined colour map is given
    def test_stitch_8(self):
        with pytest.raises(ValueError):
            scicm.tools.stitch([scicm.cm.Stone,'gibberish'],
                                np.array([[0.2,0.4],[0.2,0.4]]),[0.5])
    def test_stitch_9(self):
        with pytest.raises(TypeError):
            scicm.tools.stitch([scicm.cm.Stone,0],
                                np.array([[0.2,0.4],[0.2,0.4]]),[0.5])

class Test_merge:
    # Test if scicm.tools.merge raises the appropiate errors
    
    # Test scicm.tools.merge raises error with cmapinlist not being a list
    def test_merge_0(self):
        with pytest.raises(TypeError):
            scicm.tools.merge(scicm.cm.Stone,[0.5])
    # Test scicm.tools.merge raises error with cmapinlist being less than two elements
    def test_merge_1(self):
        with pytest.raises(ValueError):
            scicm.tools.merge([scicm.cm.Stone],[0.5])
    # Test scicm.tools.merge raises error with tpoints is the wrong shape
    def test_merge_2(self):
        with pytest.raises(ValueError):
            scicm.tools.merge([scicm.cm.Stone,scicm.cm.Stone],[[0.2,0.4]])
    # Test scicm.tools.merge raises error with tpoints outside of allowed values
    def test_merge_3(self):
        with pytest.raises(ValueError):
            scicm.tools.merge([scicm.cm.Stone,scicm.cm.Stone],[-1.3])
    def test_merge_4(self):
        with pytest.raises(ValueError):
            scicm.tools.merge([scicm.cm.Stone,scicm.cm.Stone],[1.3])
    # Test scicm.tools.merge raises error with name_newcmap not being a string
    def test_merge_5(self):
        with pytest.raises(TypeError):
            scicm.tools.merge([scicm.cm.Stone,scicm.cm.Stone],[0.5],name_newcmap=5)
    # Test scicm.tools.crop raises error if an undefined colour map is given
    def test_merge_6(self):
        with pytest.raises(ValueError):
            scicm.tools.merge([scicm.cm.Stone,'gibberish'],[0.5])
    def test_merge_7(self):
        with pytest.raises(TypeError):
            scicm.tools.merge([scicm.cm.Stone,0],[0.5])













from .PadImage import PadImage
from .AdjustMask import AdjustMask
from .Shift import ShiftWithMask, RepeatImage


NODE_CLASS_MAPPINGS = {
    "Pad Image with Random Edge": PadImage,
    "Adjust Mask Value": AdjustMask,
    "Shift Image with Mask": ShiftWithMask,
    "Repeat Image": RepeatImage
}

__all__ = ["PadImage", "AdjustMask", "ShiftWithMask", "RepeatImage"]
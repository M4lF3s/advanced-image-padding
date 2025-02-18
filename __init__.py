from .PadImage import PadImage
from .AdjustMask import AdjustMask
from .Shift import ShiftWithMask

NODE_CLASS_MAPPINGS = {
    "Pad Image with Random Edge": PadImage,
    "Adjust Mask Value": AdjustMask,
    "Shift Image with Mask": ShiftWithMask
}

__all__ = ["PadImage", "AdjustMask", "ShiftWithMask"]
from .PadImage import PadImage
from .AdjustMask import AdjustMask

NODE_CLASS_MAPPINGS = {
    "Pad Image with Random Edge": PadImage,
    "Adjust Mask Value": AdjustMask,
}

__all__ = ["PadImage", "AdjustMask"]
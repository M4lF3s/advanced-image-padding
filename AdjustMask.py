

class AdjustMask:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "mask": ("MASK",),
                "mask_value": ("FLOAT", {"default": 1, "min": 0, "max": 1, "step": 0.01}),
            }
        }

    RETURN_TYPES = ("MASK",)
    FUNCTION = "adjust_mask"

    CATEGORY = "mask"

    def adjust_mask(self, mask, mask_value):
        adjusted_mask = (mask!=0)*mask_value
        return (adjusted_mask,)
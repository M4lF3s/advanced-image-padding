import torch


class ShiftWithMask:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "mask": ("MASK",),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "shift_with_mask"

    CATEGORY = "mask"

    def shift_with_mask(self, image, mask):
        d1, d2, d3, d4 = image.size()
        shifted_image = torch.roll(image, shifts=[d3//2], dims=[2])
        shifted_mask = torch.roll(mask, shifts=[d3//2], dims=[1])

        return (shifted_image, shifted_mask)
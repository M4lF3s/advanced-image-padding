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

        if d3 % 2 != 0:
            image = image[:, :, :-1, :] # TODO this only works properly if there is a mask on the right edge!
            mask = mask[:, :-1]

        shifted_image = torch.roll(image, shifts=[d3//2], dims=[2])
        shifted_mask = torch.roll(mask, shifts=[d3//2], dims=[1])

        return (shifted_image, shifted_mask)


class RepeatImage:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "repeats": ("INT", {"default": 3, "min": 1, "max": 5}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "repeat"
    CATEGORY = "image"

    def repeat(self, image, repeats):
        new_image = image.repeat(1,1,repeats,1)
        return (new_image,)
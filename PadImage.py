from math import floor

import torch
import random

MAX_RESOLUTION=16384

class PadImage:

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "image": ("IMAGE",),
                "left": ("INT", {"default": 0, "min": 0, "max": MAX_RESOLUTION, "step": 1}),
                "right": ("INT", {"default": 0, "min": 0, "max": MAX_RESOLUTION, "step": 1}),
                "interval_size": ("INT", {"default": 50, "min": 0, "max": MAX_RESOLUTION, "step": 1}),
                "max_mask": ("INT", {"default": 100, "min": 0, "max": MAX_RESOLUTION, "step": 1}),
            }
        }

    RETURN_TYPES = ("IMAGE", "MASK")
    FUNCTION = "expand_image"

    CATEGORY = "image"

    def lerp(self, a, b, x) -> float:
        return (1 - x) * a + x * b

    def expand_image(self, image, left, right, interval_size, max_mask):
        d1, d2, d3, d4 = image.size()

        new_image = torch.ones(
            (d1, d2, d3 + left + right, d4),
            dtype=torch.float32,
        ) * 0.5

        new_image[:, :, left:left + d3, :] = image
        if left > 0:
            new_image[:, :, :left, :] = torch.flip(image, [2])[:, :, -left:, :]
        if right > 0:
            new_image[:, :, -right:, :] = torch.flip(image, [2])[:, :, :right, :]

        mask = torch.zeros(
            (d2, d3 + left + right),
            dtype=torch.float32,
        )

        random.seed(42)
        r1 = random.randint(0, max_mask)
        r2 = random.randint(0, max_mask)
        if left > 0:
            for h in range(d2):
                r1 = r2 if h % interval_size == 0 else r1
                r2 = random.randint(0, max_mask) if h % interval_size == 0 else r2
                l1 = floor(self.lerp(r1, r2, (h%interval_size) / interval_size))
                mask[h, :left+l1] = 1.

        r3 = random.randint(0, max_mask)
        r4 = random.randint(0, max_mask)
        if right > 0:
            for h in range(d2):
                r3 = r4 if h % interval_size == 0 else r3
                r4 = random.randint(0, max_mask) if h % interval_size == 0 else r4
                l2 = floor(self.lerp(r3, r4, (h%interval_size) / interval_size))
                mask[h, -(right+l2):] = 1.

        return (new_image, mask)

from imageLoader import imageLoader

class SpriteObject(object):
    def __init__(self, imageUrl, frameCount, scale, frameWidth, frameHeight, cutColor):
        self.frameCount = frameCount
        self.scale = scale
        self.cutColor = cutColor
        self.frameHeight = frameHeight
        self.frameWidth = frameWidth
        self.url = imageUrl

    def fillFrameArray(self, frameArray):
        for i in range(0, self.frameCount):
            frame = imageLoader(self.url, self.scale, (self.frameWidth * i, 0, self.frameWidth, self.frameHeight))
            frame.set_colorkey(self.cutColor)
            frameArray.append(frame)
        return frameArray
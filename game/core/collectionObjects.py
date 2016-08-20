from singleton import Singleton

# All object has been created and add to CollectionObject Array
# In game loop we rerender and check state this objects
# This is can be asteroids, enemies, player etc
class _CollectionObjects(Singleton):
    def __init__(self):
        self.objects = []

    def get(self):
        return self.objects

    def add(self, object):
        self.objects.append(object)

    def resetObjects(self):
        for gameObject in self.objects:
            if hasattr(gameObject, 'type'):
                if gameObject.objectType == 'enemy':
                    gameObject.reset()
        self.objects = filter(lambda obj: obj.objectType != 'enemy', self.objects)

collectionObjects = _CollectionObjects()
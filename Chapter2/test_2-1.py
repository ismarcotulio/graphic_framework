from core.base import Base

class Test(Base):
    def initialize(self):
        print("Initializing program...")

Test().run()
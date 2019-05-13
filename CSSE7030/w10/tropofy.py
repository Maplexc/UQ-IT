from sqlalchemy import Column, Text, Float
from tropofy.database.tropofy_orm import DataSetMixin
from tropofy.app.application import AppWithDataSets, Step, StepGroup
from tropofy.widgets import SimpleGrid

class MyLocation(DataSetMixin):
    name = Column(Text)
    latitude = Column(Float)
    longitude = Column(Float)

class MyFirstApp(AppWithDataSets):
    def get_name(self):
        return "My First App"

    def get_gui(self):
        return [StepGroup(steps=[Step(widgets=[SimpleGrid(MyLocation)])])]

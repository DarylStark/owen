class Baby:
    def __init__(self, mom, dad) -> None:
        pass


from datetime import datetime
from maes import Birgit
from stark import Daryl

Owen = Baby(mom=Birgit, dad=Daryl)
Owen.birth_datetime = datetime(year=2022,
                               month=1,
                               day=20,
                               hour=21,
                               minute=42)
Owen.gender = "Boy"
Owen.weight_grams = 3786
Owen.length_cm = 51
Owen.cute = True

while True:
    Owen.hug()

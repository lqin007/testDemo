from PythonPractice.heroPractice.heroFactory import HeroFactory
from PythonPractice.heroPractice.police import Police
from PythonPractice.heroPractice.timo import Timo

timo =HeroFactory().creatHero("timo")
police =HeroFactory().creatHero("police")
timo.fight(police)


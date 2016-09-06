from setuptools import setup
from subprocess import call
from setuptools.command.install import install

class MyInstall(install):
    def run(self):
        call(["pip", "install", "-r", "requirements.txt", "-t", "python_modules"], shell=True)
        install.run(self)

setup(
    name="Distutils",
    version="1.0",
    description="The arcade game",
    author="Aleksandrov Sergey",
    author_email="gooddev.sergey@gmail.com",
    url="https://github.com/AlexSergey/Space-Invaders-Python-game",
    cmdclass={"install": MyInstall},
)
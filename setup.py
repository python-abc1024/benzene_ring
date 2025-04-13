from setuptools import setup,find_packages

with(open(file="README.md",mode="r",encoding="utf-8"))as(f):
  long_description=f.read()
with(open(file="requirements.txt",mode="r",encoding="utf-8")as(f)):
  install_requires=f.read().split("\n")

setup(
  name="benzene_ring",
  version="1.2.0",
  author="yangjinhe",
  author_email="python_abc@outlook.com",
  description="A better statistics module of python",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=r"https://github.com/python-abc1024/benzene_ring",
  packages=find_packages(),
  include_package_data=True,
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
  ],
  python_requires='>=3.6',
  install_requires=install_requires,
)
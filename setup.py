from setuptools import setup

setup(
    name='Sickle_Cell',
    version='1.0',
    packages=[''],
    package_dir={'': 'src'},
    url='https://github.com/OriWeiss/Sickle-Cell-Anemia-Detection',
    license='MIT License',
    author='Ori Weiss',
    author_email='oriweiss212@gmail.com',
    description='Computer Vision Sickle Cell Anemia Detection',
    install_requires = [
        "matplotlib",
        "opencv-python",
        "numpy",
        "scikit-image",
        "pillow",
        "scipy"
    ]
)

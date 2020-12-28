from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='visual_perception',
    description='A High Level Python Library for Visual Recognition ',
    url="https://github.com/SSusantAchary/Visual-Perception",
    author="SusantAchary",
    author_email="sache.meet@yahoo.com",
    maintainer="Susant Achary",
    maintainer_email="sache.meet@yahoo.com",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=find_packages(),
    python_requires='>=3.5, <4',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Image Processing',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    keywords=[
        "object detection",
        "computer vision",
        'yolo',
        'yolov4',
        'tinyyolo'],

    install_requires=[
        "tensorflow",
        'keras',
        'opencv-python',
        'numpy',
        'pillow',
        'matplotlib',
        'pandas',
        'scikit-learn',
        'progressbar2',
        'scipy',
        'h5py',
        'imgaug',
        'scikit-image',
        'labelme2coco',
        'configobj',
    ],

    project_urls={

        'Bug Reports': 'https://github.com/SSusantAchary/Visual-Perception/issues',
        'Source': 'https://github.com/SSusantAchary/Visual-Perception/'},

)
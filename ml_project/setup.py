from setuptools import find_packages, setup

setup(
    name='ml_project',
    version='0.1.0',
    packages=find_packages(),
    description='Machine Learning Project',
    author='Your Name',
    author_email='your.email@example.com',
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'pyyaml',
    ],
    python_requires='>=3.8',
)

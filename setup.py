import setuptools

with open(r'README.md', mode=r'r') as readme_handle:
    long_description = readme_handle.read()

setuptools.setup(
    name=r'hopfield',
    version=r'1.0.2',
    author=r'Bernhard Schäfl',
    author_email=r'schaefl@ml.jku.at',
    url=r'https://https://github.com/emmas96/modern-hopfield-layers',
    description=r'Continuous modern Hopfield layers for Deep Learning architectures',
    long_description=long_description,
    long_description_content_type=r'text/markdown',
    packages=setuptools.find_packages(),
    python_requires=r'>=3.8.0',
    install_requires=[
        r'torch>=1.5.0',
        r'numpy>=1.20.0'
    ],
    zip_safe=True
)

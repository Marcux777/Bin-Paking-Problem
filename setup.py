from setuptools import setup, find_packages

setup(
    name='bin-packing-problem',
    version='0.1.0',
    description='Núcleo reutilizável para o problema de Bin Packing',
    author='Marcus Vinicius, Eduardo Augusto Moreira',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],  # Pode ser preenchido conforme o requirements.txt
)

from setuptools import setup, find_packages

setup(
    name="LoCyanFrpLauncher",
    author="ltzXiaoYanMo",
    author_email="xiajiaruimail@qq.com",
    long_description="Python 库 - 乐青 Frp 启动器",
    python_requires='>=3.7, <=3.11',
    url="https://github.com/LxHTT/LoCyanFrpLauncher",
    packages=find_packages(),
    license='MIT',
    install_requires=[
        "requests>=2.31.0"
        "LoCyanFrpLib>=1.0.0"
    ]
)

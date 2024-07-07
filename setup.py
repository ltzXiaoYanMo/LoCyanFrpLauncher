from setuptools import setup, find_packages

setup(
    name="locyan_launcher",
    version="1.0.0",
    author="YanMo",
    author_email="xiajiaruimail@qq.com",
    description="Python 库 - 乐青 Frp 启动器",
    url="https://github.com/ltzXiaoYanMo/LoCyanFrpLauncher",
    requires=["requests", "aiohttp", "asyncio"],
    packages=find_packages(),
    license="MIT License",
    long_description=open("README.md", "r", encoding="UTF-8").read(),
    python_requires=">=3.6"
)

from setuptools import setup

PACKAGES = [
    "django_websocket",
]


setup(
    name="django-websocket",
    author="Enes Gulakhmet",
    author_email="wwho.mann.3@gmail.com",
    description="Django websocket library",
    long_description=open("README.md").read(),
    setup_requires=["setuptools_scm"],
    url="https://github.com/GoodBitDev/django-websocket",
    packages=PACKAGES,
    include_package_data=True,
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Framework :: Django",
        "Topic :: Software Development :: Libraries :: Application Frameworks",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=[
        "Django>=3.2",
        "requests>=1.2.0",
        "channels>=3.0.3"
    ],
    zip_safe=False,
)

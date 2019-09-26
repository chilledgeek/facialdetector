import setuptools

package_name = "photo_sorter"
package_version = "0.0.2"
packages = ['opencv-python', "joblib", "matplotlib", "face-recognition", "cmake", "dlib"]
long_description = open("README.md", "r").read()

setuptools.setup(name=package_name,
                 version=package_version,
                 author="E CHOW",
                 author_email="chilledgeek@gmail.com",
                 description='Simple photo sorter app',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url='https://github.com/chilledgeek/photo_sorter',
                 install_requires=packages,
                 classifiers=[
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: MacOS',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Programming Language :: Python :: 3',
                     'Topic :: Scientific/Engineering :: Image Recognition',
                 ],
                 )

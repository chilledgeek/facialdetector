import setuptools

package_name = "facialdetector"
package_version = "0.0.2"
packages = ['opencv-python']
long_description = open("README.md", "r").read()

setuptools.setup(name=package_name,
                 version=package_version,
                 author="E CHOW",
                 author_email="chilledgeek@gmail.com",
                 description='Simple facial detection app',
                 long_description=long_description,
                 long_description_content_type="text/markdown",
                 url='https://github.com/chilledgeek/facialdetector',
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

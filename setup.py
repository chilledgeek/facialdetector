import setuptools

package_name = "facialdetector"
package_version = "1.0.0"
packages = ['opencv-python']
long_description = open("README.md", "r").read()

setuptools.setup(name=package_name,
                 version=package_version,
                 author="E CHOW",
                 author_email="chilledgeek@gmail.com",
                 description='Simple facial detection app',
                 long_description=long_description,
                 url='https://github.com/chilledgeek/facialdetector',
                 install_requires=packages,
                 classifiers=[
                     'License :: OSI Approved :: MIT License',
                     'Operating System :: MacOS',
                     'Operating System :: Microsoft :: Windows',
                     'Operating System :: POSIX',
                     'Operating System :: Unix',
                     'Programming Language :: Python',
                     'Programming Language :: Python :: 3',
                     'Topic :: Scientific/Engineering :: Image Recognition',
                 ],
                 )

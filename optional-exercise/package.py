# Copyright Spack Project Developers. See COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

# ----------------------------------------------------------------------------
# If you submit this package back to Spack as a pull request,
# please first remove this boilerplate and all FIXME comments.
#
# This is a template package file for Spack.  We've put "FIXME"
# next to all the things you'll want to change. Once you've handled
# them, you can save this file and test your package like this:
#
#     spack install spack-exercise
#
# You can edit this file again by typing:
#
#     spack edit spack-exercise
#
# See the Spack documentation for more information on packaging.
# ----------------------------------------------------------------------------

from spack_repo.builtin.build_systems.cmake import CMakePackage

from spack.package import *


class SpackExercise(CMakePackage):
    """SSE WS 2025/26 spack exercise by MarcelGraf0710"""

    # websites
    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/MarcelGraf0710/spack-exercise.git"
    git = "https://github.com/MarcelGraf0710/spack-exercise.git"

    # maintainers
    maintainers("MarcelGraf0710")

    # license
    license("MIT", checked_by="MarcelGraf0710")

    # versions
    version("main", branch="main", preferred=True)
    version("0.3.0", sha256="c179ccc9d56b724fcb7eeff8cebbc1afe2797929b99aa6e7d9b8478a014f2d02")
    version("0.2.0", sha256="010c900a3d4770116844636b89c1e42b1920f27c3da615543fb14f2ae9bb7f64")
    version("0.1.0", sha256="f1c212a58376fd78e9854576627e6927d7cb93ccffe3a162b1664570c491e3a7")

    # variants
    variant("boost", default=True, description="Enable support for boost")
    variant("yamlcpp", default=True, description="Enable support for yaml-cpp")

    # dependencies
    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("boost@1.65.1:", when="+boost @0.2.0:")
    depends_on("yaml-cpp@0.7.0:", when="+yamlcpp @0.3.0:")

    def cmake_args(self):
        args = [
            self.define_from_variant("WITH_BOOST", "boost"),
            self.define_from_variant("WITH_YAML", "yamlcpp")
        ]
        return args

    

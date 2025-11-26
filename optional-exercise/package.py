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

    homepage = "https://simulation-software-engineering.github.io/homepage/"
    url = "https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.3.0.tar.gz"
    git = "https://github.com/Simulation-Software-Engineering/spack-exercise.git"

    maintainers("MarcelGraf0710")

    license("MIT", checked_by="MarcelGraf0710")

    version("main", branch="main", preferred=True)
    version("0.3.0", sha256="c179ccc9d56b724fcb7eeff8cebbc1afe2797929b99aa6e7d9b8478a014f2d02")
    version("0.2.0", sha256="010c900a3d4770116844636b89c1e42b1920f27c3da615543fb14f2ae9bb7f64")
    version("0.1.0", sha256="f1c212a58376fd78e9854576627e6927d7cb93ccffe3a162b1664570c491e3a7")

    variant("boost", default=True, description="Enable support for boost")
    variant("yamlcpp", default=True, description="Enable support for yaml-cpp")

    depends_on("cxx", type="build")
    depends_on("c", type="build")
    depends_on("boost@1.65.1:", when="@0.2.0:")
    depends_on("yaml-cpp@0.7.0:", when="@0.3.0:")

    def cmake_args(self):
        args = []
        args.append(self.define("WITH_BOOST", "+boost" in self.spec))
        args.append(self.define("WITH_YAML", "+yamlcpp" in self.spec))
        return args

    

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
    url = "TBD"
    git = "TBD"

    maintainers("MarcelGraf0710")

    license("MIT", checked_by="MarcelGraf0710")

    version("main", branch="main", preferred=True)
    version("0.3.1", sha256="TBD")

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

    

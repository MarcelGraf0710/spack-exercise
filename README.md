# Packaging with Spack

Repository for the [Spack exercise](https://github.com/Simulation-Software-Engineering/Lecture-Material/blob/main/03_building_and_packaging/spack_exercise.md). The code is a slightly modified version of the [code used in the CMake exercise](https://github.com/Simulation-Software-Engineering/cmake-exercise).

The directory `docker/` contains the recipe of the Docker image that has been prepared for the exercise. Build a Docker image from the recipe and start a container from this image.

## My elaborations

I implemented all mandatory tasks and most optional tasks. In the following, the structure of my elaboration is explained, and information for reproducing the results is provided.

### Building and launching the docker container

All of the following commands are to be executed from within the `docker` folder. I built the docker container with

```bash
sudo docker build -t spack-exercise .
```

and ran it with

```bash
sudo docker run -it --mount type=bind,src=..,dst=/mnt/host/ spack-exercise
```

What should be done from there on depends on whether only the mandatory tasks or also the optional tasks are considered.

### Mandatory tasks

For reproducing the results of the mandatory tasks, proceed as follows:

```bash
spack create https://github.com/Simulation-Software-Engineering/spack-exercise/archive/refs/tags/v0.3.0.tar.gz
# Press 'c' and enter
# Escape Vim without any changes (type ':wq' and enter)
cd /home/spackbuilder/.spack/package_repos/fncqgg4/repos/spack_repo/builtin/packages/spack_exercise/
cp /mnt/host/mandatory-exercise/package.py .

# v0.1.0
spack install spack-exercise@0.1.0
spack load spack-exercise@0.1.0
spackexample
spack unload spack-exercise@0.1.0

# v0.2.0
spack install spack-exercise@0.2.0
spack load spack-exercise@0.2.0
spackexample
spack unload spack-exercise@0.2.0

# v0.3.0
spack install spack-exercise@0.3.0
spack load spack-exercise@0.3.0
spackexample /mnt/host/yamlParser/config.yml
```

This part is fully compliant with the exercise template and assumes the unaltered `C++` code and `CMakeLists.txt` provided there.

### Optional tasks

I completed the following optional tasks:

1. Add the main branch of the GitHub repository as version to the Spack recipe.
2. Make the current dependencies (Boost, yaml-cpp) optional by defining suitable options in the CMakeLists.txt which are also picked up in the C++ code. Then add corresponding variants in the Spack recipe which allow to turn on/off these features.

The corresponding `package.py` is located at the folder `optional-exercise`. The first optional task is straightforward. I implemented the second task such that the user can modify two separate variants, namely `boost` and `yamlcpp`. By default, both are `true`. Notice that the releases are not available in forks of the exercise repository, but the `package.py` assumes they are, since that would be the case in a realistic workflow.

Notice that the ability to specify whether the functionality relying on `boost` and `yaml-cpp` should be built or not requires changes to the source code and the `CMakeLists.txt`. The required changes were applied in the `C++` code and `CMakeLists.txt` contained within this branch. To reproduce the results without troubles, please mind executing

```bash
spack create https://github.com/MarcelGraf0710/spack-exercise
```

instead of the link to the `tar.gz` belonging to the exercise template.

To reproduce the results of the optional tasks with `boost` and `yamlcpp` *disabled*, proceed as follows:

```bash
# Create package.py stub from my fork

spack create https://github.com/MarcelGraf0710/spack-exercise
# Escape Vim without any changes (type ':wq' and enter)
cd /home/spackbuilder/.spack/package_repos/fncqgg4/repos/spack_repo/builtin/packages/spack_exercise/
cp /mnt/host/optional-exercise/package.py .

# Install spack-exercise/main with boost and yaml-cpp disabled
spack install spack-exercise -boost -yamlcpp
spack load spack-exercise
spackexample /mnt/host/yamlParser/config.yml
```

The `boost` and `yamlcpp` variants do not depend on each other, so you may test arbitrary combinations of those.
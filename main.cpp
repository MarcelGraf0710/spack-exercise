#ifdef WITH_BOOST
  #include "flatset/flatset.hpp"
  #include "filesystem/filesystem.hpp"
#endif

#ifdef WITH_YAML
  #include "yamlParser/yamlParser.hpp"
#endif

#include <iostream>

int main(int argc, char *argv[])
{
  std::cout << "Let's fight with CMake, Docker, and some dependencies!" << std::endl << std::endl;

  #ifdef WITH_BOOST
    std::cout << "Modify a flat set using boost container" << std::endl;
    modifyAndPrintSets();
    std::cout << std::endl;

    std::cout << "Inspect the current directory using boost filesystem" << std::endl;
    inspectDirectory();
    std::cout << std::endl;
  #endif

  #ifdef WITH_YAML
    if ( argc == 2 )
    {
      const std::string yamlFile( argv[1] );
      std::cout << "Parse some yaml file with yaml-cpp" << std::endl;
      std::cout << "  " << yamlFile << std::endl;
      parseConfig( yamlFile );
    }
  #endif

  return 0;
}


# Nombre del ejecutable
EXECUTABLE = programa

# Archivos fuente en la misma carpeta que el Makefile
SRC_FILES = $(wildcard *.cpp)

# Compilador y flags
CXX = g++
CXXFLAGS = -Wall

# Flags de enlace
LDFLAGS = -lwiringPi

# Regla principal: compilar el ejecutable
all: $(EXECUTABLE)

$(EXECUTABLE): $(SRC_FILES)
	$(CXX) $(CXXFLAGS) $^ -o $@ $(LDFLAGS)
	chmod +x $@

# Limpiar los archivos generados
clean:
	rm -f $(EXECUTABLE)

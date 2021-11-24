
CXX=mpic++

all: petsc-systempath petsc-pkg-config

petsc-systempath:
	$(CXX) petsc-test.cpp -I/usr/lib/petscdir/petsc3.12/x86_64-linux-gnu-real/include -lpetsc -o petsc-systempath

petsc-pkg-config:
	$(CXX) petsc-test.cpp `pkg-config --cflags --libs PETSc` -o petsc-pkg-config

clean:
	rm -f petsc-systempath petsc-pkg-config
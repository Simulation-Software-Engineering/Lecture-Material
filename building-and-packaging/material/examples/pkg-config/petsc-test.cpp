#include<iostream>

#include<petsc.h>

static char help[] = "PETSc dummy example.\n\n";


int main(int argc,char **argv)
{
    PetscErrorCode ierr;
    ierr = PetscInitialize(&argc,&argv,(char*)0,help);
    if (ierr) return ierr;
    std::cout << "Using PETSc version: " <<  PETSC_VERSION_MAJOR << "." <<  PETSC_VERSION_MINOR << "." << PETSC_VERSION_SUBMINOR << std::endl;
    ierr = PetscFinalize();
    return ierr;
}
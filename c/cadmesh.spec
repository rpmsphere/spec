Name: cadmesh
Summary: A CAD file interface for GEANT4
Version: 1.1
Release: 1
Group: Development/Tools
License: Apache License 2.0
URL: https://github.com/christopherpoole/CADMesh
Source0: CADMesh-%{version}.tar.gz
BuildRequires: cmake
BuildRequires: geant4-devel
BuildRequires: assimp-devel

%description
Importing predefined CAD models into GEANT4 is not always possible or requires
intermediate file format conversion to Geometry Description Markup Language
(GDML) using commercial or third party software. CADMesh is a direct CAD model
import interface for GEANT4 optionally leveraging VCGLIB, and ASSIMP by default.
Currently it supports the import of triangular facet surface meshes defined in
formats such as STL and PLY. A G4TessellatedSolid is returned and can be
included in a standard user detector constructor.

Additional functionality is included for the fast navigation of tessellated
solids by automatically creating equivalent tetrahedral meshes thereby making
smart voxelisation available for the solid.

%prep
%setup -q -n CADMesh-%{version}

%build
%cmake
make

%install
%make_install

%files
%doc README.md
%{_bindir}/*

%changelog
* Thu Aug 15 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora

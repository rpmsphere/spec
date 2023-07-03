Summary: 	Molecule viewer and editor
Name: 		viewmol
Version: 	2.4.1
Release: 	20.1
License: 	GPLv2
Group: 		Sciences/Chemistry
URL: 		https://viewmol.sourceforge.net
Source0: 	%name-%version.src.tar.bz2
Patch0:		viewmol-2.4.1-prevent-app-defaults-file-install.patch
Patch1:		viewmol-2.4.1-mdv-fix-str-fmt.patch
BuildRequires: 	libtiff-devel mesa-libGLU-devel
BuildRequires: 	xorg-x11-proto-devel libXt-devel libXi-devel libXmu-devel
BuildRequires:  motif-devel libpng-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  python2-devel

%description
Viewmol is a graphical front end for computational chemistry programs.
It is able to graphically aid in the generation of molecular structures
for computations and to visualize their results. At present Viewmol
includes input filters for Discover, DMol, Gamess, Gaussian 9x, Gulp,
Mopac, and Turbomole outputs as well as for PDB files.

%prep
%setup -q
%patch0 -p1
%patch1 -p1 -b .strfmt
cd source
perl -p -i -e 's!usr/local/lib!%_libdir!g' getrc.c
perl -p -i -e 's!lib/viewmol!%_lib/viewmol!g' install

%build
cd source
mkdir Linux
echo "LIBTIFF = -L%_libdir" > .config.Linux
echo "TIFFINCLUDE = /usr/include" >> .config.Linux
echo "MESALIB = -L/usr/%_lib" >> .config.Linux
echo "MESAINCLUDE = /usr/include/GL" >> .config.Linux
#echo "PYTHONVERSION = %pythonver" >> .config.Linux
echo "PYTHONINCLUDE = /usr/include/python2.7" >> .config.Linux
echo "LIBPYTHON = -L%_libdir/python2.7" >> .config.Linux
cd Linux
cat ../.config.Linux > makefile
echo 'COMPILER = gcc' >> makefile
echo 'OPT=${RPM_OPT_FLAGS}' >> makefile
echo 'CFLAGS=-Wall -I/usr/include -DLINUX' >> makefile
echo 'LDFLAGS=' >> makefile
echo 'SCANDIR=' >> makefile
echo 'INCLUDE=$(MESAINCLUDE) -I$(TIFFINCLUDE) -I$(PYTHONINCLUDE)' >> makefile
echo 'LIBRARY=$(MESALIB) $(LIBPYTHON)' >> makefile
echo 'LIBS=-L/usr/%_lib -lpython2.7 -ltiff -lGLU -lGL -lpng -lXm -lXmu -lXt -lX11 -lXi -lm' >> makefile
cat ../Makefile >> makefile
make viewmol_
make tm_
make bio_
make readgamess_
make readgauss_
make readmopac_
make readpdb_

%install
cd source
./install %{buildroot}%_prefix
mkdir -p %{buildroot}%_docdir
mkdir -p %{buildroot}%_docdir/%name
mv %{buildroot}/%_libdir/viewmol/doc/* %{buildroot}%_docdir/%name
rmdir %{buildroot}/%_libdir/viewmol/doc
chmod 755 %{buildroot}/%_libdir/viewmol/Linux/*
chmod 755 %{buildroot}/%_bindir/*

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=ViewMol
Comment=GUI interface for chemistry software
Exec=%{name} 
Icon=%_docdir/%name/html/%name.png
Terminal=false
Type=Application
StartupNotify=true
Categories=Motif;Education;Science;Chemistry;
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_libdir}/viewmol/writegauss.py

%files
%_docdir/%name
%_bindir/%name
%_libdir/%name
%_datadir/applications/%name.desktop

%changelog
* Wed Apr 29 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.1
- Rebuilt for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 2.4.1-15
+ Revision: 6820fd7
- MassBuild#464: Increase release tag

Name: fluxspace
Summary: Flux space is a desktop extention for fluxbox
Version: 0.0.3
Release: 1
License: GPL
Group: System/GUI/Other
Source: %{name}-%{version}.tar.bz2
URL: https://fluxspace.sourceforge.net/
Requires: fluxbox python libxml2 rox
BuildRequires: swig, python2-devel, imlib2-devel, libxml2-devel
#BuildRequires: allegro-devel

%description
Fluxspace blends Fluxbox's window management with new desktop management
capabilities. It leverages existing components and the power of Python to
help build a flexible desktop environment around Fluxbox and other lightweight
window managers.

See %{_datadir}/doc/packages/fluxspace/README for instructions.

%prep
%setup -q
#sed -i '1i LDFLAGS=-lsupc++ -lstdc++' Makefile.am
#sed -i 's/explicit FbPixmap(const/FbPixmap(const/' src/FbTk/FbPixmap.hh
sed -i '259,269s/PythonInterfaceModule:://' src/PythonInterface.cc
sed -i '1i #include <cstring>' src/FluxspaceDisplay.cc
cp -f /usr/share/automake-*/config.guess .

%build
PYTHON_CONFIG_PROG=/usr/bin/python2-config PYTHON=/usr/bin/python2 CFLAGS="$RPM_OPT_FLAGS" CXXFLAGS="$RPM_OPT_FLAGS -lstdc++ -std=gnu++14" \
./configure --bindir=%{_bindir}
make

%install
rm -rf %{buildroot}
#make DESTDIR=%{buildroot} install-strip
make install     prefix=%{buildroot}/usr \
                 bindir=%{buildroot}%{_bindir} \
                 mandir=%{buildroot}%{_datadir}/man \
                 datadir=%{buildroot}%{_datadir}

%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
rm %{buildroot}%{python2_sitearch}/_fluxspace.so
rm %{buildroot}%{python2_sitearch}/fluxspace/__init__.py
ln -s %{_libdir}/libfluxspace-0.0.3.so %{buildroot}%{python2_sitearch}/_fluxspace.so
ln -s %{python2_sitearch}/fluxspace.py %{buildroot}%{python2_sitearch}/fluxspace/__init__.py

#remove unwanted doc files
rm -r %{buildroot}%{_datadir}/fluxspace

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/*

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS COPYING BUGS NEWS README TODO INSTALL examples/fluxspace.xml
%{_bindir}/*
%{_libdir}/libfluxspace*
%{python2_sitearch}/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.3
- Rebuilt for Fedora
* Sun Nov 28 2004 Sebastien Corot <scorot@libertysurf.fr>
- Compilded for SuSE Linux 9.2
* Sun May 23 2004 Sebastien Corot <scorot AT libertysurf.fr>
- Compiled for SuSE Linux 9.1
* Sat May 01 2004 Sebastien Corot <scorot AT libertysurf.fr>
- Create spec file
- Compiled for SuSE 9.0

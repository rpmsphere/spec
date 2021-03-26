%define _name MadButterfly

Name: madbutterfly
Version: 20110930
Release: 1
Summary: SVG toolkit for GUI environment
Group: Development/Libraries
License: GPL v3
URL: http://madbutterfly.sourceforge.net/
Source: %{_name}.tar.gz
#Source: hg clone http://hg.assembla.com/MadButterfly MadButterfly
BuildRequires: cairo, pango

%description
MadButterfly is a toolkit for GUI environment, designed for embedded system.
It make GUI designers and programmers work seperately.
Designer export their artifacts to files with SVG format.
MadButterfly provides a tool to translate graphics in SVG into C code and
a framework that programmer can manipulate graphics.
It works like a Javascript programmer to manipulate DOM object.
Programmers using MadButterfly manipulate objects corresponding to SVG tags
to interact with users of application.

%package devel
Summary: Development files for MadButterfly

%description devel
Development files for MadButterfly

%prep
%setup -q -n %{_name}
chmod +x tools/gen_precomputed_tabs.py
sed -i '1s|env python|python2|' tools/*.py

%build
export PYTHON_PATH=/usr/bin/python2
./autogen.sh
./configure --prefix=/usr --libdir=%{_libdir}
sed -i 's|-lcairo|-lcairo -lX11|' src/Makefile
make || make -C src libmbfly.la
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%{_libdir}/libmbfly.so*

%files devel
%{_bindir}/svg2code.py
%{_libdir}/pkgconfig/libmbfly.pc
%{_libdir}/libmbfly.*a
%{_includedir}/mb*.h
%{_datadir}/mb

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20090817
- Rebuild for Fedora

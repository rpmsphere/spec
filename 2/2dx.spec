%define __python /usr/bin/python2

Summary: Image Processing for 2D Crystal Images
Name: 2dx
Version: 3.5.0
Release: 19.1
License: GPL
Group: Applications/Miscellaneous
URL: http://www.2dx.unibas.ch/
Source0: %{name}-%{version}.tar.gz
BuildRequires: gcc-c++, gcc-gfortran, cmake, fftw-devel
BuildRequires: qt5-qtbase-devel, qt5-qtscript-devel, qt5-qtwebkit-devel
Patch0: 2dx-labelh-common.diff
Requires: python-pillow-tk

%description
A graphical front end suite allows interactive processing of single
EM-Micrographs of 2D membrane crystals from Stalhberg Lab, UC Davis.

%prep 
%setup -q
%patch0 -p1

%build
export PATH=%{_libdir}/qt5/bin:$PATH
cmake . -DCMAKE_INSTALL_PREFIX=$RPM_BUILD_ROOT%{_libdir}/%{name}
%make_build

%install
rm -rf $RPM_BUILD_ROOT
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_libdir}/%{name}

%changelog
* Fri Mar 25 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 3.5.0
- Rebuilt for Fedora

%undefine _debugsource_packages

Name: fractgen
Version: 2.1.0
Release: 12.1
Summary: Fractal Generator
Group: Applications/Multimedia
License: GPLv3
URL: https://github.com/dreibh/fractgen
Source: https://github.com/dreibh/fractgen/archive/%{name}-%{version}.tar.gz
BuildRequires: qt5-qtbase-devel

%description
FractGen is a simple Qt-based fractal generator program for Mandelbrot fractals.
The image size is only limited by virtual memory. It is possible to zoom into
images. Image parameters can be saved in XML files and loaded from XML files.
Calculated images can be exported as PNG files. The intention of this program
is to generate graphics to be post-processed by other image tools, e.g.
in order to generate nice screen backgrounds or book covers.

%prep
%setup -q

%build
qmake-qt5
make %{?_smp_mflags}

%install
#make install INSTALL_ROOT=%{buildroot}
install -Dm755 -p src/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc ChangeLog COPYING
%{_bindir}/fractgen

%changelog
* Fri Apr 21 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1.0
- Rebuilt for Fedora
* Thu Sep 26 2013 Thomas Dreibholz <dreibh@iem.uni-due.de> - 2.0.16
- Created RPM package.

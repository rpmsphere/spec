%global debug_package %{nil}

Name:           knotter
Version:        0.9.6
Release:        5.1
Summary:        Celtic knot editor
License:        GPLv3+
URL:            http://www.knotdraw.org/
Source0:        http://sourceforge.net/projects/knotter/files/latest/download/%{name}-%{version}.tar.gz
BuildRequires:  qt-devel, qtwebkit-devel
Requires:       qt, qtwebkit
Group:          Productivity/Graphics

%description
Knotter is an editor for interlace patterns.
Knots drawn with Knotter can be exported as SVG or raster images.

%prep
%setup -q
sed -i '26i #include <vector>' src/c++.hpp

%build
export CXXFLAGS=-std=c++98
export QMAKE=qmake-qt4
./configure.sh --prefix=/usr
make %{?_smp_m_flags}

%install
make install INSTALL_ROOT=$RPM_BUILD_ROOT

%files
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%changelog
* Fri Dec 20 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.6
- Rebuild for Fedora
* Mon Oct 29 2012 Mattia Basaglia <> - 0.8.0-1
- Initial release

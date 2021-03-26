Name:		qbriscola
%define Uname QBriscola
Summary:	Qt4 Italian card game Briscola
Version:        1.1svn.2
Release:	8.1
URL:		http://%{name}.sourceforge.net/
Source:         %{name}-%{version}.tar.xz
Patch0:		qbriscola_desktop.diff
License:	GPL-3.0
Group:		Amusements/Games/Board/Card
BuildRequires:  cmake
BuildRequires:  pkgconfig(QtGui)
BuildRequires:  pkgconfig(QtCore)
BuildRequires:  pkgconfig(QtSql)
BuildRequires:  pkgconfig(QtNetwork)
BuildRequires:  pkgconfig(QtDBus)

%description
The game of the Briscola (Italian card-game) with Qt4 graphics.

%prep
%setup -q
%patch0
%__sed -i '\|DESTINATION \"share/icons\"|s|share/icons|share/pixmaps|' CMakeLists.txt

%build
%cmake \
 -DCMAKE_INSTALL_PREFIX=%{_prefix} \
 -DLIB_SUFFIX=$(echo %_lib | cut -b4-) \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_SKIP_RPATH=YES
%{__make} %{?_smp_mflags} VERBOSE=1

%install
%make_install

%files -f install_manifest.txt
%doc README

%changelog
* Mon Jan 13 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1svn.2
- Rebuild for Fedora
* Wed Aug 21 2013 fa0sck@gmail.com
- Build latest stable version for openSUSE (from svn)

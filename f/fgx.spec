%undefine _debugsource_packages

Summary: FlightGear Launcher
Name: fgx
Version: 2.6.0
Release: 13.1
License: GPL
Group: Amusements/Games/3D/Simulation
Source0: fgx-1328651169.tar.bz2
Source1: FGx.desktop
Source2: fgx.png
Source3: x_default.ini
URL: https://code.google.com/p/fgx
BuildRequires: desktop-file-utils, gcc-c++, zlib-devel, zlib
BuildRequires: qt4-devel, qt-creator, qt4-webkit-devel, llvm-devel
Requires: FlightGear

%description
FGx is a lightweight graphical launcher for the FlightGear flight simulator.

%prep
%setup -n fgx-1328651169 -q -T -b 0
cp %{SOURCE3} src/resources/default/x_default.ini

%build
cd src
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$RPM_OPT_FLAGS"
export CPPFLAGS="$RPM_OPT_FLAGS"
qmake-qt4 -project
qmake-qt4 -makefile fgx.pro
make %{?_smp_mflags} clean
make %{?_smp_mflags}

%install
install -Dm755 src/fgx $RPM_BUILD_ROOT%{_bindir}/fgx
install -Dm644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps/fgx.png
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/applications/FGx.desktop

%files
%{_datadir}/pixmaps/fgx.png
%{_datadir}/applications/FGx.desktop
%{_bindir}/fgx

%changelog
* Sun Sep 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.6.0
- Rebuilt for Fedora
* Wed Dec 28 2011 thorstenb@flightgear.org
- Updated setup
* Fri Jul 29 2011 Daniel Zucchetto
- Created package

Name: fisicalab
Version: 0.3.5
Release: 5.3
Summary: An educational application to solve physics problems
License: GPLv3
Group: Graphical desktop/GNUstep
URL: https://www.gnu.org/software/fisicalab/
Source0:       https://ftp.gnu.org/gnu/fisicalab/%{name}-%{version}-1.tar.gz
Source2:       %{name}.png
Source3:       %{name}.desktop
BuildRequires: gcc-objc
BuildRequires: gsl-devel
#BuildRequires: gnustep-back
BuildRequires: gnustep-base
BuildRequires: gnustep-base-devel
BuildRequires: gnustep-gui-devel
BuildRequires: gnustep-make
Requires:      gnustep-make gnustep-back

%description
FisicaLab consist in a chalkboard to set the problems and a palette with
elements like mobiles, blocks, forces,... that let the user set the
problems.

FisicaLab can solve the fallowing problems:
* Kinematics of particles in 2D.
* Circular kinematics of particles in 2D.
* Static of particles in 2D.
* Static of rigid bodies in 2D.
* Dynamics of particles in 2D.
* Circular dynamics of particles in 2D.
* Heat, calorimetry, ideal gas and expansion.

%prep
%setup -q

%build
. /etc/GNUstep/GNUstep.conf
. %_libdir/GNUstep/Makefiles/GNUstep.sh

%configure
make \
	messages=yes \
	debug=yes \
	strip=no \
	shared=yes
 
%install
. /etc/GNUstep/GNUstep.conf
. %_libdir/GNUstep/Makefiles/GNUstep.sh
%make_install GNUSTEP_INSTALLATION_DOMAIN=SYSTEM

mkdir -p %buildroot/%{_datadir}/{applications,pixmaps}
install -m 644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE3} %{buildroot}%{_datadir}/applications

%files
%doc ChangeLog README COPYING NEWS
%_bindir/*
%_libdir/GNUstep/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed Jan 11 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.5
- Rebuilt for Fedora
* Fri Feb 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt3
- Built with clang
* Wed Jan 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt2
- Added Requires: gnustep-back
* Mon Jan 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Version 0.3.3
* Wed Mar 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Version 0.3.2
* Wed Feb 27 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2
- Added menu file (thnx kostyalamer@)
* Mon Feb 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus


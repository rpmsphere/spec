%undefine _debugsource_packages

Name: systester		
Version: 1.5.1
Release: 5.1
Summary: An open source clone of SuperPI	
Group: Applications/System
License: GPLv2	
URL: http://systester.sourceforge.net		
Source0:  http://voxel.dl.sourceforge.net/project/systester/systester/1.5.0/systester-1.5.1.tar.gz
BuildRequires: qt >= 4.5.3
BuildRequires: qt-devel
BuildRequires: gmp >= 4.2.1
BuildRequires: gmp-devel
BuildRequires: desktop-file-utils

%description
System Stability Tester tries to test the system's stability by calculating up 
to 128 millions of Pi digits. It supports multiple calculation algorithms. For 
the moment only two have been implemented. The Quadratic Convergence of Borwein 
and Gauss-Legendre, the algorithm SuperPi uses. The testing process includes the 
creation of two or more threads. After each step of the calculation, the results 
of all the threads are compared. Any differences between them are reported. 
There is also the option for single threaded calculation, but in this case there 
is no stability check.

%prep
%setup -q
sed -i 's|/usr/share/pixmaps/%{name}.png|%{name}|' %{name}.desktop
%ifarch aarch64
sed -i 's|ASM_CODE (ret)|ret = 0|' cpufreq.cpp
%endif

%build
qmake-qt4 systester.pro
make 
cd cli
make
make lite

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/pixmaps/
cp -p systester %{buildroot}%{_bindir}/
cp -p cli/systester-cli %{buildroot}%{_bindir}/
cp -p cli/systester-lite %{buildroot}%{_bindir}/
cp -p images/systester.png %{buildroot}%{_datadir}/pixmaps/
desktop-file-install \
--dir=${RPM_BUILD_ROOT}%{_datadir}/applications \
systester.desktop
desktop-file-validate %{buildroot}%{_datadir}/applications/systester.desktop

%clean
rm -rf %{buildroot}

%files
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Sun Apr 9 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5.1
- Rebuilt for Fedora
* Thu Jun 28 2012 systester.project@gmail.com 1.5.1-1
- PI and log files now lay on user's home directory (GUI only)
* Wed May 02 2012 systester.project@gmail.com 1.5.0-1
- New splash screen with about and license windows
- License button removed
- Flattr button added
- Minor bugs fixed
- Aesthetic changes
- Terminal autoscroll
* Sat Jan 07 2012 systester.project@gmail.com 1.4.2-1
- Systester now depends on QT >= 4.5.3
- Display available memory in Darwin 
- Checksum validation re-implemented in order to bypass gcc bug 
* Fri Sep 09 2011 systester.project@gmail.com 1.4.0-1
- Systester now depends on QT >= 4.4
- Update button introduced for latest version check
- Updated systester.pro
- KDE and Gnome menu icon introduced through
- install-desktop.sh script
- FAQ.txt added in the source tree

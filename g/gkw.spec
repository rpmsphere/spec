%undefine _debugsource_packages

Summary:        Gyro-Kinetics at Warwick
Name:           gkw
Version:        0.1b4
Release:        4.1
License:        GPLv3
Group:          Applications/Engineering
URL:            https://code.google.com/p/gkw/
Source0:        https://gkw.googlecode.com/files/gkw-0.1-b4.tar.gz
BuildRequires:  gcc-gfortran

%description
Gyro-kinetic simulation code for the study of turbulence in magnetised plasmas.
A tool for fusion energy research.

%prep
%setup -q -n gkw-0.1-b4
sed -i 's/-fdefault-real-8//' src/makefile

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}
install -m755 gkw.x bin/* $RPM_BUILD_ROOT%{_bindir}

%files
%doc README LICENSE REVISIONS samples
%{_bindir}/%{name}*

%changelog
* Fri Dec 09 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1b4
- Rebuilt for Fedora

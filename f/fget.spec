Summary:	Commandline tool for mirroring remote files via FTP
Name:		fget
Version:	1.3.3
Release:	10.1
License:	GPLv2+
Group:		Networking/File transfer
URL:		http://www.feep.net/fget/
Source0:	ftp://ftp.feep.net/pub/software/fget/%{name}-%{version}.tar.bz2
Patch0:		fget-1.3.3-no-strip.patch

%description
fget is a commandline tool for mirroring remote files via FTP. It was designed
as an analog to the GNU wget utility. The fget package includes an FTP client
library, so that others can make use of FTP from within their own C programs.

%files
%doc README
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*

%package devel
Summary:	Development library for fget
Group:		Development/Other
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name} < 1.3.3-6
Conflicts:	%{name}-devel < 1.3.3-6
Obsoletes:	%{name}-devel < 1.3.3-6

%description devel
Development library for fget.

%files devel
%{_includedir}/*.h
%{_libdir}/*.a
%{_mandir}/man3/*.3*

%prep
%setup -q
%patch0 -p1

%build
%configure
%make_build

%install
%make_install

%changelog
* Wed Jul 04 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3.3
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1.3.3-10
- (9869f59) MassBuild#1257: Increase release tag

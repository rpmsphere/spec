Name: ttyload
Summary: Gives a color-coded graph of load averages over time
Version: 0.5.3
Release: 8.1
License: GPL
Group: System/Monitoring
URL: http://www.daveltd.com/src/util/ttyload/
Source0: http://www.daveltd.com/src/util/ttyload/%{name}-%{version}.tar.bz2
BuildRequires: libpcap-devel

%description
ttyload is a little *NIX utility which is meant to give a color-coded graph of
load averages over time.

%prep  
%setup -q
sed -i '1i #include <time.h>' ttyload.h

%build
make
  
%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
make INSTALLDIR=$RPM_BUILD_ROOT%{_bindir} install
  
%clean  
rm -rf $RPM_BUILD_ROOT

%files 
%attr(755,root,root) %{_bindir}/ttyload
%doc BUGS HISTORY LICENSE README.md TODO

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.3
- Rebuild for Fedora
* Sun Apr 17 2011 04:55:21 UTC - jamesp@vicidial.com
- Code cleanup to try and make a better package I hope
* Wed Dec 15 2010 01:21:18 UTC - jamesp@vicidial.com
- Initial RPM

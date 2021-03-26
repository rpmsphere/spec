%global debug_package %{nil}

Name:         peep
Summary:      Network/File/StdIO Connectivity Utility
URL:          http://www.cslab.ece.ntua.gr/~gtsouk/peep/
Group:        Network
License:      GPL
Version:      0.5.7
Release:      6.1
Source0:      http://www.cslab.ece.ntua.gr/~gtsouk/peep/peep-%{version}.tar.gz
Patch:        peep.patch

%description
PEEP is an ultra-flexible utility for general purpose
routing/redirecting of data among local files, network connections
and the standard I/O.

%prep
%setup -q
%patch -p0

%build
%{__make} %{_smp_mflags} linux-gcc-dynamic

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p -m 755 \
    $RPM_BUILD_ROOT%{_bindir} \
    $RPM_BUILD_ROOT%{_mandir}/man1
install -c -m 755 \
    peep $RPM_BUILD_ROOT%{_bindir}
install -c -m 644 \
    peep-*.ReadMe $RPM_BUILD_ROOT%{_mandir}/man1/peep.1

%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1.*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.7
- Rebuild for Fedora

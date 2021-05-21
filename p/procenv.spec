Name:           procenv
Version:        0.36
Release:        2.3
Summary:        Utility to show process environment
Group:          Applications/System
License:        GPLv3+
URL:            https://launchpad.net/procenv
Source0:        https://launchpad.net/procenv/trunk/%{version}/+download/procenv-%{version}.tar.gz
BuildRequires:  gcc, make, binutils, autoconf, automake, pkgconfig, expat, libcap-devel, libselinux-devel
BuildRequires:  perl-JSON-PP
BuildRequires:  numactl-devel

%description
This package contains a command-line tool that displays as much
detail about itself and its environment as possible. It can be
used as a test tool, to understand the type of environment a
process runs in, and for comparing system environments.

%prep
%setup -q

%build
%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/procenv
%{_mandir}/man1/procenv.1.*

%changelog
* Wed Apr 13 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.36
- Rebuilt for Fedora
* Thu Jun  5 2014 Dave Love <d.love@liverpool.ac.uk> - 0.35-2
- Only BR perl-JSON-PP and run tests on fedora
* Fri Jan 31 2014 James Hunt <james.hunt@ubuntu.com> - 0.32-1
- Update to 0.31.
* Thu Jan 23 2014 James Hunt <james.hunt@ubuntu.com> - 0.30-1
- Update to 0.30.
* Wed Nov 14 2013 Dave Love <d.love@liverpool.ac.uk> - 0.27-1
- Update to 0.27, fix Source0
* Sun Dec  9 2012 Dave Love <fx@gnu.org> - 0.18-1
- Update to 0.18
* Tue Dec  4 2012 Dave Love <fx@gnu.org> - 0.16-2
- Re-fix locale-reporting.
* Mon Dec  3 2012 Dave Love <fx@gnu.org> - 0.16-1
- Update to 0.16
* Thu Nov 22 2012 Dave Love <fx@gnu.org> - 0.12-1
- Initial packaging

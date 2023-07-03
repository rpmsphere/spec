Name:		putils
Version:	1.0
Release:	2.1
Summary:	Various Linux utilities using the /proc filesystem
Group:		Application/System
License:	GPLv2
URL:		https://udrepper.livejournal.com/22255.html
Source0:	https://www.akkadia.org/drepper/%{name}-%{version}.tar.bz2

%description
The plimit utility allows to query and set the limits of a process.
The pfiles utility allows to examine the open files of a process.

%prep
%setup -q

%build
make %{?_smp_mflags}

%install
make install DESTDIR=$RPM_BUILD_ROOT

%files
%{_bindir}/pfiles
%{_bindir}/plimit

%changelog
* Sun Jun 30 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuilt for Fedora
* Thu May 31 2012 Ulrich Drepper <drepper@gmail.com> - 1.0
- Initial build

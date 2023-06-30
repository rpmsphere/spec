Name:		become
Version:	0.1
Release:	4.1
URL:		https://www.bindshell.net/tools/become
Source:		https://www.bindshell.net/tools/become/become.tgz
Summary:	Utility to changes the effective, or real, user and group id
License:	BSD
Group:		System/Base

%description
The become utility changes the current effective, or real, user and
group identity to those specified on the command line. The default shell
(/bin/sh) is then executed.
UID and GID are specified numercially and do not have to be currently
defined on the system.

%prep
%setup -q -n %{name}

%build
make

%install
%{__rm} -Rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_sbindir} $RPM_BUILD_ROOT%{_mandir}/man8
%{__install} -c become $RPM_BUILD_ROOT%{_sbindir}
%{__install} -c -m 644 become.8 $RPM_BUILD_ROOT%{_mandir}/man8

%files
%doc LICENSE
%{_sbindir}/%{name}
%{_mandir}/man8/%{name}.8.*

%changelog
* Sun Sep 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1
- Rebuilt for Fedora
* Tue Sep 01 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.1-4mdv2010.0
+ Revision: 424029
- rebuild
* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-3mdv2009.0
+ Revision: 243210
- rebuild
* Thu Feb 14 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.1-1mdv2008.1
+ Revision: 167826
- fix no-buildroot-tag
* Fri Aug 17 2007 Nicolas Vigier <nvigier@mandriva.com> 0.1-1mdv2008.0
+ Revision: 65018
- Import become

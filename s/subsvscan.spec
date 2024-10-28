Name:      subsvscan
Version:   200511041029
Release:   3.1
Group:     System/Base
License:   GPL
URL:       https://gpl.internetconnection.net/
Source:    https://gpl.internetconnection.net/files/subsvscan.tar.gz
Patch0:     subsvscan_implicit_declarations.patch
Summary:   Sub supervise support

%description
Run svscan under supervise, allowing svc -t the parent supervise to kill all of
the children under the sub-supervise.

%prep
%setup -n %{name}
%patch 0

%build
gcc %{optflags} -DUSE_FCNTL lock.c  subsvscan.c -o subsvscan

%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__install} -D -m 0755 subsvscan   $RPM_BUILD_ROOT%{_bindir}/subsvscan
%{__install} -D -m 0644 subsvscan.8 $RPM_BUILD_ROOT%{_mandir}/man8/subsvscan.8

%files
%{_bindir}/subsvscan
%{_mandir}/man8/subsvscan.8*
%doc CHANGELOG

%changelog
* Tue Aug 21 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 200511041029
- Rebuilt for Fedora
* Sat Oct  7 2006 mrueckert@suse.de
- initial package

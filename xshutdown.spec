Summary: Shutdown and reboot buttons for xdm
Name: xshutdown
Version: 1.0
Release: 3.1
Group: X11/Utilities
License: GPL
Source: xshut.tgz
BuildArch: noarch
Requires: perl-Tk

%description
Xshutdown is a nice and elegant way of shutting down
or rebooting your machine from X.
Xshutdown consists of a perl script called xshut.
xshut can be used to query, install, and uninstall
shutdown and reboot buttons in the xdm login screen.
The buttons only exist while the login widget is
displayed, and are removed when the user logs in.

%prep
%setup -q -n Xshutdown-%{version}

%build

%install
install -Dm755 xshut $RPM_BUILD_ROOT%{_bindir}/xshut
install -Dm644 xshut.1 $RPM_BUILD_ROOT%{_mandir}/man1/xshut.1

%files
%{_bindir}/xshut
%{_mandir}/man1/xshut.1.*
%doc COPYING README INSTALL

%changelog
* Sun Feb 22 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora

%undefine _debugsource_packages

Summary: A program that keeps your connections alive
Name: lifekeeper
Version: 1.4
Release: 2
License: GPLv3
Group: Utilities/System
URL: https://vigna.dsi.unimi.it/lifekeeper
Source: https://vigna.dsi.unimi.it/lifekeeper/lifekeeper-%{version}.tar.gz

%description
lifekeeper prints an ASCII NUL character every 30 seconds. This has
no effect visually, but if someone is watching the connection for activity
it will see some.

%prep
%setup -q

%build
gcc -O3 lifekeeper.c -o lifekeeper

%install
rm -rf $RPM_BUILD_ROOT
install -Dm755 lifekeeper $RPM_BUILD_ROOT/usr/bin/lifekeeper
install -Dm644 lifekeeper.1 $RPM_BUILD_ROOT/usr/share/man/man1/lifekeeper.1

%files
%{_bindir}/lifekeeper
%{_mandir}/man1/lifekeeper.1*

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4
- Rebuilt for Fedora

%undefine _debugsource_packages

Summary: A time reminder taken from NetBSD
Name: leave
#Version: 1.12
Version: 1.8
Release: 6.1
License: BSD
Group: Utils
Source0: %{name}-%{version}.tar.gz
Patch0: %{name}-%{version}.patch

%description
The leave command is a simple text reminder. It advices you
needs to leave at the programmed hour. Also it advices you when
the last five minutes.

%prep
%setup -q
%patch0 -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 0755 leave $RPM_BUILD_ROOT/usr/bin/leave
install -Dm 0644 leave.1 $RPM_BUILD_ROOT/usr/share/man/man1/leave.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/*
%{_mandir}/*/*

%changelog
* Wed Mar 25 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8
- Rebuilt for Fedora
* Thu Dec 14 2000 Ismael Olea <olea@hispafuentes.com>
Corregidas algunas erratas de Juanjo }:-)
* Thu Dec 14 2000 Juan J. Amor <jjamor@hispalinux.es>
First version. Some ideas taken from the equivalent Debian
package.

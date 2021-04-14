Name: firc
Summary: An IRC client for the console
Version: 1.34
Release: 4.1
Group: Applications/Communications
License: GPLv2
URL: http://www.vanheusden.com/f-irc/
Source0: http://www.vanheusden.com/f-irc/fi-%{version}.tgz
BuildRequires: ncurses-devel

%description
F-IRC's goal is to be as user friendly as possible with easy navigation
and keyboard shortcuts for quick navigation. It has an as much a gentle
learning curve as possible.

%prep
%setup -q -n fi-%{version}

%build
export LDFLAGS=-Wl,--allow-multiple-definition
make %{?_smp_mflags} DESTDIR=

%install
make install DESTDIR=%{buildroot}/usr

%files
%{_datadir}/doc/f-irc
%{_bindir}/*
%{_mandir}/man1/*.1.*

%changelog
* Sat Feb 08 2014 Wei-Lun Chao <bluebat@member.fsf.org> - 1.34
- Rebuilt for Fedora

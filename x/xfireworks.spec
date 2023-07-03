%undefine _debugsource_packages

Name: xfireworks
Summary: Fireworks in your root window
Version: 1.3
Release: 9.1
Group: Amusements/Graphics
License: GPL
URL: https://kozos.jp/myfreesoft/#11
Source0: https://kozos.jp/myfreesoft/%{name}-%{version}.tar.gz
BuildRequires: libX11-devel

%description
XFireworks makes fireworks in the root window on X.
This is imitation of Japanese "Hanabi Taikai". It is very popular event
in Japanese summer and performed on some rivers.

Sumidagawa River's Hanabi Taikai is very popular. The author has seen
Arakawa River's Hanabi Taikai every year.

%prep
%setup -q

%build
make %{?_smp_mflags} X11BASE=/usr BINDIR=%{_bindir} LIBDIR=%{_sysconfdir} MANDIR=%{_mandir}/man1

%install
make install BINDIR=%{buildroot}%{_bindir} LIBDIR=%{buildroot}%{_sysconfdir} MANDIR=%{buildroot}%{_mandir}/man1

%files
%doc README NEWS COPYING COPYRIGHT ChangeLog AUTHORS HISTORY
%{_bindir}/*
%{_mandir}/man1/%{name}.1.*
%{_sysconfdir}/%{name}.conf

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora

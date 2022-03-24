Summary:	ASCII Jump Game
Name:		asciijump
Version:	1.0.2beta
Vendor:		Grzegorz Moskal <eldevarth@nemerle.org>
Release:	1
License:	GPL
Group:		Applications/Games
Source0:	http://asciijump.prv.pl/%{name}-%{version}.tar.gz
BuildRequires:	slang-devel

%description
Ski jumping in text mode.

%description -l pl
Skoki narciarskie w trybie tekstowym.

%prep
%setup -q
sed -i '32,35s|printf(|printf("%s",|' cmdline.c

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README-pl README
%{_bindir}/asciijump
%{_bindir}/aj-server
%{_datadir}/asciijump
%{_mandir}/man6/*
%{_datadir}/applications/asciijump.desktop
%exclude /usr/X11R6/share/pixmaps/asciijump.png
%{_datadir}/pixmaps/asciijump.png
/var/games/asciijump

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.2beta
- Rebuilt for Fedora

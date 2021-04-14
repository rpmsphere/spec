Name:         advancemenu
Release:      6.1
Group:        Games
License: GPL
BuildRequires:  SDL-devel gcc-c++ mesa-libGL-devel
Version:      2.7
Summary:      An emulator frontend
Source: http://prdownloads.sourceforge.net/advancemame/%{name}-%{version}.tar.gz
URL: http://advancemame.sourceforge.net/menu-readme.html

%description
AdvanceMENU is a frontend for AdvanceMAME, MAME™, MESS, RAINE and any other
emulator with sound and animated previews of your games.

%prep
%setup -q

%build
%configure
make

%install
make install prefix=$RPM_BUILD_ROOT/usr bindir=$RPM_BUILD_ROOT/%_bindir mandir=$RPM_BUILD_ROOT/%_mandir docdir=$RPM_BUILD_ROOT%_docdir

%clean
rm -fr $RPM_BUILD_ROOT

%files
%{_bindir}/adv*
%{_mandir}/man1/*
%{_docdir}/advance

%changelog
* Mon Jan 12 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 2.7
- Rebuilt for Fedora

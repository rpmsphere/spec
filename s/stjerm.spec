Name:           stjerm
Version:        0.18
Release:        5.1
Summary:        A roll-down, quake-like terminal emulator
License:        GPLv2
URL:            https://github.com/stjerm/stjerm
Source0:        https://github.com/stjerm/stjerm/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gtk2-devel
BuildRequires:  libXinerama-devel
BuildRequires:  vte-devel

%description
Stjerm is a roll-down, quake-like terminal emulator. Its window is shown 
with a key shortcut. Stjerm is very minimalistic and works well with Compiz 
window manager.

%prep
%setup -q

%build
autoreconf -fiv
%configure
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%doc AUTHORS CHANGES.md COPYING README.md
%{_bindir}/stjerm
%{_mandir}/man8/stjerm.8*

%changelog
* Fri Apr 07 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 0.18
- Rebuilt for Fedora
* Fri Jun 19 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.18-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Fri Feb 21 2014 Christopher Meng <rpm@cicku.me> - 0.18-2
- SPEC cleanup.
* Thu Jan 16 2014 Christopher Meng <rpm@cicku.me> - 0.18-1
- Initial Package.

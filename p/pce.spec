%global srcdate 20211108
%global srcserial 09abd2e3

Name:           pce
Version:        0.2.2
Release:        1.%{srcdate}
Summary:        A collection of microcomputer emulators
License:        GPLv2
URL:            https://www.hampa.ch/%{name}/about.html
Source0:        https://www.hampa.ch/pub/%{name}/pre/%{name}-%{srcdate}-%{srcserial}/%{name}-%{srcdate}-%{srcserial}.tar.gz
Obsoletes:      %{name}-sim6502 <= 0.2.2
BuildRequires:  gcc
BuildRequires:  nasm
BuildRequires:  readline-devel
BuildRequires:  SDL2-devel

%description
A collection of microcomputer emulators, including Atari ST, IBM PC, Mac Plus,
RC759 as well as a large collection of simulators.

%package atarist
Summary: An Atari ST emulator from the PCE collection
Requires: pce%{?_isa} = %{version}-%{release}

%description atarist
The Atari ST emulator from the PCE collection of emulators and simulators.

%package cpm80
Summary: A CPM80 simulator from the PCE collection
Requires: pce%{?_isa} = %{version}-%{release}

%description cpm80
The CPM80 simulator from the PCE collection of emulators and simulators.

%package ibmpc
Summary: An IBM PC emulator from the PCE collection
Requires: pce%{?_isa} = %{version}-%{release}

%description ibmpc
The IBM PC 5150 emulator from the PCE collection of emulators and simulators.

%package dos
Summary: A DOS command line simulator from the PCE collection
Requires: pce%{?_isa} = %{version}-%{release}

%description dos
A DOS command line simulator from the PCE collection of emulators and
simulators.

%package macplus
Summary: A Mac Classic/Plus/SE emulator from the PCE collection
Requires: pce%{?_isa} = %{version}-%{release}

%description macplus
An Apple Mac Classic, Plus and SE emulator from the PCE collection of emulators
and simulators.

%package rc759
Summary: An RC 759 emulator from the PCE collection
Requires: pce%{?_isa} = %{version}-%{release}
%description rc759

An RC759 (Regnecentralen) Piccoline emulator from the PCE collection of
emulators and simulators.

%package vic20
Summary: A VIC 20 emulator from the PCE collection
Requires: pce%{?_isa} = %{version}-%{release}

%description vic20
A Commodore VIC20 emulator from the PCE collection of emulators and simulators.

%package sim405
Summary: A PowerPC 405 simulator from the PCE collection
Requires: pce%{?_isa} = %{version}-%{release}

%description sim405
A PowerPC 405 simulator from the PCE collection of emulators and simulators.

%package simarm
Summary: An ARM simulator from the PCE collection
Requires: pce%{?_isa} = %{version}-%{release}

%description simarm
An ARM simulator from the PCE collection of emulators and simulators.

%package sims32
Summary: A SPARC 32 simulator from the PCE collection
Requires: pce%{?_isa} = %{version}-%{release}

%description sims32
A SPARC 32 simulator from the PCE collection of emulators and simulators.

%prep
%setup -qn %{name}-%{srcdate}-%{srcserial}

%build
%configure  --enable-atari-st \
            --enable-cpm80 \
            --enable-ibmpc \
            --enable-ibmpc-rom \
            --enable-macplus \
            --enable-rc759 \
            --enable-sim405 \
            --enable-sims32 \
            --enable-simarm \
            --enable-vic20 \
            --enable-tun \
            --enable-char-posix \
            --enable-char-ppp \
            --enable-char-pty \
            --enable-char-slip \
            --enable-char-tcp \
            --enable-char-termios \
            --disable-char-wincom \
            --enable-sound-oss \
            --enable-readline \
            --with-sdl \
            CFLAGS="%optflags -fcommon"

# Requires a 68k cross-compiler
#            --enable-macplus-rom \
make %{?_smp_mflags} CFLAGS="%optflags -fcommon"

%install
%make_install

%files
%dir %{_sysconfdir}/%{name}
%dir %{_datadir}/%{name}
%{_bindir}/pfi
%{_bindir}/pri
%{_bindir}/psi
%{_bindir}/pti
%{_bindir}/%{name}-img
%{_mandir}/man1/pri.1.gz
%{_mandir}/man1/psi.1.gz
%{_mandir}/man1/pfi.1.gz
%{_mandir}/man1/pti.1.gz
%{_mandir}/man1/%{name}-img.1.gz
%license COPYING
%doc AUTHORS ChangeLog NEWS

%files atarist
%{_bindir}/%{name}-atarist
%{_bindir}/aym
%{_mandir}/man1/%{name}-atarist.1.gz
%{_mandir}/man1/aym.1.gz
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-atarist.cfg

%files cpm80
%{_bindir}/%{name}-cpm80
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-cpm80.cfg

%files ibmpc
%{_bindir}/%{name}-ibmpc
%{_mandir}/man1/%{name}-ibmpc.1.gz
%{_datadir}/%{name}/ibmpc
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-ibmpc.cfg

%files dos
%{_bindir}/%{name}-dos
%{_mandir}/man1/%{name}-dos.1.gz

%files macplus
%{_bindir}/%{name}-macplus
%{_datadir}/%{name}/macplus
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-mac-classic.cfg
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-mac-plus.cfg
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-mac-se.cfg

%files rc759
%{_bindir}/%{name}-rc759
%{_mandir}/man1/%{name}-rc759.1.gz
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-rc759.cfg

%files vic20
%{_bindir}/%{name}-vic20
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-vic20.cfg

%files sim405
%{_bindir}/%{name}-sim405
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-sim405.cfg

%files simarm
%{_bindir}/%{name}-simarm
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-simarm.cfg

%files sims32
%{_bindir}/%{name}-sims32
%config(noreplace) %{_sysconfdir}/%{name}/%{name}-sims32.cfg

%changelog
* Sun Nov 27 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.2
- Rebuilt for Fedora
* Sat Nov 20 2021 RPMBuilder - 0.2.2-1.20211108
- Upgraded to latest version
* Tue Dec 29 2020 RPMBuilder - 0.2.2-1.20201020
- Upgraded to latest version
- Use the ISA for the requires with sub packages
- 6502 simulator has been removed upstream
- Added new emulator VIC20
* Mon May 11 2020 RPMBuilder - 0.2.2-1.20191006
- Upgraded to latest version
- Added -fcommon to C flags. This reverses a GCC 10 default for failing on
  multiple defines. Should really be fixed upstream
* Sun May 26 2019 RPMBuilder - 0.2.2-1.20181220
- Upgrade to latest version
* Sun Nov 11 2018 RPMBuilder - 0.2.2-1.20181110
- Upgrade to latest version
- Now compiled against SDL2
- Updated BRs due to new F29 buildroot
* Wed Jun 07 2017 RPMBuilder - 0.2.2-1.20170208
- Initial RPM Release

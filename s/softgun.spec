Name:         softgun
License:      GPL
Group:        System/Emulators/Other
Version:      0.21
Release:      3.1
Summary:      ARM, ATMega, M32C, and R8C Board Emulator
Source:       https://sourceforge.net/projects/softgun/files/softgun/%{name}-%{version}/%{name}-%{version}.tgz
URL:          https://softgun.sourceforge.net/
BuildRequires: zlib-devel alsa-lib-devel

%description
Softgun is a an embedded system simulator. Softgun is known to run Linux
blob and u-boot for the ARM-9 processors Digi NS9750, Freescale i.MX21 and
Atmel AT91RM9200.  Softgun can also emulate the ATMega 644-based game
console "Uzebox", the Renesas Microcontrollers M32C and R8C.

%prep
%setup -q

%build
make %{?jobs:-j%jobs} CFLAGS="$RPM_OPT_FLAGS -fPIC -ldl -Wl,--allow-multiple-definition" prefix=/usr

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
make install prefix=$RPM_BUILD_ROOT/usr

%files
%doc README configs
%{_bindir}/*

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.21
- Rebuilt for Fedora
* Mon Jul 12 2010 uli@suse.de
- update -> 0.18
* Fri Nov 28 2008 uli@suse.de
- fixed rpmlint complaint
* Fri Jun 13 2008 uli@suse.de
- fixed to build with new toolchain

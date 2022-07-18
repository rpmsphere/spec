%undefine _debugsource_packages

Name: linapple
Summary: Apple2 emulator for Linux
Version: 2.2.1
Release: 1
Group: Emulators
License: GPL
URL: https://github.com/linappleii/linapple
Source0: %{name}-master.zip
BuildRequires: gcc-c++, SDL-devel, libcurl-devel, libzip-devel

%description
Linapple is an emulator of Apple2 (Apple][, Apple 2, Apple2e) series computers
for Linux or other systems with SDL support, which works out of the box.
It derives from AppleWin, and almost as powerful as AppleWin is.

%prep
%setup -q -n %{name}-master
sed -i 's|-Wall|-fpermissive|' Makefile

%build
%make_build

%install
install -Dm755 build/bin/linapple %{buildroot}/usr/bin/linapple
install -Dm644 build/share/linapple/Master.dsk %{buildroot}/usr/share/linapple/Master.dsk
install -Dm644 build/etc/linapple/linapple.conf %{buildroot}/etc/linapple/linapple.conf

%files
%doc CHANGELOG COPYING.txt README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_sysconfdir}/%{name}

%clean
%__rm -rf $RPM_BUILD_ROOT

%changelog
* Sun Jun 19 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 2.2.1
- Rebuilt for Fedora

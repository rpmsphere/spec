%undefine _debugsource_packages

Name: uvncrepeater-ac
Version: 1.0.0
Release: 1
Source: %name-%version.tar
Summary: VNC repeater based on ultravnc repeater
URL: https://github.com/tenchman/uvncrepeater-ac
License: GPL2+
Group: Networking/Remote access
BuildRequires: gcc

%description
Ansi-C Version of uvncrepeater V14

Changes:
* removed C++ compiler dependency
* compilable with 'any?' Ansi-C compiler (tested with gcc, clang, tcc)
* IPv6 support
* support CIDR addresses in server lists

Uvncrepeater V14 is Jari Korhonen's Linux port of Ultravnc repeater source code.

%prep
%setup -q

%build
%make_build

%install
%makeinstall
install -pDm644 systemd/%{name}.service %{buildroot}%{_unitdir}/%{name}.service

%files
%{_sysconfdir}/uvnc/uvncrepeater-ac.ini
%{_bindir}/uvncrepeater-ac
%{_unitdir}/%{name}.service

%changelog
* Sun Mar 13 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuilt for Fedora
* Mon Dec 16 2019 Grigory Maksimov <zacat@altlinux.org> 1.0.0-alt1
- Initial build for ALT


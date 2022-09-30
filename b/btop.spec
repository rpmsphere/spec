Name:           btop
Version:        1.2.9
Release:        1
Summary:        A monitor of resources
Group:          Monitoring
License:        Apache License 2.0
URL:            https://github.com/aristocratos/btop
Source:         %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

%description
Resource monitor that shows usage and stats for processor, memory, disks,
network and processes.
C++ version and continuation of bashtop and bpytop.

%prep
%autosetup

%build
export CC="/usr/bin/gcc"
export CXX="/usr/bin/g++"
%set_build_flags
%make_build

%install
%make_install PREFIX=%{_prefix}

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.*

%changelog
* Sun Sep 25 2022 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.9
- Rebuilt for Fedora
* Sun Jan 16 2022 kekepower <kekepower> 1.2.0-1.mga9
+ Revision: 1768721
- Update to version 1.2.0
* Wed Dec 29 2021 kekepower <kekepower> 1.1.4-1.mga9
+ Revision: 1765363
- Update to version 1.1.4
* Sat Dec 11 2021 kekepower <kekepower> 1.1.3-1.mga9
+ Revision: 1761515
- Update to version 1.1.3
* Sat Nov 27 2021 kekepower <kekepower> 1.1.2-1.mga9
+ Revision: 1759692
- Update to version 1.1.2
* Tue Nov 16 2021 kekepower <kekepower> 1.1.1-1.mga9
+ Revision: 1757104
- Update to version 1.1.1
* Sun Nov 14 2021 kekepower <kekepower> 1.1.0-1.mga9
+ Revision: 1756218
- Update to version 1.1.0
* Wed Nov 10 2021 kekepower <kekepower> 1.0.24-1.mga9
+ Revision: 1755597
- Update to version 1.0.24
* Mon Nov 08 2021 kekepower <kekepower> 1.0.23-1.mga9
+ Revision: 1754785
- Update to version 1.0.23
* Thu Nov 04 2021 kekepower <kekepower> 1.0.22-1.mga9
+ Revision: 1753874
- Update to version 1.0.22
+ wally <wally>
- build debug pkgs and use our build time flags
* Fri Oct 29 2021 kekepower <kekepower> 1.0.20-1.mga9
+ Revision: 1753274
- imported package btop

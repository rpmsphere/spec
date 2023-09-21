%global __spec_install_post %{nil}
%global debug_package %{nil}

Summary: 	A GUI utility to control and monitor AMD GPU
Name: 		systemdeck
Version: 	1.01.68.00
Release: 	1.bin
License: 	Refer to LICENSE.TXT
Group:		Hardware/Tools
Source0:	AMDSystemDeck_x86_64_v%{version}.tar.gz
Source1:	%{name}.desktop
Source2:        %{name}.png

%description
AMD SystemDeck is a GUI utility to control and monitor GPU device parameters
such as clocks, voltage, temperature, etc. Supported Devices:
AMD GPU (discrete or integrated) from HD2XXX and up.

%prep
%setup -q -c

%build

%install
install -Dm755 AMDSystemDeck %{buildroot}%{_sbindir}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc CHANGES.LOG LICENSE.TXT readme.txt
%{_sbindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Sep 17 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 1.01.68.00
- Initial binary package

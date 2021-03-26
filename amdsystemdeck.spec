%global debug_package %{nil}

Summary: 	A GUI utility to control and monitor AMD GPU
Name: 		amdsystemdeck
Version: 	1.01.00.00
Release: 	1.bin
License: 	Refer to LICENSE.TXT
Group:		Hardware/Tools
Source0:	SystemDeck_1_1_0_0.tar.gz
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
* Fri Jul 17 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.01.00.00
- Initial binary package

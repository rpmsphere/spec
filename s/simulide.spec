%undefine _missing_build_ids_terminate_build
%global _name SimulIDE

Name: simulide
Summary: Simple real time electronic circuit simulator
Version: 1.1.0
Release: 0.sr0
Group: electronics
License: GPLv3
URL: https://simulide.com/p/
Source0: https://launchpad.net/simulide/1.1.0/1.1.0-sr0/+download/%{_name}_%{version}/%{_name}_%{version}-SR0_sources.zip
Source1: %{name}.desktop
Source2: %{name}.png
BuildRequires: desktop-file-utils
BuildRequires: gpsim-devel
BuildRequires: elfutils-libelf-devel
BuildRequires: qt5-qtbase-devel

%description
Simulide is a real time electronic circuit simulator intended for hobbist and
student experimentation with simple general purpose electronic circuits and
PIC, AVR and Arduino microcontroller simulations.

PIC and AVR simulation are provided by gpsim and simavr.

%prep
%setup -q -n %{_name}_%{version}-SR0_sources
touch config.h

%build
cd build_XX
%qmake_qt5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/%{name}
cd build_XX/executables/%{_name}_%{version}-SR0
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}
cp -a data examples %{buildroot}%{_datadir}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc COPYING README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Sun Nov 17 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1.0
- Rebuilt for Fedora

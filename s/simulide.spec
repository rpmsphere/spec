Name: simulide
Summary: Simple real time electronic circuit simulator
Version: 0.2.8
Release: 6.1
Group: electronics
License: GPLv3
URL: http://simulide.blogspot.com/
Source0: https://dl.sourceforge.net/project/simulide/SimulIDE_%{version}/%{name}_%{version}-sources.tar.gz
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
%setup -q -n %{name}_%{version}
touch config.h

%build
cd build_XX
%qmake_qt5
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr
cd build_XX/release/SimulIDE_%{version}
cp -a * %{buildroot}/usr
mv %{buildroot}%{_bindir}/SimulIDE_%{version} %{buildroot}%{_bindir}/%{name}
install -Dm644 %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
install -Dm644 %{SOURCE2} %{buildroot}%{_datadir}/pixmaps/%{name}.png

%files
%doc COPYING README.md
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Thu Jul 26 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.8
- Rebuilt for Fedora

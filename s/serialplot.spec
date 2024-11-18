%undefine _debugsource_packages

Name: serialplot
Summary: Small and simple software for plotting data from serial port
Version: 0.6
Release: 1
Group: devel
License: Free Software
Source0: %{name}-%{version}.tar.gz
BuildRequires: desktop-file-utils
BuildRequires: qwt5-qt5-devel
BuildRequires: qwt5-qt4-devel
BuildRequires: qt5-qtserialport-devel
BuildRequires: qt5-qtsvg-devel
#Requires: libqt5widgets5
#Requires: libqt5svg5
#Requires: libqt5serialport5

%description
Supports binary data formats ([u]int8, [u]int16, [u]int32, float)
and ASCII (as CSV). Captured waveforms can be exported in CSV format.
Can also send simple user defined commands to serial port device.

%prep
%setup -q
sed -i '22i #include <math.h>' src/plot.cpp src/dataformatpanel.cpp src/plotcontrolpanel.cpp

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr .
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}

%files
%{_docdir}/%{name}
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Dec 12 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6
- Rebuilt for Fedora

Name: qst
Summary: Q Serial Terminal
Version: 1.01
Release: 10.1
Group: Applications/Communications
License: GPL
URL: https://sourceforge.net/projects/qst/
Source0: https://sourceforge.net/projects/qst/files/QST-source/%{name}-source-%{version}.tgz
BuildRequires: qt-devel, qextserialport-devel

%description
A QT-based serial terminal program. Works on Linux or Windows.
Basic serial terminal for use with embedded systems.

%prep
%setup -q -n %{name}

%build
qmake-qt4
sed -i -e 's|-I/usr/include/QtCore|-I/usr/include/QtCore -I/usr/include/QtExtSerialPort|' -e 's|-lQtCore|-lQtCore -lqextserialport-1.2|' Makefile
make %{?_smp_mflags}

%install
install -Dm755 %{name} %{buildroot}%{_bindir}/%{name}

%files
%doc COPYING README
%{_bindir}/%{name}

%changelog
* Sun May 26 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.01
- Rebuilt for Fedora

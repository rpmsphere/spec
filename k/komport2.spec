Name: komport2
Summary: An alternative to minicom in Qt
Version: 1.0.0
Release: 6.1
Group: Applications/Communications
License: GPLv2
URL: http://sourceforge.net/projects/komport2/
Source0: http://sourceforge.net/projects/komport2/files/source/%{name}-%{version}-src.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: qt-devel

%description
Komport is an serial port communications and vt102 terminal emulator for Qt.
Aim of the project is to provide an alternative to minicom with an Qt style
user interface.

%prep
%setup -q -n %{name}/1.0
sed -i '1i #include <unistd.h>' cdevicelock.cpp

%build
qmake-qt4
make %{?_smp_mflags}

%install
install -Dm755 komport %{buildroot}%{_bindir}/%{name}

%files
%doc README.TXT
%{_bindir}/%{name}

%changelog
* Sun May 26 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.0
- Rebuild for Fedora

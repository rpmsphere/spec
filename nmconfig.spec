%global debug_package %{nil}

Name:           nmconfig
URL:            http://cmpd2.phys.msu.ru/~arseniy/nmconfig/
Version:        0.2.4
Release:        3.1
License:        GPL v2 or later
BuildRequires:  gcc-c++ qt-devel
Group:          Productivity/Networking/System
Summary:        Qt based command-line tool for NetworkManager
Source0:        %{name}-%{version}.tar.gz
Requires:       NetworkManager >= 0.7

%description
Command-line client for NetworkManager intended to replace GUI applets.
Unlike those applets, it only deals with system connections.

%prep
%setup -q

%build
qmake-qt4
make

%install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -m 755 bin/%{name} $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf "$RPM_BUILD_ROOT"

%files
%{_bindir}/%{name}

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.4
- Rebuild for Fedora

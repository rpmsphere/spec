%undefine _debugsource_packages

Name: noxim
Summary: The NoC Simulator
Version: 20131016
Release: 13.1
Group: Development/Tools
License: GPL
URL: http://www.noxim.org/
Source0: http://sourceforge.net/projects/noxim/files/noxim/%{name}-%{version}.tar.gz
BuildRequires: systemc

%description
Welcome to Noxim, the Network-on-Chip Simulator developed at the University of
Catania (Italy). The Noxim simulator is developed using SystemC.

%prep
%setup -q -n %{name}-code
sed -i -e 's|/Library/SystemC/systemc-2.3.0|/usr|' -e 's|lib-$(TARGET_ARCH)|%{_lib}|' bin/Makefile.defs
sed -i 's|return false;|return NULL;|' src/NoximNoC.cpp

%build
make -C bin

%install
install -Dm755 bin/%{name} %{buildroot}%{_bindir}/%{name}

%files
%doc doc/*.txt
%{_bindir}/%{name}

%changelog
* Wed Dec 11 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 20131016
- Rebuilt for Fedora

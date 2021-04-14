Summary: An Altair 8800 Emulator
Name: altairrfp
Version: 1.1
Release: 3.1
License: GPL
Group: Emulator
URL: http://code.google.com/p/altair-rfp
Source: %{name}-%{version}.tar.gz
BuildRequires:  gcc-c++

%description
This is an Altair 8800 simulator, primarily written in C++. It can run in
a stand alone mode or communicate with a Briel Computers Micro 8800 device
using it as a front panel.

%prep
%setup -q

%build
make -C linux

%install
install -Dm755 linux/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a images/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%files
%defattr(-,root,root)
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.1
- Rebuilt for Fedora
* Mon Feb 21 2011 Al Williams <al.williams@awce.com>
- Initial package

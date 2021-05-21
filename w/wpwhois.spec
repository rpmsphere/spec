Summary: White pages query tool
Name: wpwhois
Version: 2.1
Release: 4.1
Group: System Environment/Base
License: Rutgers (based on GPL'd Lynx source)
Source: wpwhois-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-root

%description
Wpwhois lets you look up Rutgers faculty and students from the command line.

%prep
%setup -q

%build
./configure
make

%install
rm -rf $RPM_BUILD_ROOT
install -Dm 0755 lynx $RPM_BUILD_ROOT%{_bindir}/wpwhois
install -Dm 0644 wpwhois.1 $RPM_BUILD_ROOT%{_mandir}/man1/wpwhois.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/wpwhois
%{_mandir}/man1/wpwhois.1.*

%changelog
* Sun Sep 23 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1
- Rebuilt for Fedora

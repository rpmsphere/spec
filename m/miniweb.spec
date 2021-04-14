%undefine _debugsource_packages

Name:    miniweb
Version: 0.2.0
Release: 4.1
Summary: A browser tool which uses different User Agents and screen sizes to test mobile versions of websites
License: GPLv3
Group:   Applications/Network
URL:     http://bernd-stramm.com/
Source: miniweb-0.2.0.tar.gz
BuildRequires:  libpng-devel
BuildRequires:  qt4-devel qt4-webkit-devel
BuildRequires:  gcc-c++

%description
A webkit-based browser tool which uses different User Agents and screen sizes to test mobile versions of websites.

%prep
%setup -q

%build
sh configure
make 

%install
rm -rf $RPM_BUILD_ROOT
install -p -d $RPM_BUILD_ROOT%{_bindir}
install -p -m 755 miniweb $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README
%doc COPYRIGHT
%doc LICENSE.txt
%doc helpman.html
%{_bindir}/miniweb

%changelog
* Mon Apr 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.2.0
- Rebuilt for Fedora
* Wed Apr 23 2010 Bernd Stramm <bernd.stramm@gmail.com> - 0.2.0-1
- Initial RPM release

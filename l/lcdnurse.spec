%undefine _debugsource_packages

Name: lcdnurse
Summary: LCD Nurse
Version: 1.0.3
Release: 6.1
Group: Applications/Tools
License: GPLv3
URL: http://congelli.eu/prog_info_lcdnurse.html
Source0: http://congelli.eu/download/lcdnurse/%{name}-%{version}.tar.gz
BuildRequires: wxGTK2-devel

%description
Repair dead pixels is now possible on Linux (GNU/Linux) ! LCD Nurse is a free
program wich enable you to "heal" dead pixels on your LCD screen thanks to
the blink method.

%prep
%setup -q
sed -i '31,35d' src/findFile.cpp

%build
%configure
make %{?_smp_mflags} CXXFLAGS+="-fPIC -fPIE"

%install
%make_install

%files
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-icon.png

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuilt for Fedora

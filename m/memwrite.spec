%undefine _debugsource_packages

Name: memwrite
Summary: It enable you to edit program's memory
Version: 1.0.3
Release: 20.1
Group: Amusements/Games
License: GPLv3
URL: http://congelli.eu/prog_info_memwrite.html
Source0: http://congelli.eu/download/memwrite/%{name}-%{version}.tar.gz
BuildRequires: wxGTK-devel

%description
This small program is a free and open source equivalent of ArtMoney(on Windows)
or The Cheat (on Mac)... but it works only with Linux. With it you can edit
numbers stocked in your computer memory... to cheat in game... for example.

%prep
%setup -q

%build
autoreconf -ifv
./configure --prefix=/usr
make CXXFLAGS+="-fpermissive -fPIC "

%install
%make_install

%files
%doc README COPYING ChangeLog AUTHORS
%{_bindir}/%{name}
%{_bindir}/lunch-%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}-icon.png
%{_mandir}/man1/%{name}.1.*

%changelog
* Mon Oct 21 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.3
- Rebuilt for Fedora

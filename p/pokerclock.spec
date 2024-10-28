%undefine _debugsource_packages

Name:                            pokerclock
Version:                         1.0.6
Release:                         7.1
Summary:                         Poker Tournament Clock
Source:                  pokerclock-%{version}.tar.bz2
Patch1:         pokerclock-fix_cmake.patch
Patch2:         pokerclock-fix_paths.patch
URL:                             https://sourceforge.net/projects/pokerclock/
Group:                   Amusements/Games
License:                         GNU General Public License version 2 or later (GPL v2 or later)
BuildRequires:   libpng-devel
BuildRequires:   qt4-devel openssl-devel
BuildRequires:   gcc-c++ cmake gcc make glibc-devel

%description
A clock for tournaments of Poker.

Main features:
* Small/Big blinds
* Antes
* Blinds/Antes Time
* Total Time
* ReBuy
* AddOn
* Avg Stack
* Total Stack
* Total Prize 

%prep
%setup -q -n pokerclock
%patch 1
%patch 2
%__mv src/sounds/event.wav src/sounds/pokerclock-event.wav

%build
mkdir -p build
pushd build
cmake -DCMAKE_INSTALL_PREFIX="%{_prefix}" -DCMAKE_VERBOSE_MAKEFILE=ON ..
%__make %{?jobs:-j%{jobs}}
popd #build

%install
pushd build
make DESTDIR=$RPM_BUILD_ROOT install
popd #build
sed -i 's|Game;|Game;Emulator;|' %{buildroot}%{_datadir}/applications/pokerclock.desktop

%files
%doc CHANGELOG COPYING TODO
%{_bindir}/pokerclock
%{_datadir}/applications/pokerclock.desktop
%{_datadir}/pixmaps/pokerclock.png
%{_datadir}/sounds/pokerclock-event.wav

%changelog
* Wed Nov 30 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.6
- Rebuilt for Fedora
* Fri Jun 11 2010 pascal.bleser@opensuse.org
- initial package (1.0.6)

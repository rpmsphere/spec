%global theme_name Tux

Name:           tux-cursor-theme
License:        GPL v2 only
Group:          User Interface/Desktops
Summary:        Tux Cursors!
Version:        0.5
Release:        142.1
Source0:        tuxcursors-0.5.tar.bz2
BuildArch:      noarch
BuildRequires:  xcursorgen
BuildRequires:  libpng
BuildRequires:  libX11-devel

%description
A cursor set that has nice animated penguins.

%prep
%setup -qn tuxcursors

%build
./build.sh

%install
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons
cp -a tuxcursors $RPM_BUILD_ROOT%{_datadir}/icons/%{theme_name}

%files
%{_datadir}/icons/%{theme_name}
%doc LICENSE COPYING

%changelog
* Tue Oct 25 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5
- Rebuilt for Fedora
* Tue Oct  7 2008 jw@suse.de
- added /usr/bin/tuxcursors
  shell script with some helpful logic and info.
  Needed, since I could not find a way to start
  KDE Control Center from the SUSE Menu at 11.0
* Wed Feb 13 2008 seife@suse.de
- add libpng to buildrequires, since otherwise 10.2 build fails
* Tue Feb 12 2008 seife@suse.de
- add stupid application cursor symlinks
* Tue Feb 12 2008 seife@suse.de
- initial package submission

Name:		aumix
Summary:	A GTK+/Ncurses audio mixer 
Version:	2.9.1
Release:	13.1
License:	GPL
Group:		Sound/Mixers
BuildRequires:	ncurses-devel
BuildRequires:	gtk2-devel
BuildRequires:	autoconf
BuildRequires:	automake
Source0:	http://www.jpj.net/~trevor/aumix/%{name}-%{version}.tar.bz2
URL: 		http://www.jpj.net/~trevor/aumix.html

%description
This is a program for adjusting audio mixers from the command line or scripts,
or interactively at the console or a terminal with a full-screen, ncurses-based
interface or a GTK-based X interface.

%prep
%setup -q

%build
%ifarch aarch64
autoreconf -ifv
%endif
sed -i 's|-g -O2|-g -O2 -Wl,--allow-multiple-definition|' configure
mkdir build-text
pushd build-text
../configure --prefix=/usr --with-alsa --without-gtk1 --without-gtk
make
popd
mkdir build-gui
pushd build-gui
../configure --prefix=/usr --with-alsa --without-gtk1
make
popd

%install
%makeinstall -C build-gui

# install text version
install -m755 build-text/src/aumix %{buildroot}%{_bindir}/aumix-text

# menu entry
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Name=Aumix
Comment=Basic volume controller
Exec=%{name}
Icon=multimedia-volume-control
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;AudioVideo;Mixer;
EOF

%find_lang %name

%post
modprobe snd-pcm-oss

%files -f %{name}.lang
%doc README TODO NEWS ChangeLog
%_bindir/aumix
%_bindir/mute
%_bindir/xaumix
%_mandir/man1/*
%_datadir/applications/*
%_datadir/%name
%_bindir/aumix-text

%changelog
* Sat Aug 03 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 2.9.1
- Rebuild for Fedora
* Fri Jan 11 2013 umeabot <umeabot> 2.9.1-3.mga3
+ Revision: 346603
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild
* Sun Nov 25 2012 zezinho <zezinho> 2.9.1-2.mga3
+ Revision: 321873
- fix rpm group
* Wed Sep 07 2011 tv <tv> 2.9.1-1.mga2
+ Revision: 140082
- new release
- drop merged patches
* Tue Jan 11 2011 blino <blino> 2.8-22.mga1
+ Revision: 5706
- use macros for vendor name
- remove old ldconfig scriptlets
  + pterjan <pterjan>
    - imported package aumix

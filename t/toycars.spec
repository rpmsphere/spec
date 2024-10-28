Name:                   toycars
Summary:                Toy Cars is a physics based 2-D racer
License:                GPL
Group:                  Amusements/Games/Action/Race
Version:                0.3.7
Release:                1
URL:                    https://sourceforge.net/projects/toycars/
Source:                 %{name}-%{version}.tar.gz
Patch0:                 %{name}-64bit.patch
Patch1:                 %{name}-gcc43.patch
BuildRequires:  gcc-c++
#BuildRequires: Mesa-devel
BuildRequires:  mesa-libGL-devel
#BuildRequires: libfmodex-devel
BuildRequires:  pkgconfig
BuildRequires:  SDL-devel
BuildRequires:  SDL_image-devel
#BuildRequires: update-desktop-files

%description
Toy Cars is a physics based 2-D racer.

The current build implements three modes of play. These are: Timed
Race, Hot Potato, and Knock 'em Out. You can have up to 16 human
or computer controlled players except in Hot Potato mode which
only supports two human controlled players. There is also a track
editor.

In Timed Race mode the aim is to complete four laps in the best
time you can.

In Hot Potato mode the aim is to avoid having the bomb when the
fuse runs out. The bomb can be transfered between players if they
crash into each other with sufficient velocity.

In Knock 'em Out mode the aim is to race around the track and to
try and prevent your car from going off the screen.


%prep
%setup -q -n %{name}-%{version}
%patch 0 -p1
%patch 1 -p1

%ifarch x86_64
%__sed -i -e 's|lfmodex|lfmodex64|g' \
        configure
%endif

%__rm data/tracks/._tracklist.xml
%__rm data/tracks/Hairpin/._Hairpin.map.Aoj

%build
export CPPFLAGS="$RPM_OPTF_LAGS -fPIC -I%{_includedir}/fmodex"
export CXXFLAGS="$RPM_OPTF_LAGS -fPIC -I%{_includedir}/fmodex"
%configure
%__make %{?jobs:-j%{jobs}}

%install
%makeinstall

# install the menu icon
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 celica-render.png \
        %{buildroot}%{_datadir}/pixmaps/%{name}.png

# install menu entry
%__install -dm 755 %{buildroot}%{_datadir}/applications
%{__cat} > %{name}.desktop << EOF
[Desktop Entry]
Name=Toy Cars
Name[zh_TW]=極速賽車手
Comment=Toy Cars is a physics based 2-D racer
Comment[zh_TW]=極速賽車手裡有法拉利﹑Viper和多種車輛供玩家選擇，有計時制也有圈數制，盡情的跑在最前面吧!
Exec=%{name}
Icon=%{name}.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Game;SportsGame;
EOF

%__install -m 644 %{name}*.desktop \
        %{buildroot}%{_datadir}/applications

%files
%doc AUTHORS ChangeLog COPYING README TODO
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}*.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.7
- Rebuilt for Fedora
* Tue Oct 21 2008 Feather Mountain <john@ossii.com.tw> - 0.3.7-0.1.ossii
- Rebuild for M6(OSSII)
* Thu Jul 03 2008 Toni Graffy <toni@links2linux.de> - 0.3.7-0.pm.1
- update to 0.3.7
* Sat Jun 28 2008 Toni Graffy <toni@links2linux.de> - 0.3.6-0.pm.1
- update to 0.3.6
* Wed Dec 19 2007 Toni Graffy <toni@links2linux.de> - 0.3.5-0.pm.1
- update to 0.3.5
* Tue Nov 06 2007 Toni Graffy <toni@links2linux.de> - 0.3.4-0.pm.1
- initial build for packman 0.3.4

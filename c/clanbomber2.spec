Name:           clanbomber2
Version:        0.9.1
Release:        1
URL:            http://clanbomber.sourceforge.net/
License:        GPL v2 or later
Group:          Amusements/Games/Action/Arcade
Summary:        Bomberman-like multiplayer game
Source:         %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         %{name}-%{version}-socklen.patch
BuildRequires:  gcc-c++ automake pkgconfig directfb-devel fusionsound-devel

%description
ClanBomber is a free (GPL) Bomberman-like multiplayer game.

%prep
%setup -q
%patch0
sed -i -e '706s/DFBResult/DirectResult/' -e '824d' clanbomber/Resources.cpp
sed -i -e 's|__u8|u8|' -e 's|__u16|u16|' -e 's|__u32|u32|' clanbomber/*.h clanbomber/*.cpp
sed -i 's|path+filename|(const char *)(path+filename)|' clanbomber/Config.cpp
sed -i 's|map_selection_file(filename)|map_selection_file((const char *)filename)|' clanbomber/Map.cpp
sed -i -e '/#define min/d' -e '/#define max/d' clanbomber/ClanBomber.h
sed -i 's|pthread_mutexattr_setkind_np|pthread_mutexattr_settype|' clanbomber/Mutex.cpp

%build
%configure
make %{?jobs:-j%jobs}

%install
make DESTDIR=$RPM_BUILD_ROOT install
%__mkdir_p $RPM_BUILD_ROOT/%{_datadir}/applications
%__cp %{SOURCE1} $RPM_BUILD_ROOT/%{_datadir}/applications/
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/pixmaps
%__cp clanbomber/pics/cup2.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING ChangeLog IDEAS README
%{_bindir}/clanbomber2
%dir %{_datadir}/clanbomber2
%{_datadir}/clanbomber2/*
%{_datadir}/applications/*.desktop
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.1
- Rebuilt for Fedora
* Fri Oct 24 2008 wind <yc.yan@ossii.com.tw>
- Rebuild for OSSII.
* Wed Oct 17 2007 prusnak@suse.cz
- created package (version 0.9.1)
- fixed socklen_t usage (socklen.patch)

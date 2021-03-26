Name:           dark-oberon
URL:            http://dark-oberon.sourceforge.net/
License:        GNU General Public License (GPL)
Group:          Amusements/Games/Strategy/Real Time
Version:        svn.2007.11.30
Release:        1
Summary:        Real-time strategy game similar to Warcraft II
Source:         dark-oberon-svn-2007-11-30.tar.bz2
Source1:       %{name}.png
Patch1:         dark-oberon-svn-2007-11-30.patch
BuildRequires:  glfw-devel gcc-c++
BuildRequires:  mesa-libGL-devel libX11-devel

%description
Dark Oberon is an open source real-time strategy game similar to Warcraft II released under GPL.
It has got unique graphics - textures created from shots of real models made out of plasticine!


Authors:
--------
Peter Knut <peter@ajtak.sk>

%prep
%setup -q -n dark-oberon
%patch1 -p1
find . -name "CVS" | xargs rm -r
find . -name "*.h" | xargs sed -i -e "s:<DATADIR>:%{_datadir}/dark-oberon:"
find . -name "*.cpp" | xargs sed -i -e "s:<DATADIR>:%{_datadir}/dark-oberon:"
sed -i -e "s:<LIB>:%{_lib}:g" src/Makefile
sed -i -e "s:<RPMOPTFLAGS>:$RPM_OPT_FLAGS:" src/Makefile
%__cp %{SOURCE1} ./
sed -i '3264s|return false|return NULL|' src/doworkers.cpp

%build
make

%install
install -d %{buildroot}%{_bindir}
install dark-oberon %{buildroot}%{_bindir}

install -d %{buildroot}%{_datadir}/dark-oberon/
%__cp -a dat/ %{buildroot}%{_datadir}/dark-oberon/
%__cp -a maps/ %{buildroot}%{_datadir}/dark-oberon/
%__cp -a races/ %{buildroot}%{_datadir}/dark-oberon/
%__cp -a schemes/ %{buildroot}%{_datadir}/dark-oberon/
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=%{name}
Comment=Real-time strategy game similar to Warcraft II
Exec=%{name}
Terminal=false
StartupNotify=true
Categories=Applications;Game
Icon=%{name}.png
Name[zh_TW]=魔黯爭霸
Comment[zh_TW]=%{name} 一款類似魔獸爭霸的遊戲
EOF
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__cp %{name}.png %{buildroot}%{_datadir}/pixmaps

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%clean
rm -rf %{buildroot};

%files
%{_bindir}/dark-oberon
%dir %{_datadir}/dark-oberon
%dir %{_datadir}/dark-oberon/dat
%dir %{_datadir}/dark-oberon/maps
%dir %{_datadir}/dark-oberon/races
%dir %{_datadir}/dark-oberon/schemes
%{_datadir}/dark-oberon/dat/*
%{_datadir}/dark-oberon/maps/*
%{_datadir}/dark-oberon/races/*
%{_datadir}/dark-oberon/schemes/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - svn.2007.11.30
- Rebuild for Fedora
* Tue Oct 21 2008 Wind Win <yc.yan@ossii.com.tw>
- Rebuild for OSSII.
* Sat Dec  1 2007 mskibbe@suse.de
- use RPM_OPT_FLAGS for build
* Fri Nov 30 2007 mskibbe@suse.de
- create package

Name:           formido
BuildRequires:  SDL_image-devel SDL_mixer-devel gcc-c++
License:        GPL v2 or later
Group:          Amusements/Games/Action/Arcade
AutoReqProv:    on
Version:        1.0.1
Release:        1
Summary:        Fast bug shooting game
URL:            http://www.mhgames.cjb.net
Source0:        %{name}-%{version}.tar.bz2
Source3:        %{name}.png
Patch:          %{name}-%{version}-make.patch
Source2:        %{name}

%description
Fast bug shooting game.

Authors:
--------
    Mika Halttunen

%prep
%setup -q
%patch

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/%{_bindir}
cp %{S:2} $RPM_BUILD_ROOT/%{_bindir}/
install -d $RPM_BUILD_ROOT/%{_datadir}/%{name}
cp -a %{name} %{name}.cfg data $RPM_BUILD_ROOT/%{_datadir}/%{name}
%__mkdir_p %{buildroot}%{_datadir}/applications/
%__cat << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=%{name}
Name[zh_TW]=除虫狙擊手
Comment=Fast bug shooting game
Comment[zh_TW]=%{name}  除虫狙擊手
Exec=%{name}
Icon=%{name}.png
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Game;ArcadeGame;
EOF
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
%__cp %{SOURCE3} %{buildroot}%{_datadir}/pixmaps

%clean
rm -rf $RPM_BUILD_ROOT

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%files
%doc INSTALL README GPL_license.txt
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0.1
- Rebuild for Fedora
* Tue Oct 21 2008 Wind <yc.yan@ossii.com.tw>
- Rebuild for OSSII.
* Mon Oct 16 2006 - pnemec@suse.cz
- package created with version 1.0.1

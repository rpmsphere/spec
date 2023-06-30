%undefine _debugsource_packages

BuildRequires:  gcc-c++ SDL-devel SDL_image-devel SDL_ttf-devel SDL_mixer-devel
Name:           2h4u
Version:        1.3
Release:        1
URL:            https://sourceforge.net/projects/toohardforyou
License:        GPL v2 or later
Group:          Amusements/Games/Action/Arcade
Summary:        Too Hard For You - a mix between a Tetris-like game and a wall breaker
Source0:        %{name}-%{version}.tar.bz2
Source1:        %{name}.desktop
Patch0:         %{name}-%{version}-datadir.patch

%description
2H4U, which stands for Too Hard For You, is an open source game, and a mix between
a Tetris-like game and a wall breaker. It requires good reflexes, coordination,
and ambidexters should have some advantages. Will 2H4U be too hard for you?

%prep
%setup -q -n 2H4U
%patch0
%{__cp} %{SOURCE1} .

%build
cd scripts
make %{?jobs:-j%jobs}

%install
install -D -m 0755 2H4U $RPM_BUILD_ROOT%{_bindir}/%{name}
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/%{name}
%__cp -a data/* $RPM_BUILD_ROOT%{_datadir}/%{name}

%__mkdir_p %{buildroot}%{_datadir}/applications/
%__mkdir_p %{buildroot}%{_datadir}/pixmaps/
%__cp %{SOURCE1} %{buildroot}%{_datadir}/applications/%{name}.desktop
%__cp %{buildroot}%{_datadir}/%{name}/images/icone.png %{buildroot}%{_datadir}/pixmaps/%{name}.png


%clean
%__rm -rf $RPM_BUILD_ROOT

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%files
%doc COPYING.txt LISEZ-MOI.txt README.txt aide help
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.3
- Rebuilt for Fedora
* Mon Oct 20 2009 Wind <yc.yan@ossii.com.tw>
- Rebuild for OSSII.
- Add desktop and icon file.
* Fri Jun 13 2008 prusnak@suse.cz
- created package (version 1.3)
- repacked Musique.mp3 to Musique.ogg
- patched game to load data from /usr/share/games and to save config
  and high scores in ~/.2h4u/{config,hiscore} (datadir.patch)

BuildRequires:  python desktop-file-utils
Requires:       python python-pygame python-opengl python-numeric python-imaging python-ogg python-vorbis python-numpy
Name:           fretsonfire
Version:        1.2.512
Release:        1
URL:            https://fretsonfire.sourceforge.net/
License:        GPL v2 or later
Group:          Amusements/Games/Action/Arcade
Summary:        A game of musical skill and fast fingers
Source:         FretsOnFire-src-%{version}.tar.bz2
Source1:        FretsOnFire-data-%{version}.tar.bz2
Source2:        FretsOnFire-datapng-%{version}.tar.bz2
Source3:        %{name}.desktop
Patch0:         %{name}-%{version}.patch
Patch1:         %{name}-%{version}-fix_glow_svg.patch
# Patch2:         %{name}-%{version}-fix_window_height_bug.patch
Patch3:         %{name}-%{version}-font-revert.patch
Patch4:         %{name}-%{version}-fonts_lower_cpu.patch
Patch5:         %{name}-%{version}-keep_sound_when_failed.patch
Patch6:         %{name}-%{version}-stage.ini.patch
Patch7:         %{name}-%{version}-svg.patch
Patch8:         %{name}-%{version}-typeerror.patch
BuildArch:      noarch

%description
Frets on Fire is a game of musical skill and fast fingers. The aim of the game
is to play guitar with the keyboard as accurately as possible.

%prep
%setup -q -n FretsOnFire-src-%{version} -a 1 -a 2
%patch0
%patch1 -p1
# %patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
chmod -x copying.txt src/*py
chmod +x src/FretsOnFire.py
# remove unneeded files
%__rm -f data/*.svg
%__rm -f data/mods/*/*.svg
%__rm -f data/translations/update.py
%__rm -f src/*.pot src/rgb2py.py src/setup*.py src/svg2png.py src/*Test*.py

%build

%install
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/games/%{name}
%__cp -a data $RPM_BUILD_ROOT%{_datadir}/games/%{name}/data
%__cp -a src/*.py $RPM_BUILD_ROOT%{_datadir}/games/%{name}
%__cp -a src/midi $RPM_BUILD_ROOT%{_datadir}/games/%{name}/midi
%__mkdir_p $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_datadir}/games/%{name}/FretsOnFire.py $RPM_BUILD_ROOT%{_bindir}/fretsonfire
install -D -m 0644 data/icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
%__mkdir_p $RPM_BUILD_ROOT%{_datadir}/applications/
%__cp %{SOURCE3} $RPM_BUILD_ROOT%{_datadir}/applications/

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/games/%{name}/*.py

%post
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%postun
update-mime-database %{_datadir}/mime &> /dev/null
update-desktop-database %{_datadir}/applications &> /dev/null

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc copying.txt readme.txt todo.txt
%{_bindir}/%{name}
%dir %{_datadir}/games/%{name}
%{_datadir}/games/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Fri Mar 02 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.512
- Rebuilt for Fedora
* Tue Oct 28 2008 Wind <yc.yan@ossii.com.tw>
- Rebuild for OSSII.
* Wed Aug  6 2008 prusnak@suse.cz
- fix broken Requires
* Wed Nov  7 2007 prusnak@suse.cz
- created package (version 1.2.512)

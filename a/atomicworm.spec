%define realname AtomicWorm
Name:           atomicworm
Version:        0.19
Release:        9.2
URL:            http://tweeler.com/index.php?PAGE=atomicw_linux
License:        GPLv3
Group:          Amusements/Games
Summary:        Atomic Worm
# http://www.tweeler.com/AtomicWorm_019_src.tar.gz
Source:         %{realname}_019_src.tar.bz2
Source1:    %{realname}.desktop
Source2:    %{realname}.png
Patch0:         %{realname}-%{version}.patch
BuildRequires:  cmake gcc-c++ libtuxcap-devel

%description
Atomic Worm has flown into the light.
A new game which features:
* Simple mouse control
* Exciting challenges and puzzle oriented game-play
* It takes the snake genre to a new dimension.

%prep
%setup -q -n %{realname}_019_src
%patch0
find ./data -type f -exec chmod 644 {} \;
find ./data -type d -exec chmod 755 {} \;

%build
mkdir _build
cd _build
cmake ..
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
install -s -D -m 0755 _build/%{realname} $RPM_BUILD_ROOT%{_bindir}/%{realname}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{realname}
cp -a data/* $RPM_BUILD_ROOT%{_datadir}/%{realname}
cp -a src/*.py $RPM_BUILD_ROOT%{_datadir}/%{realname}
install -D %{S:1} $RPM_BUILD_ROOT/%{_datadir}/applications/%{realname}.desktop
install -D %{S:2} $RPM_BUILD_ROOT/%{_datadir}/pixmaps/%{realname}.png

%files
%defattr(-,root,root)
%doc COPYING README
%{_bindir}/%{realname}
%dir %{_datadir}/%{realname}
%{_datadir}/%{realname}/*
%{_datadir}/applications/%{realname}.desktop
%{_datadir}/pixmaps/%{realname}.png

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Mon May  7 2012 Simon Sun <simon@ossii.com.tw>
- Rebuild for OSSII
* Sat Jul  2 2011 jengelh@medozas.de
- Use %%_smp_mflags for parallel building
- Strip %%clean section (not needed on BS)
* Thu Sep  3 2009 PVince81@yahoo.fr
- Fixed 64-bits compilation issue
* Mon Aug  3 2009 PVince81@yahoo.fr
- Added desktop icon
- Python files are now compiled
* Fri Jul 10 2009 prusnak@suse.cz
- /usr/games, /usr/share/games -> /usr/bin, /usr/share
* Tue May  5 2009 prusnak@suse.cz
- created package (version 0.19)

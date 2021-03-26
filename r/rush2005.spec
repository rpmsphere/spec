%define pkg_name Rush2005

Name:	rush2005
Version:	0.4.12c
Release:	1
Summary:	An American football game.
Group:	Action/Games
License:	BSD
URL:	http://rush2005.sourceforge.net/
Source0:	http://downloads.sourceforge.net/rush2005/%{pkg_name}-0.4.12.tar.bz2
Source1:	%{pkg_name}.png
BuildRequires:	SDL-devel >= 1.2.8, SDL_mixer-devel >= 1.2.6, SDL_image-devel >= 1.2.4
BuildRequires:	desktop-file-utils
Requires:	SDL >= 1.2.8, SDL_mixer >= 1.2.6, SDL_image >= 1.2.4

%description
Rush 2005 is a BSD-licensed project to create an American football game
for Windows and Linux in the tradition of Tecmo Bowl and NFL Blitz,
built using the cross-platform SDL game programming library.

%prep
%setup -q -n %{pkg_name}-%{version}

%build
export LDFLAGS=-Wl,--allow-multiple-definition
cd src
cp /usr/share/automake-*/config.guess .
./configure
ln -sf /usr/share/automake-1.??/depcomp depcomp
make
cd ../

%install
%__rm -rf %{buildroot}
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} << EOF
#!/bin/sh
cd %{_libdir}/%{name}
./rush2005
EOF
%__mkdir_p %{buildroot}%{_libdir}
%__cp -a bin %{buildroot}%{_libdir}/%{name}
%__cp src/rush2005 %{buildroot}%{_libdir}/%{name}/
%__mkdir_p %{buildroot}%{_datadir}/applications
%__mkdir_p %{buildroot}%{_datadir}/pixmaps
cp %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Comment=American football game 2005
Comment[zh_TW]=2005 美式足球大賽
Name=Rush 2005
Name[zh_TW]=2005 美式足球
Type=Application
Exec=%{name}
Icon=%{name}
Categories=Game;StrategyGame;
EOF

%clean
%__rm -rf %{buildroot}

%files
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.4.12c
- Rebuild for Fedora
* Tue Nov 25 2008 Wind <yc.yan@ossii.com.tw> - 0.4.12c-1
-First Build for OSSII.

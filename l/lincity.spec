Name:           lincity
Version:        1.12.1
Release:        1
Summary:        Lincity is a city simulation game
Group:          Amusements/Games
License:        LGPL
URL:            http://lincity.sourceforge.net/
Source0:        http://nchc.dl.sourceforge.net/sourceforge/lincity/lincity-1.12.1.tar.gz
Source1:	lincity.png

BuildRequires:  gettext bison 
BuildRequires:  jam, physfs-devel, zlib-devel, libxml2-devel
BuildRequires:  SDL-devel, SDL_mixer-devel, SDL_image-devel, SDL_gfx-devel
BuildRequires:  SDL_ttf-devel, desktop-file-utils
BuildRequires:  xorg-x11-proto-devel, libX11-devel, mesa-libGL-devel, mesa-libGLU-devel

%description
Lincity is a city simulation game. You are required to build and maintain
a city. You must feed, house, provide jobs and goods for your residents.
You can build a sustainable economy with the help of renewable energy and
recycling, or you can go for broke and build rockets to escape from
a pollution ridden and resource starved planet, it's up to you.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
make 

%install
DESTDIR=$RPM_BUILD_ROOT make install 
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
install -m0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

#Desktop
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF

[Desktop Entry]
Name=%{name}
Name[zh_TW]=模擬林市
Comment=Lincity is a city simulation game
Comment[zh_TW]=Lincity 是一套模擬城市的遊戲
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Game;Simulation;
EOF

%clean

%files
%defattr(-,root,root,0755)
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*
%{_bindir}/*lincity
%{_datadir}/locale/ca/LC_MESSAGES/lincity.mo
%{_datadir}/locale/it/LC_MESSAGES/lincity.mo
%{_datadir}/man/man6/lincity.6.gz

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Mon Oct 20 2008 Feather Mountain <john@ossii.com.tw> 1.12.1.ossii
- Build for OSSII

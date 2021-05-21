Name:           goonies
Version:        1.0
Release:        1
Summary:        This remake was make from the 2004
Group:          Amusements/Games
License:        LGPL
URL:            http://goonies.jorito.net/
Source0:        http://nchc.dl.sourceforge.net/sourceforge/goonies/%{name}_r1-0-1.tgz

BuildRequires:  SDL_sound-devel mesa-libGL-devel alsa-oss-devel

%description
This remake was make from the 2004.

%prep
%setup -q -n %{name}_r1-0-1

%build
cp build/linux/Makefile src
cd src
make 

%install
%__rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m0644 -p graphics/title_logo.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

cp src/%{name} .
rm -rf src
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}/

#Desktop
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF

[Desktop Entry]
Name=%{name}
Name[zh_TW]=七寶奇謀
Comment=This remake was make from the 2004
Comment[zh_TW]=七寶奇謀是 2004 年仿製的遊戲，以擊倒敵人並閃躲敵人，拿取過關道具突破關卡。
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Game;
EOF

#Exec
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
cd %{_datadir}/%{name}
./%{name}
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(0755,root,root,0755)
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Thu Jan 15 2009 Feather Mountain <john@ossii.com.tw> 1.0-1
- Build for OSSII


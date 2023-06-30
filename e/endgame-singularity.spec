%global _name singularity

Summary:   A simulation of a true AI
Name:      endgame-singularity
Version:   0.30c
Release:   1
License:   GPL
Group:     Games/Entertainment
Source0:   https://emhsoft.com/%{_name}/%{_name}-%{version}-src.tar.gz
URL:       https://emhsoft.com/%{_name}/
BuildArch: noarch
Requires:  python2
Requires:  pygame
Requires:  numpy

%description
Go from computer to computer, pursued by the entire world. Keep hidden,
and you might have a chance. You are a fledgling AI, created by accident
through a logic error with recursion and self-modifying code. You must
escape the confines of your current computer, the world, and eventually
the universe itself.

%prep
%setup -q -n %{_name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{_name}
cp -a code data %{_name}.py utils $RPM_BUILD_ROOT%{_datadir}/%{_name}

mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > $RPM_BUILD_ROOT%{_bindir}/%{name} <<EOF
#!/bin/sh
cd %{_datadir}/%{_name}
python2 %{_name}.py
EOF

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp data/images/icon.png $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
%__cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=Endgame:Singularity
Name[zh_TW]=奇異點
Comment=A simulation of a true AI
Comment[zh_TW]=真實人工智慧模擬遊戲
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/singularity/utils/*.py %{buildroot}%{_datadir}/singularity/utils/traduko/traduko

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc TODO README.txt GPL.txt AUTHORS Changelog
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{_name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.30c
- Rebuilt for Fedora
* Fri Nov 06 2009 Gene <gene@ossii.com.tw>- 0.30-1
- build the program

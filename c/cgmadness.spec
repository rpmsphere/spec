%undefine _debugsource_packages

Name:                   cgmadness
Summary:                Based on the classic game Marble Madness
Version:                1.2.2
Release:                1
License:                GPL
Group:                  Amusements/Games/3D/Other
URL:                    https://cgmadness.sourceforge.net/
Source:                 %{name}-%{version}-src.tar.bz2
Source1:                %{name}.png
BuildRequires:  gcc-c++
BuildRequires:  freeglut-devel
BuildRequires:  glew-devel
Requires:       glew
Requires:       freeglut

%description
CG Madness is based on the classic game Marble Madness.
It is running on OpenGL and uses current CG techniques.

Author: Sven Reinck <sreinck@gmx.de>

%prep
%setup -q -n %{name}
# ifneq ($(findstring linux-gnu,$(MACHINE)),) ... won't work
sed -i -e 's|-lm|-lm -lglut -lGL -lGLEW -lGLU|g' -e 's|-Werror||' Makefile
sed -i '27i #include <cstddef>' process/MainProcess.cpp

%build
%__make %{?jobs:-j%{jobs}}

%install
%__rm -rf %{buildroot}
%__install -dm 755 %{buildroot}%{_bindir}
%__install -m 755 %{name} \
        %{buildroot}%{_bindir}
%__install -m 755 convert-cgm \
        %{buildroot}%{_bindir}

# startscript
%__cat > %{name}-wrapper << EOF
#!/bin/sh
if [ ! -d \$HOME/.%{name} ]; then
        mkdir \$HOME/.%{name}
        cd \$HOME/.%{name}
        ln -s %{_datadir}/%{name}/* .
        cd ..
fi

cd \$HOME/.%{name}
%{name}
EOF
%__install -m 755 %{name}-wrapper \
        %{buildroot}%{_bindir}

%__install -dm 755 %{buildroot}%{_datadir}/%{name}/data
%__install -m 644 data/* \
        %{buildroot}%{_datadir}/%{name}/data
%__install -dm 755 %{buildroot}%{_datadir}/%{name}/levels
%__install -m 644 levels/* \
        %{buildroot}%{_datadir}/%{name}/levels

# icon and menu-entry
%__install -dm 755 %{buildroot}%{_datadir}/pixmaps
%__install -m 644 %{SOURCE1} \
        %{buildroot}%{_datadir}/pixmaps

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Comment=Based on the classic game Marble Madness
Comment[zh_TW]=一套經典的彈珠遊戲
Exec=%{name}-wrapper
Icon=%{name}
Name=CG Madness
Name[zh_TW]=瘋狂滾球
Terminal=false
Type=Application
Categories=Game;ActionGame;
EOF

%files
%doc *.txt 
%{_bindir}/%{name}
%{_bindir}/%{name}-wrapper
%{_bindir}/convert-cgm
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/pixmaps/*.png
%{_datadir}/applications/*.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.2.2
- Rebuilt for Fedora
* Wed Jun  8 2011 Chris lin <chris.lin@ossii.com.tw> - 1.2.2.-0.2.ossii
- Add -lGLU
* Wed Dec 31 2008 Feather Mountain <john@ossii.com.tw> - 1.2.2.-0.1.ossii
- Rebuild for M6(OSSII)
* Sun Nov 23 2008 Toni Graffy <toni@links2linux.de> - 1.2.2-0.pm.1
- update to 1.2.2
* Thu Oct 02 2008 Toni Graffy <toni@links2linux.de> - 1.2.1-0.pm.1
- update to 1.2.1
* Sat Dec 15 2007 Toni Graffy <toni@links2linux.de> - 1.2-0.pm.1
- update to 1.2
* Wed Oct 17 2007 Toni Graffy <toni@links2linux.de> - 1.1.3-0.pm.1
- initial release 1.1.3

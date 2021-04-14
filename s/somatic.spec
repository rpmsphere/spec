%undefine _debugsource_packages
Name:           somatic
Version:        20040406
Release:        1
Summary:        Somatic is a software for solving arbitrary polyomino and polycube puzzles, like the soma puzzle.
Group:          Amusements/Games
License:        LGPL
URL:            http://www.moerig.com/somatic/
Source0:        http://www.moerig.com/somatic/somatic-source-20040406.tar.bz2
Source1:	http://www.moerig.com/somatic/somaforms.gif
Patch0:		somatic-Make.Config.patch
Patch1:		somatic-txtsoma.cpp.patch
Patch2:		somatic-sGFX_cube.hpp.patch
Patch3:		somatic-sFOX_mainwin.hpp.patch
Patch4:		somatic-sFOX_piecewin.cpp.patch
Patch5:		somatic-sFOX_mainwin.cpp.patch
BuildRequires:  fox-devel
Requires:	fox

%description
Somatic is a software for solving arbitrary polyomino and polycube puzzles,
like the soma puzzle. The soma puzzle is made from a set of 7 pieces,
each build from 3 or 4 small cubes. With these pieces one can build a bigger
cube made of 3x3x3=27 of the smaller cubes and a lot of other figures. 

%prep
%setup -q -n %{name}
%patch0 -p0
%patch1 -p0
%patch2 -p0
%patch3 -p0
%patch4 -p0
%patch5 -p0

%build
make 

%install
%__rm -rf %{buildroot}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m0644 -p %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png
cp -a * $RPM_BUILD_ROOT%{_datadir}/%{name}

#Desktop
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF

[Desktop Entry]
Name=%{name}
Name[zh_TW]=變型金磚
Comment=Somatic is a software for solving arbitrary polyomino and polycube puzzles, like the soma puzzle.
Comment[zh_TW]=Somatic 是一套益智的遊戲，使用不同的方塊組合來組成多種變化。
Exec=%{name}
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;Game;
EOF

#Exec
mkdir -p $RPM_BUILD_ROOT%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name} <<EOF
cd %{_datadir}/%{name}/bin
./guisomatic
EOF

%clean
%__rm -rf %{buildroot}

%files
%{_bindir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/*
%{_datadir}/pixmaps/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 20040406
- Rebuilt for Fedora
* Wed Feb 4 2009 Feather Mountain <john@ossii.com.tw> 
- Build for OSSII

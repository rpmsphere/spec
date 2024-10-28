%define _appdatadir %{_datadir}/appdata

Name:           glpeces
Summary:        Tangram game using Qt5
License:        GPLv2
Version:        5.2
Release:        16.1
Group:          Games/Puzzles
URL:            https://pecesjocdetangr.sourceforge.net/iniciang.htm
Source0:        https://sourceforge.net/projects/pecesjocdetangr/files/version%205.2%20%28February%2C%202016%29/glpeces-5.2.tar.gz
Source1:        %{name}.desktop
BuildRequires:  cmake
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Script)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  ghostscript-core ImageMagick
BuildRequires:  libappstream-glib
BuildRequires:  desktop-file-utils

%description
PIECES is a program to play the traditional Tangram, game of Chinese origin.
It consists on constructing shapes with some polygonal pieces. Traditionally
the game has seven pieces, but there are also variations with 5,14 pieces
and others.

%files
%doc copying readme changelog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_appdatadir}/%{name}.appdata.xml
%{_datadir}/pixmaps/%{name}.*
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/%{name}
%{_mandir}/man6/glpeces.6.*

%prep
%setup -q
sed -i -e 's|/\$(CURDIR)||' -e 's|share/games|share|' -e 's|/games|/bin|' CMakeLists.txt

%build
%cmake
%cmake_build

%install
%cmake_install
# fixed menu entry
desktop-file-install %{SOURCE1} \
  --dir=%{buildroot}%{_datadir}/applications 
  
# appdata  
mkdir -p %{buildroot}%{_appdatadir}
cp -pr menu/%{name}.appdata.xml \
  %{buildroot}%{_appdatadir}/%{name}.appdata.xml

# icons
for N in 16 32 48 64;
  do
   convert images/glpeces-64x64.png -scale ${N}x${N} $N.png;
   install -D -m 0644 $N.png %{buildroot}%{_datadir}/icons/hicolor/${N}x${N}/apps/%{name}.png
done  

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop
appstream-util validate-relax --nonet %{buildroot}%{_appdatadir}/*.xml

%changelog
* Thu Jun 02 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 5.2
- Rebuilt for Fedora
* Sat May 07 2016 abfonly <abfonly@gmail.com> 5.2-1
- (bf3b177) Fixed BR

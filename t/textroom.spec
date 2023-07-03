%undefine _debugsource_packages

Name:		textroom
Version:	0.8.2
Release:	14.4
License:	GPLv3
URL:		https://code.google.com/p/textroom/
BuildRequires:  libpng-devel
BuildRequires:	qt4-devel 
BuildRequires:	SDL-devel 
BuildRequires:	hunspell-devel 
BuildRequires:	mesa-libGL-devel
BuildRequires:  SDL_mixer-devel
BuildRequires:  curl-devel
BuildRequires:  libxml++-devel
BuildRequires:  xdg-utils
BuildRequires:	gcc-c++
Source:		https://textroom.googlecode.com/files/%name-%version.tar.gz
Patch1:		textroom-0.8.2-fix-libdir.patch
Patch2:		textroom-0.8.2-fix-desktop.patch
Group:		Applications/Editors
Summary:	Full Screen Rich Text Editor For Writers

%description
Open Source Cross Platform Full Screen Rich Text Editor For Writers.

%files
%doc License ReadMe
%_bindir/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/hunspell/tr.aff
%{_datadir}/hunspell/tr.dic
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/sounds/keyany.wav
%{_datadir}/sounds/keyenter.wav
%{_datadir}/%{name}/

%prep
%setup -q
sed -i "s/-lhunspell/`pkg-config -libs hunspell`/" application/application.pro
%ifarch x86_64 aarch64
%patch1 -p1
%endif
%patch2 -p1
chmod 644 License ReadMe
sed -i '1i #include <unistd.h>' library/sxfile/getusername.cpp

%build
qmake-qt4 PREFIX=/usr QMAKE_CXXFLAGS+="-std=c++11"
make

%install
rm -fr $RPM_BUILD_ROOT
make install INSTALL_ROOT=$RPM_BUILD_ROOT
# Remove the uninstall script 
rm -rf $RPM_BUILD_ROOT/%{_bindir}/%{name}-uninstall

%clean
rm -rf $RPM_BUILD_ROOT

%changelog
* Fri Dec 09 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.8.2
- Rebuilt for Fedora
* Sun Jun 26 2011 fwang <fwang> 0.8.2-2.mga2
+ Revision: 114003
- link hunspell 1.3
- rebuild for new hunspell
* Tue Jun 14 2011 mikala <mikala> 0.8.2-1.mga2
+ Revision: 106048
- imported package textroom

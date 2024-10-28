%undefine _debugsource_packages

Summary:        Cuberok audio player
Name:           cuberok
Version:    0.1.0.rev434
Release:    29.4
License:        GPL
Group:          Productivity/Multimedia/Sound/Players
Source:         trunk-%{version}.tar.bz2
Vendor:         Vasiliy Makarov <drmoriarty.0@gmail.com>
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++, pkgconfig, pkgconfig(QtGui), pkgconfig(QtWebKit), taglib-devel, phonon-devel, gstreamer1-plugins-base-devel
#BuildRequires:  yajl-devel <= 1.0.7
Requires:       cuberok_engine >= %version 

%description
Cuberok is yet another audio player based on Qt4.
It has lightweight interface, music collection support and many features, e.g. music autorating and Last.FM scrobbler.

%prep
%setup -q -n trunk-%{version}
# hack
sed -i 's/X-SuSE-translate-true//' %{name}.desktop
sed -i 's|CUBEROK_PLUGINS|"%{_libdir}/%{name}"|' src/*.cpp

%build
qmake-qt4 CONFIG+=player_phonon CONFIG+=disable_ffmpeg Cuberok.pro
make 

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} INSTALL_ROOT=$RPM_BUILD_ROOT/usr
mkdir -p %{buildroot}%{_libdir}/%{name}

%files
%doc ChangeLog README license.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}
%{_libdir}/%{name}

%changelog
* Sun Mar 19 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0.rev434
- Rebuilt for Fedora
* Sat Feb 05 2011 Petr Vanek <petr@scribus.info> - 0.1.0
- suse fixes
* Fri Jan 07 2011 TI_Eugene <ti.eugene@gmail.com>
- 0.1.0
* Tue May 19 2009 TI_Eugene <ti.eugene@gmail.com>
- Initial release for OBS
* Fri Apr 10 2009 Vasiliy Makarov <drmoriarty.0@gmail.com>
- First release for openSuse

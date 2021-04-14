%undefine _debugsource_packages

Summary:	Cuberok audio player
Name:		cuberok
Version:    0.1.0.rev434
Release:    29.4
License:	GPL
Group:		Productivity/Multimedia/Sound/Players
Source:		trunk-%{version}.tar.bz2
Vendor:		Vasiliy Makarov <drmoriarty.0@gmail.com>
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++, pkgconfig, pkgconfig(QtGui), pkgconfig(QtWebKit), taglib-devel, phonon-devel, pkgconfig(gstreamer-plugins-base-0.10) 
#BuildRequires:  yajl-devel <= 1.0.7
Requires:	cuberok_engine >= %version 

%description
Cuberok is yet another audio player based on Qt4.
It has lightweight interface, music collection support and many features, e.g. music autorating and Last.FM scrobbler.

%package gstreamer
Summary:	GStreamer Output Plugin for cuberok
Group:		Productivity/Multimedia/Sound/Players
Requires:	cuberok = %version
Provides:	cuberok_engine = %version

%description gstreamer
cuberok media player can play via GStreamer using this plugin.

%package phonon
Summary:	Phonon Output Plugin for cuberok
Group:		Productivity/Multimedia/Sound/Players
Requires:	cuberok = %version
Provides:	cuberok_engine = %version

%description phonon
cuberok media player can play via GStreamer using this plugin.

%prep
%setup -q -n trunk-%{version}
# hack
sed -i 's/X-SuSE-translate-true//' %{name}.desktop

%build
qmake-qt4 CONFIG+=player_phonon CONFIG+=disable_ffmpeg Cuberok.pro
make 

%install
rm -rf $RPM_BUILD_ROOT
%{makeinstall} INSTALL_ROOT=$RPM_BUILD_ROOT/usr

%clean
%__rm -rf $RPM_BUILD_ROOT

%post

%postun

%files
%doc ChangeLog README license.txt
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.xpm
%{_datadir}/%{name}

%files gstreamer
%{_libdir}/%{name}

%files phonon  
%{_libdir}/%{name}

%changelog
* Wed May 09 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.0.rev434
- Rebuilt for Fedora
* Sat Feb 05 2011 Petr Vanek <petr@scribus.info> - 0.1.0
- suse fixes
* Fri Jan 07 2011 TI_Eugene <ti.eugene@gmail.com>
- 0.1.0
* Tue May 19 2009 TI_Eugene <ti.eugene@gmail.com>
- Initial release for OBS
* Fri Apr 10 2009 Vasiliy Makarov <drmoriarty.0@gmail.com>
- First release for openSuse

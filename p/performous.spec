Name:	        performous	
Version:	0.6.1
Release:	1
Summary:	A free cross-platform singing game
Group:		Amusements/Games
License:	GPL
URL:		http://performous.org/
Source0:	http://sourceforge.net/projects/performous/files/performous/Performous-%{version}-Source.tar.bz2
Source1:	%{name}-0.5.1.zh_TW.po
BuildRequires:	cmake, glibmm24-devel, ImageMagick-c++-devel, glew-devel, librsvg2-devel, libxml++-devel, ffmpeg-devel, boost-devel
BuildRequires:  mesa-libGL-devel, SDL-devel, alsa-lib-devel, cairo-devel, pango-devel, libpng-devel, gettext

%description
While Performous might be classified as a karaoke program, it is actually much
more than that. Instead of just displaying the lyrics, notes are also displayed
and the performance is scored based on how well you actually hit the notes.

%prep
%setup -q -n Performous-%{version}-Source
echo -e 'Name[zh_TW]=歡唱\nComment[zh_TW]=Performous 卡拉OK' >> data/%{name}.desktop
cp %{SOURCE1} lang/zh_TW.po

%build
mkdir build
cd build
cmake .. -DCMAKE_INSTALL_PREFIX=/usr -DSHARE_INSTALL=share/performous
make

%install
rm -rf $RPM_BUILD_ROOT
cd build
make DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc docs/*
%{_bindir}/*
##%{_libdir}/%{name}
%{_datadir}/pixmaps/*
%{_datadir}/applications/*.desktop
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%{_datadir}/%{name}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Fri Dec 17 2010 Wei-Lun Chao <bluebat@member.fsf.org> - 0.6.1-1.ossii
- Update to 0.6.1

* Tue Sep 1 2009 Harry Chen <harry@server1.ossii.com.tw> - 0.3.2-1.ossii
- Build for ossii

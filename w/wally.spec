%undefine _debugsource_packages
%define tarballdir build

Name:           wally
Version:        2.4.1
Release:        1
Summary:        wallpaper changer using files, folders, FTP and web sites
Group:          Amusements/Graphics
License:        GPLv2 
URL:            http://www.becrux.com/index.php?page=projects&name=wally
Source0:        http://www.becrux.com/pages/projects/wally/wally-2.4.1.tar.gz
Source1:	wally.desktop
BuildRequires:  qt4-devel libexif-devel cmake gcc gcc-c++ desktop-file-utils

%description
Wally is a Qt4 wallpaper changer, using multiple sources like files, folders, 
FTP remote folders, Flickr, Yahoo!, Panoramio, Pikeo, Ipernity, Photobucket, 
Buzznet, Picasa, Smugmug and Bing images. Now it's available in many 
languages!!

%prep
%setup -q
sed -i '44,50d' wallyplugin/wallyplugin.cpp

%build
mkdir -p %{tarballdir}
cd %{tarballdir}
export LDFLAGS=-lX11
cmake -DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release ..
make


%install
rm -rf $RPM_BUILD_ROOT
cd %{tarballdir}
mkdir -p %buildroot
make DESTDIR=%buildroot install
cd ..
echo `pwd`
mkdir -p %{buildroot}%{_datadir}/applications
desktop-file-install --vendor="" \
	--dir=%{buildroot}%{_datadir}/applications/   \
	--add-category Utility \
	%{SOURCE1}
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps
%{__cp} res/images/wally.png \
        $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/wally.png

%post
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-desktop-database &> /dev/null || :

%postun
touch --no-create %{_datadir}/icons/hicolor
if [ -x %{_bindir}/gtk-update-icon-cache ]; then
  %{_bindir}/gtk-update-icon-cache -q %{_datadir}/icons/hicolor;
fi
update-desktop-database &> /dev/null || :

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS ChangeLog COPYING DISCLAIMER INSTALL LICENSE NEWS README README.shortcuts README.XFCE4 TODO
%{_bindir}/%{name}
%{_datadir}/applications/wally.desktop
%{_datadir}/icons/hicolor/32x32/apps/wally.png
%if %((kde4-config --kde-version 2>/dev/null || echo 0) | cut -c1) > 0
%{_libdir}/kde4/*
%{_datadir}/icons/oxygen/16x16/apps/*
%{_datadir}/kde4/services/*
%endif

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 2.4.1
- Rebuilt for Fedora
* Sat Oct 23 2010 - Sandrine Soudant <sandrine.soudant at gmail.com> - 2.4.1-1
 - Build RPM package for Wally 2.4.1	
* Sat Aug 28 2010 - Sandrine Soudant <sandrine.soudant at gmail.com> - 2.4.0-1
 - Build RPM package for Wally 2.4.0
* Fri Aug 13 2010 - Sandrine Soudant <sandrine.soudant at gmail.com> - 2.3.2-1
 - Initial version for Fedora RPM

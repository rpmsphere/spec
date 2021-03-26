Summary:       My Media System is a multimedia center for GNU/LInux
Name:          mms
Version:       1.1.0
Release:       2287
License:       GPL
Group:         Applications/Multimedia
URL:           http://mymediasystem.org/
Source0: http://mms.mymediasystem.net/mms110/nightly-snapshot/%{name}-%{version}-2287.tgz
Source1:       mms.png
Source2:       mms.xsession
Source3:       mms-1.1.0.zh_TW.po.zip
BuildRequires: SDL-devel
BuildRequires: commoncpp2-devel
BuildRequires: gcc-c++
BuildRequires: gettext-devel
BuildRequires: imlib2-devel
BuildRequires: libtool
BuildRequires: libxml2-devel
BuildRequires: ncurses-devel
BuildRequires: pcre-devel
BuildRequires: pkgconfig
BuildRequires: sed
BuildRequires: taglib-devel
BuildRequires: zlib-devel
BuildRequires:  imlib2-devel
BuildRequires:  sqlite-devel
BuildRequires:  xine-lib-devel
BuildRequires:  em8300-devel
BuildRequires:  lirc-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  mesa-libGLU-devel
BuildRequires:  svgalib-devel
BuildRequires:  pcre-devel
BuildRequires:  libXScrnSaver-devel
BuildRequires:  ffmpeg-devel
BuildRequires:  python-devel
BuildRequires:  gstreamer-devel
BuildRequires:  inotify-tools-devel
BuildRequires:  boost-devel
BuildRequires:  sqlite-devel

Requires:       mplayer
#Recommends:    W32codecs

%description
My Media System is an application that manages, displays and plays media content
such as videos, music, pictures, and more. MMS runs perfectly on anything from
a Set-Top-Box connected to your TV-Set, to your specially tailored multimedia PC
and HD display.

%prep
%setup -q -n %{name}-%{version}-2287
unzip -q %{SOURCE3}
sed -i -e 's|cc_verc_fail=yes|cc_verc_fail=no|' -e 's/2\.4/2.7/' -e 's/LANGUAGES =/LANGUAGES = zh_TW/' configure

%build
./configure --prefix=%{_prefix} \
	--enable-game \
	--enable-tv \
	--enable-lirc \
        --enable-evdev \
	--enable-dvb \
        --enable-opengl \
        --enable-dxr3 \
        --enable-mpeg \
        --enable-gst-audio \
        --enable-python \
        --enable-clock \
        --enable-notify-area \
        --enable-weather \
        --enable-lcd
        #--enable-bttv-radio
	#--enable-eject-tray
sed -i 's/-D_GNU_SOURCE/-D_GNU_SOURCE -D__STDC_CONSTANT_MACROS/' config.mak
%{__make}
#%{__make} library-builders

%install
%{__rm} -fr %{buildroot}
%{__make} DESTDIR=%{buildroot} install
#%{__make} DESTDIR=%{buildroot} library-builders-install

%{__install} -D -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/%{name}.png
%{__install} -D -m 0644 %{SOURCE2} %{buildroot}%{_datadir}/xsessions/mms.desktop

#Desktop
%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Name[zh_TW]=我的影音中心
Comment=My Media System is a multimedia center
Comment[zh_TW]=My Media System 是一套影音播放中心
Exec=%{name}.sh
Terminal=false
Type=Application
Icon=%{name}
Encoding=UTF-8
Categories=Application;AudioVideo;Video;MultiMedia;
EOF

#Exec
%__mkdir_p %{buildroot}%{_bindir}
%__cat > %{buildroot}%{_bindir}/%{name}.sh <<EOF
#!/bin/bash
mms -u \`%{__id_u}n\` -i keyboard -o opengl;
EOF

perl -pi -e 's,fullscreen\ \=\ /media/,input\ \=\ keyboard,g' %{buildroot}%{_sysconfdir}/mms/config*

#sed -i -f - %{buildroot}%{_sysconfdir}/mms/config* <<EOF
#s/^input = lirc/input = keyboard/
#s/^fullscreen = false/fullscreen = true/
#EOF

ln -sf /usr/share/fonts/opendesktop/TrueType/odokai.ttf %{buildroot}%{_datadir}/mms/fonts/Vera.ttf

%clean
%{__rm} -fr %{buildroot}

%files
%defattr(0755, root, root, 0755)
%doc doc/LICENSE doc/README
#%config(noreplace) %{_sysconfdir}/mms/config
#%config %{_sysconfdir}/mms/config.orig
#%config(noreplace) %{_sysconfdir}/mms/input-keyboard
#%config(noreplace) %{_sysconfdir}/mms/input-lirc
#%config(noreplace) %{_sysconfdir}/mms/lirc.conf
%{_sysconfdir}/*
%{_libdir}/mms
%{_libdir}/python2.?/site-packages/*
%{_bindir}/*
%{_datadir}/mms
%lang(de) %{_mandir}/de/man1/mms*.1.gz
%{_mandir}/man1/mms*.1.gz
%{_datadir}/applications/mms.desktop
#%attr(0777,root,root) %{_localstatedir}/cache/%{name}
#%attr(0777,root,root) %{_localstatedir}/lib/%{name}
%{_datadir}/xsessions/mms.desktop
%{_datadir}/pixmaps/mms.png
%{_datadir}/locale/*/LC_MESSAGES/*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Thu Jun 09 2011 Wei-Lun Chao <bluebat@member.fsf.org> 1.1.0-2287.ossii
- Add zh_TW locale
- Update to 1.1.0-2287

* Fri Dec 26 2008 Feather Mountain <john@ossii.com.tw> 1.1.0-0.9.ossii
- Rebuild for FC10
- Add mms.sh

* Sat Aug 16 2008 Funda Wang <fundawang@mandriva.org> 1.1.0-0.rc8.1mdv2009.0
+ Revision: 272524
- New version 1.1.0 rc8

* Sun Aug 10 2008 Funda Wang <fundawang@mandriva.org> 1.1.0-0.rc7.1mdv2009.0
+ Revision: 270149
- fix file list
- drop option
- New version rc7
- rebuild for new directfb

  + Pixel <pixel@mandriva.com>
    - adapt to %%_localstatedir now being /var instead of /var/lib (#22312)

* Thu Apr 17 2008 Anssi Hannula <anssi@mandriva.org> 1.1.0-0.rc5.1mdv2009.0
+ Revision: 195243
- new version

  + Thierry Vignaud <tvignaud@mandriva.com>
    - fix gstreamer0.10-devel BR for x86_64

* Thu Jan 03 2008 Anssi Hannula <anssi@mandriva.org> 1.1.0-0.rc1.2mdv2008.1
+ Revision: 141688
- disable vgagl output
- do not ship midentify, it is shipped with mplayer
- 1.1.0-rc1
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Sep 07 2007 Anssi Hannula <anssi@mandriva.org> 1.0.8.5-1mdv2008.0
+ Revision: 81921
- 1.0.8.5
- change some requires to suggests and add mplayer as such

* Thu Jul 19 2007 Anssi Hannula <anssi@mandriva.org> 1.0.8.4-1mdv2008.0
+ Revision: 53643
- allow build with gcc4.2 (patch1)
- 1.0.8.4
- add URL (Colin Guthrie)

* Sun Jun 03 2007 Anssi Hannula <anssi@mandriva.org> 1.0.8.3-2mdv2008.0
+ Revision: 34970
- initial Mandriva release

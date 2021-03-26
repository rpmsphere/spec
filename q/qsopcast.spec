Name:           qsopcast
Version:        0.3.5
Release:        1
Summary:        QT GUI front-end of sopcast
URL:		http://code.google.com/p/qsopcast/
License:        GPL
Group:          Networking/Other
Source0:        http://qsopcast.googlecode.com/files/%name-%version.tar.bz2
Source1:	%name-icons.tar.bz2
Patch0:		qmake_lsb.patch
Patch1:		translation.patch
Patch2:		channel.diff
Patch3:		cpp43.patch
BuildRequires:	qt3-devel alsa-lib-devel pkgconfig desktop-file-utils

%description
qsopcast is a QT GUI front-end of the Linux command line executive of P2P TV sopcast.

%prep
%setup -q
tar -C src -xjf %{SOURCE1}
%patch0 -p 0
%patch1 -p 0
%patch2 -p 0
%patch3 -p 1
sed -i '1i #include <unistd.h>' src/loadsave.cpp src/record.cpp src/sopfork.cpp src/sound.cpp

%build
cd src
%ifarch x86_64 aarch64
/usr/lib64/qt-3.3/bin/qmake
%else
/usr/lib/qt-3.3/bin/qmake
%endif
lrelease-qt4 %name.pro
make

%install
%__rm -rf $RPM_BUILD_ROOT
export BINDIR=%_bindir
export DATADIR=%_datadir
make -C src install INSTALL_ROOT=$RPM_BUILD_ROOT

# desktop file
%__mkdir_p $RPM_BUILD_ROOT%_datadir/applications
cat > $RPM_BUILD_ROOT%_datadir/applications/%name.desktop << EOF
[Desktop Entry]
Name=qsopcast
Name[zh_CN]=网络电视
Name[zh_TW]=網路電視
Comment[zh_CN]=P2P的网络电视
Comment[zh_TW]=QSopcast 點對點網路電視圖形介面
Comment=P2P Online TV SOPCast
Exec=qsopcast
Icon=qsopcast
Terminal=false
Type=Application
StartupNotify=true
Categories=Qt;AudioVideo;Network;
EOF

desktop-file-install --vendor ""\
 --dir $RPM_BUILD_ROOT%_datadir/applications\
 $RPM_BUILD_ROOT%_datadir/applications/%name.desktop

%post
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%postun
%{_bindir}/gtk-update-icon-cache --quiet %{_datadir}/icons/hicolor || :

%clean
%__rm -rf $RPM_BUILD_ROOT

%files
%doc AUTHORS COPYING README TODO
%_bindir/qsopcast
%_datadir/icons/mozart.xpm
%_datadir/icons/hicolor/*/apps/%name.png
%_datadir/apps/qsopcast/*.qm
%_datadir/applications/%name.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.5
- Rebuild for Fedora
* Wed Aug 20 2008 Stumpy842 <stump842@gmail.com> 0.3.5-1pclos2007
- Import for PCLOS

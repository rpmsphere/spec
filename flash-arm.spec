Summary: Adobe Flash Player and Plugin for ARM
Name: flash-arm
Version: 10.1.60.66
Release: 1%{?dist}.bin
License: Adobe End User License Agreement
Group: Applications/Multimedia
Source0: %{name}-%{version}.tar.gz
Source1: flashplayer.png
URL: http://labs.adobe.com/technologies/flashplayer10/
BuildRoot: %{_tmppath}/%{name}-%{version}-root
ExclusiveArch: %arm
Provides: flashplayer, flash-plugin

%description
Release version of the standalone player (flashplayer).
Adobe(R) Flash(R) Player. Copyright (C) 1996 - 2009
Adobe Systems Incorporated. All Rights Reserved.

%prep
%setup -q

%build
%install
rm -rf %{buildroot}
install -D -m 755 bin/flashplayer %{buildroot}%{_bindir}/flashplayer
install -d %{buildroot}%{_libdir}/flash-plugin
install -m 755 lib/lib* %{buildroot}%{_libdir}
install -m 755 plugins/libflashplayer.so %{buildroot}%{_libdir}/flash-plugin/libflashplayer.so
#chrpath -d %{buildroot}%{_libdir}/flash-plugin/libflashplayer.so
install -d %{buildroot}%{_libdir}/mozilla/plugins
ln -sf ../../flash-plugin/libflashplayer.so %{buildroot}%{_libdir}/mozilla/plugins/libflashplayer.so
install -D -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/flashplayer.png

%__mkdir_p %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/flashplayer.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=FlashPlayer
Name[zh_TW]=閃圖播放器
Comment=Adobe Standalone Flash Player
Comment[zh_TW]=Adobe 的獨立閃圖播放程式
Exec=flashplayer
Terminal=false
Type=Application
Icon=flashplayer
Categories=Application;AudioVideo;
MimeType=application/x-shockwave-flash;
EOF

%clean
rm -rf %{buildroot}

%post 
update-desktop-database &> /dev/null || :

%postun
update-desktop-database &> /dev/null || :

%files
%defattr(-,root,root)
%{_bindir}/flashplayer
%{_libdir}/lib*
%{_datadir}/applications/flashplayer.desktop
%{_datadir}/pixmaps/flashplayer.png
%{_libdir}/flash-plugin/libflashplayer.so
%{_libdir}/mozilla/plugins/libflashplayer.so

%changelog
* Fri Dec 31 2010 Wei-Lun Chao <bluebat@member.fsf.org> - 10.1.60.66
- Initial package for OSSII

%undefine _debugsource_packages

Name:           plexydesk
URL:            https://www.plexyplanet.org/
BuildRequires:  cmake qt-devel qtwebkit-devel 
License:        LGPL v3
Group:          System/GUI/Other 
Version:        0.5.21
Release:        37.1
Summary:        Efficiently use your desktop background
Source:         %{name}-%{version}-28-gcf3840e.tar.gz
BuildRequires: libXcomposite-devel
BuildRequires: libXext-devel
BuildRequires: qtwebkit-devel

%description
PlexyDesk is a modular Desktop extension fully powered by Nokia Qt Framework.
PlexyDesk lets you customize your Desktop with QML and it's C++ API.
Apart from this, PlexyDesk also lets you make theme packs (Skins) for your
desktop using QML and share it with everyone.
 
PlexyDesk Currently supports the following features:
- Change your desktop wallpaper by dragging and dropping any image you like from your file manager 
- Fully supports Qt QML 
- Provides support for Qt/3D
- PlexyDesk widgets can be programmed with shader programs (GLSL). 
- API for writing data models, and C++ widget plugins 
- Dbus api for changing the wallpaper on Linux
- Various Utility widgets (like a Clock, File browser, and Photo Frame).

%prep
%setup -q -n siraj-%{name}-cf3840e
#sed -i 's| /usr| ${CMAKE_INSTALL_PREFIX}|' extensions/widgets/cpu/cpu/CMakeLists.txt

%build
#cmake -DCMAKE_INSTALL_PREFIX=%{buildroot}/usr .
export CXXFLAGS+=" -lX11 -lXext"
cmake -DCMAKE_INSTALL_PREFIX=/usr .
make

%install
%make_install
install -m755 plexylib/fbjson/libplexyjson.so %{buildroot}/usr/lib/libplexyjson.so
sed -i 's|%{buildroot}||' %{buildroot}%{_datadir}/dbus-1/services/*
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc AUTHORS COPYING TODO
%{_libdir}/libplexymime.so
%{_bindir}/plexy_icon_test
%{_bindir}/plexy_json_test
%{_bindir}/plexydesk
%{_bindir}/plexymimetest
%{_bindir}/plexypanel
%{_bindir}/socialplexyaccountman
%{_bindir}/socialplexydaemon
%{_libdir}/libmimetype.so
%{_libdir}/libplexydeskcore.so
%{_libdir}/libplexymagic.so
%{_libdir}/libwebqgv.so
%{_libdir}/libplexyjson.so
%{_libdir}/plexyext
#{_libdir}/qt4/imports/
%{_libdir}/qt4/imports/FolderView/
#{_libdir}/qt4/imports/FolderView/libfolderview.so
#{_libdir}/qt4/imports/FolderView/qmldir
/usr/share/dbus-1/services/org.plexydesk.SocialAccountsManager.service
/usr/share/dbus-1/services/org.plexydesk.social.service
%{_datadir}/plexy
%exclude /usr/theme
%exclude /usr/ext
%exclude /usr/mime

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.21
- Rebuilt for Fedora
* Wed Aug 10 2011 giacomosrv@gmail.com
- packaged plexydesk version 0.5.21

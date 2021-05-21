Name: owb
Version: 0
Release: r241

Summary: an open-source web browser for Consumers Electronic devices
License: BSD/LGPL/APSL
Group: Networking/WWW

URL: http://www.sand-labs.org/owb
Source0: http://www.sand-labs.org/downloads/sources/owb-trunk.r241.tar.bz2
Source1: owb.desktop
Source2: owb.png

BuildRequires: cmake chrpath esound flex gcc-c++ gperf libcurl-devel freetype-devel libicu-devel SDL-devel SDL_gfx-devel libxslt-devel
BuildRequires: bitstream-vera-fonts-common

# fonts: currently owb requires default font in fixed
# location; seems easier to provide at build time
%define owb_ttf /usr/share/fonts/bitstream-vera/Vera.ttf

%define owb_dir %_libdir/%name
%define owb_libs libbal.so libjscore.so libwebcore-owb.so

%description
OWB (Origyn Web Browser) is a WebKit (KHTML/KJS) based browser
for embedded devices; this build targets Linux/SDL/X11.

The desktop version is beta quality, don't expect too much
from it [yet].

%prep
%setup -q -n owb_trunk.r241
sed -i '1i #include <cstdio>' JavaScriptCore/bindings/bal/bal_instance.cpp BAL/Tests/TestHelpers/BitmapWriter.cpp
sed -i '1i #include <unistd.h>' JavaScriptCore/kjs/interpreter.cpp BAL/Implementations/Events/SDL/BCEventLoopSDL.cpp
sed -i '1i #include <cstdio>\n#include <cstring>' BAL/Implementations/Facilities/Generic/BTDeviceChannel.cpp BAL/Implementations/Facilities/Generic/BTLogManager.cpp BAL/Implementations/Facilities/Generic/BTTextLogFormatter.cpp
sed -i '1i #include <ctype.h>' BAL/Implementations/Internationalization/ICU/BCInternationalizationICU.cpp
sed -i '1i #include <cstdlib>\n#include <cstring>' BAL/Tests/TestManager/TestManager.cpp BAL/Tests/TestManager/TestRunner.cpp
sed -i '1i #include <cstdio>' BAL/Tests/TestHelpers/FileHelper.cpp BAL/Tests/FacilitiesTests/LogManagerTestInteractif.cpp
sed -i '1i #include <cstring>' BAL/Tests/FacilitiesTests/LogManagerTestInteractif.cpp

%build
cmake . -Wno-dev
make owb
chrpath -k -r %owb_dir %owb_libs %name ||:

%install
rm -rf %{buildroot}
install -d  -m755 %buildroot%owb_dir/
install -p  -m644 %owb_libs %buildroot%owb_dir/
install -pD -m755 %name %buildroot%_bindir/%name
##install -pD -m644 %owb_ttf %buildroot%_datadir/fonts/owb.ttf
install -pD -m644 %SOURCE1 %buildroot%{_datadir}/applications/%name.desktop
install -pD -m644 %SOURCE2 %buildroot%{_datadir}/pixmaps/%name.png

%files
%_bindir/%name
%owb_dir/
##%_datadir/fonts/owb.ttf
%{_datadir}/pixmaps/owb.png
%{_datadir}/applications/%name.desktop
%doc README 

%clean
rm -rf %{buildroot}

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuilt for Fedora
* Tue Sep 22 2009 Wei-Lun Chao <bluebat@member.fsf.org> 0-r241.ossii
- Rebuild for OSSII

* Sun Nov 11 2007 Michael Shigorin <mike@altlinux.org> 0-alt1.20070720
- build only browser, we don't need [mislinked] tests
- refined spec, result should at least be usable now
- replaced Vera with DejaVu for better Unicode support
  (thanks vsu@ for a hint that led to particular choice)

* Tue Oct 09 2007 Michael Shigorin <mike@altlinux.org> 0-alt1.20070720
- built for ALT Linux

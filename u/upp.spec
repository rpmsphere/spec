%undefine _debugsource_packages
%global __os_install_post %{nil}

Name:           upp
Version:        17024
Release:        1
License:        BSD
Summary:        C++ cross-platform rapid application development framework (known as U++)
URL:            https://www.ultimatepp.org
Group:          Development/Languages/C and C++
Source0:        https://downloads.sourceforge.net/project/upp/upp/%{version}/upp-posix-%{version}.tar.xz
BuildRequires:  libpng-devel
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  desktop-file-utils
BuildRequires:  libX11-devel
BuildRequires:  libXdmcp-devel
BuildRequires:  notification-daemon, sane-backends-libs
BuildRequires:  bzip2-devel, expat-devel, cairo-devel
Requires:       gcc-c++
Requires:       theide

%description
Ultimate++ is a radical and innovative GUI toolkit whose number one priority
is programmer productivity. C++ is a great programming language but
C++ programmers are sometimes hampered by the lack of effective libraries.
U++ libraries enable genuine productivity gains with shorter development
times and greatly reduced application source code size.

%package -n theide
Summary:        Modern IDE designed for developping large U++/C++ applications
Group:          Development/Tools/IDE
Requires:       %{name} = %{version}

%description -n theide
TheIDE introduces modular concepts to C++ programming. It features
BLITZ-build technology to speedup C++ rebuilds up to 4 times, Visual
designers for U++ libraries, Topic++ system for documenting code
and creating rich text resources for applications (like help and code
documentation) and Assist++ - a powerful C++ code analyzer that provides
features like code completion, navigation and transformation.

%prep
%setup -q -n %{name}
#sed -i 's|IsPicked() const|IsPicked()      |' uppsrc/Core/BiCont.h
#sed -i 's|inline UPP::int64  abs|inline UPP::int64  fabs|' uppsrc/Core/Core.h
#sed -i 's|inline double abs|inline double myabs|' uppsrc/Core/Core.h

%build
./configure
#export CFLAGS="%{optflags}"
#export CXXFLAGS="%{optflags}"
#export LDFLAGS="%{optflags}"
make -j 4
#make \
#     -e LIBPATH=$(pkg-config --libs-only-L x11 freetype2 gtk+-2.0 glib-2.0 cairo pango atk) \
#     -e CINC=" -I. $(pkg-config --cflags x11 freetype2 gtk+-2.0 glib-2.0 cairo pango atk)" \
#     -e UPPOUT="$PWD/uppsrc" \
#     -e LINKOPTIONS="$(pkg-config --libs libpng freetype2) "
#     -e OutFile="$PWD/uppsrc/ide.out"
make -f umkMakefile -j 4

%install
# put bin file in the right place
install -Dm 755 theide $RPM_BUILD_ROOT/%{_bindir}/theide
# put manual in the right place
install -Dm 644 uppsrc/ide/theide.1 $RPM_BUILD_ROOT/%{_mandir}/man1/theide.1
# install desktop file and icons
install -Dm 644 uppsrc/ide/theide-48.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/theide.png
install -Dm 644 uppsrc/ide/theide-48.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/theide.png
install -Dm 644 uppsrc/ide/theide.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/theide.desktop
# install other stuff like tutorial, reference, source, etc
install -dm 755 $RPM_BUILD_ROOT/%{_datadir}/upp
install -m755 umk $RPM_BUILD_ROOT/%{_bindir}/umk
cp -r examples $RPM_BUILD_ROOT/%{_datadir}/upp
cp -r reference $RPM_BUILD_ROOT/%{_datadir}/upp
cp -r tutorial $RPM_BUILD_ROOT/%{_datadir}/upp
cp -r uppsrc $RPM_BUILD_ROOT/%{_datadir}/upp

# We create our own GCC.bm
INCLUDEDIR=$( pkg-config --cflags x11 freetype2 gtk+-2.0 glib-2.0 cairo pango atk | awk ' { gsub ( / /, "" ) ; gsub ( /-I/, ";" ) ; sub ( /;/, "" ) ; sub ( /-pthread/, "" ) ; print $0 }' )  
LIBDIR=$( pkg-config --libs-only-L x11 freetype2 gtk+-2.0 glib-2.0 cairo pango atk | awk ' { gsub ( / /, "" ) ; gsub ( /-I/, ";" ) ; sub ( /;/, "" ) ; print $0 }' )

cat > $RPM_BUILD_ROOT/%{_datadir}/upp/GCC.bm << EOF
BUILDER         = "GCC";
COMPILER        = "g++";
DEBUG_INFO      = "2";
DEBUG_BLITZ     = "1";
DEBUG_LINKMODE  = "1";
DEBUG_OPTIONS   = "-O0";
DEBUG_FLAGS     = "";
RELEASE_BLITZ           = "0";
RELEASE_LINKMODE        = "1";
RELEASE_OPTIONS         = "-O3 -ffunction-sections -fdata-sections";
RELEASE_SIZE_OPTIONS    = "-Os -finline-limit=20 -ffunction-sections -fdata-sections";
RELEASE_FLAGS   = "";
RELEASE_LINK    = "-Wl,--gc-sections";
DEBUGGER        = "gdb";
PATH            = "";
INCLUDE = "$INCLUDEDIR";
LIB     = "$LIBDIR";
REMOTE_HOST     = "";
REMOTE_OS       = "";
REMOTE_TRANSFER = "";
REMOTE_MAP      = "";
LINKMODE_LOCK   = "0";
EOF
chmod 644 $RPM_BUILD_ROOT/%{_datadir}/upp/GCC.bm
# set /lib → /lib64 for x86_64 in GCC.bm
%ifarch x86_64
sed "/INCLUDE/s#/lib/#/lib64/#g" -i $RPM_BUILD_ROOT/%{_datadir}/upp/GCC.bm
%endif

# fix wrong file encoding
sed -i 's/\r//' uppsrc/ide/Copying

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc uppsrc/ide/Copying
%{_bindir}/umk
%{_datadir}/upp

%files -n theide
%doc uppsrc/ide/Copying
%{_bindir}/theide
%{_datadir}/applications/theide.desktop
%{_datadir}/icons/hicolor/48x48/apps/theide.png
%{_datadir}/pixmaps/theide.png
%{_mandir}/man1/theide.1*

%changelog
* Sun Nov 12 2023 Wei-Lun Chao <bluebat@member.fsf.org> - 17024
- Rebuilt for Fedora
* Thu Dec 30 2010 fisiu@opensuse.org
- fixed %%{libdir} in external Makefile and GCC.bm
* Wed Nov 17 2010 fisiu@opensuse.org
- initial package

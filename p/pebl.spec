%global __os_install_post %{nil}
%undefine _debugsource_packages

Name: pebl
Summary: Psychology Experiment Building Language
Version: 2.1git
Release: 1
Group: Development/Language
License: GPLv2
URL: https://pebl.sourceforge.net/
#Source0: https://sourceforge.net/projects/pebl/files/%{name}/%{version}/%{name}_%{version}_src.tar.gz
Source0: pebl-code-0-r1469-trunk.zip
BuildRequires: SDL-devel
BuildRequires: SDL_image-devel
BuildRequires: SDL_ttf-devel
BuildRequires: SDL_net-devel
BuildRequires: SDL_gfx-devel
BuildRequires: waave-devel
BuildRequires: libpng12-devel
BuildRequires: compat-ffmpeg-devel

%description
PEBL programming language is:
* Free psychology software for creating experiments
* Allows you to design your own experiments or use ready-made ones
* Lets you exchange experiments freely without license or charge

%prep
%setup -q -n pebl-code-0-r1469-trunk
sed -i -e 's|/usr/local|/usr|g' -e '/PEBLLaunch-log.txt/,/makelinks-mac.sh/d' Makefile
sed -i -e 's|USE_AUDIOIN=1|USE_AUDIOIN = |' -e 's|USE_DEBUG = 1|USE_DEBUG = |' Makefile
sed -i -e 's| -lSDLmain||g' -e 's| -lefence||g' -e 's|-lpng|-lpng12|g' Makefile
sed -i -e 's|-I/usr/include |-I/usr/include -I/usr/include/compat-ffmpeg28 |' -e 's|-L/usr/lib |-L%{_libdir} -L%{_libdir}/compat-ffmpeg28 -lavcodec -lavdevice -lavfilter -lavformat -lavutil -lpostproc -lswscale |' Makefile
sed -i 's|png\.h|libpng12/png.h|' src/utility/PEBLUtility.cpp src/platforms/sdl/SDLUtility.cpp
%ifarch aarch64
sed -i '33i int ioperm(unsigned long int from, unsigned long int num, int turn_on){return -1;}' src/devices/PParallelPort.cpp
%endif

%build
make

%install
make install PREFIX=%{buildroot}/usr/

%files
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/%{name}

%changelog
* Mon Sep 23 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 2.1git
- Rebuilt for Fedora

%global _name RetroArch

Name:           retroarch
Version:        1.8.1
Release:        1
Summary:        Emulator frontend
License:        GPL-3.0
URL:            http://www.retroarch.com
Group:          Emulators
Source0:        https://github.com/libretro/RetroArch/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
Source9:        %{name}.desktop
BuildRequires:  gcc-c++
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(freetype2)
BuildRequires:  pkgconfig(gbm)
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xinerama)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xv)
BuildRequires:  pkgconfig(wayland-egl)
BuildRequires:  pkgconfig(libass)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(libv4l2)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(alsa)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  pkgconfig(openal)
BuildRequires:  pkgconfig(sdl2)
BuildRequires:  pkgconfig(SDL2_gfx)
BuildRequires:  pkgconfig(SDL2_image)
BuildRequires:  pkgconfig(SDL2_mixer)
BuildRequires:  pkgconfig(SDL2_net)
BuildRequires:  pkgconfig(SDL2_ttf)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python3-devel
BuildRequires:  systemd-devel
BuildRequires:  unzip p7zip
BuildRequires:  pkgconfig(libavcodec)
BuildRequires:  pkgconfig(libavdevice)
BuildRequires:  pkgconfig(libavformat)
BuildRequires:  pkgconfig(libavutil)
BuildRequires:  pkgconfig(libswscale)
BuildRequires:  desktop-file-utils
%if ( 0%{?suse_version} || 0%{?leap_version} )
BuildRequires:  vulkan-devel
%endif

%description
RetroArch is a modular multi-system emulator system that is designed to be
fast, lightweight, and portable. It has features few other emulators frontends
have, such as real-time rewinding and game-aware shading.

%prep
%setup -q -n %{_name}-%{version}

%build
export CFLAGS="$RPM_OPT_FLAGS"
export CXXFLAGS="$CFLAGS"
./configure --prefix=%{_prefix} \
    --enable-materialui \
    --enable-xmb \
    --enable-sdl2 \
    --enable-libusb \
    --enable-udev \
    --with-man_dir=%{_mandir} \
    --enable-threads \
    --enable-thread_storage \
    --enable-ffmpeg \
    --enable-ssa \
    --enable-dylib \
    --enable-networking \
    --enable-networkgamepad \
    --enable-opengl \
    --enable-x11 \
    --enable-xinerama\
    --enable-kms \
    --enable-wayland \
    --enable-egl \
    --enable-zlib \
    --enable-alsa \
    --enable-al \
    --enable-jack \
    --enable-pulse \
    --enable-freetype \
    --enable-xvideo \
    --enable-v4l2 \
%ifarch x86
    --enable-sse \
%endif
%if ( 0%{?suse_version} || 0%{?leap_version} )
    --enable-vulkan \
    --enable-fbo \
%endif
    --enable-7zip \
    --enable-mmap
make %{?jobs:-j%jobs}

%install
%make_install
mkdir -p %{buildroot}%{_datadir}/applications
install -m 644 %{SOURCE9} %{buildroot}%{_datadir}/applications/

%files
%{_docdir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.cfg
%{_bindir}/%{name}
%{_bindir}/%{name}-cg2glsl
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.svg
%{_mandir}/man?/%{name}.?*
%{_mandir}/man?/%{name}-cg2glsl.?*

%changelog
* Tue Nov 05 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 1.8.1
- Rebuilt for Fedora
* Wed Aug 23 2017 glmarques.info@gmail.com
- Updated to version 1.6.7
  NOTE: This is a bugfixed and spit-and-polish update. The initial release notes below are still from the 1.6.6 release.
  General changelog
  SCANNER: Fix directory scanning.
  SCANNER: Fix file scanning.
  COMMON: Fix ‘Disk Image Append’ option.
  FREEBSD: Compatibility fixes for Video4Linux2 camera driver.
  GUI: (MaterialUI) Add disk image append icons.
  GUI: (MaterialUI) Improve word wrapping when menu icons are enabled.
  GUI: (MaterialUI) Add User Interface -> Appearance -> Menu Icons Enable. You can turn on/off the icons on the lefthand side of the menu entries.
  GUI: Performance optimizations for XMB menu driver – only calculates visible items.
  LOCALIZATION: Update Italian translation.
  Core updates since previous version (1.6.6)
  Picodrive should hopefully work now again on Android after notaz‘ updates.
  Beetle PSX’s OpenGL renderer should now work on various AMD GPUs thanks to rz5‘s efforts. There were previously some black screen issues on certain non-Polaris AMD GPUs.
  Beetle PSX – Fixed bugs (geometry updates had max width and height unset, other ones) (by albertofustinoni).
  Beetle Saturn – Unloading game leaves core unusable fix (by albertofustinoni).
  Beetle Supergrafx – add turbo on/off for 2-button controller mode (by retrowertz).
  Prosystem – NTSC Color Palette updates and DB updates (by underball).
* Fri Aug 11 2017 glmarques.info@gmail.com
- Updated to version 1.6.4
  General changelog
  ANDROID: Fire Stick & Fire TV remote overrides gamepad port 0 on button press and viceversa like SHIELD devices
  ANDROID: Provide default save / system / state / screenshot locations
  AUDIO: Audio mixer supports MOD/S3M/XM file types now!
  INPUT: input swap override flag (for remotes) is cleared correctly
  INPUT: allow specifying libretro device in remap files
  INPUT: allow specifying analog dpad mode in remap files
  INPUT: allow saving libretro device to remap files
  INPUT: allow saving analog dpad mode to remap files
  INPUT: allow removing core and game remap files from the menu
  COMMON: Cores can now request to set a ‘shared context’. You no longer need to explicitly enable ‘Shared Hardware Context’ for Citra/OpenLara/Dolphin.
  COMMON: Add ‘Delete Core’ option to Core Information menu.
  COMMON: Allow Max Timing Skew to be set to 0.
  COMMON: Change the “content dir” behavior so it works on either a flag or an empty directory setting, now platform drivers can provide defaults for save / system / state / screenshot dirs and still allow the content dir functionality, these settings are under settings / saving and flagged as advanced
  GUI: You can turn on/off ‘Horizontal Animation’ now for the XMB menu. Turning animations off can result in a performance boost.
  GUI: Fix sublabel word-wrapping in XMB where multi-byte languages were cut off too soon
  LOCALIZATION: Update Dutch translation
  LOCALIZATION: Update Traditional Chinese translation
  LOCALIZATION: Update Italian translation
  LOCALIZATION: Update Russian translation
  WINDOWS: Provide default save / system / state / screenshot locations
  LOBBIES: Show what country the host is in
  MENU: Enable OSD text rendering for gdi and libcaca drivers
  WINDOWS 98/ME/2K: Set default directory for MSVC 2005 RetroArch version.
  WII: Better V-Sync handling, backported from SuperrSonic.
  WIIU: Exception handler rewritten.
* Thu Jul  6 2017 igarcia@suse.com
- Add version 1.6.1

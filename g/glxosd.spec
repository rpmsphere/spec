Name:           glxosd
Version:        3.2.2
Release:        16.1
Summary:        On-Screen-Display for OpenGL applications
License:        MIT
Group:          System/X11/Utilities
URL:            https://glxosd.nickguletskii.com/
Source0:        %{name}-%{version}.tar.xz
#Source1:        baselibs.conf
Patch0:         64bit_portability.patch
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  fontconfig-devel
BuildRequires:  freetype-devel
BuildRequires:  gcc-c++
BuildRequires:  mesa-libGLU-devel
BuildRequires:  lm_sensors-devel
BuildRequires:  luajit-devel
BuildRequires:  glew-devel
Recommends:     %{name}-sensors-plugin
Source2:        LuaJIT-2.1.0-beta3.tar.gz

%description
GLXOSD is an extensible on-screen display (OSD) for OpenGL applications running on Linux
with X11 which aims to provide similar functionality to MSI Afterburner/RivaTuner OSD.
It can show FPS, frame timings, temperatures and more in OpenGL games and applications.
It can also be used to benchmark games, much like voglperf.

%package nvidia-plugin
Summary:        GLXOSD plugin for Nvidia drivers compatibility
Group:          System/X11/Utilities
BuildArch:      noarch

%description nvidia-plugin
GLXOSD plugin for compatibility with Nvidia's proprietary drivers.

%package sensors-plugin
Summary:        GLXOSD plugin to show temperatures
Group:          System/X11/Utilities
BuildArch:      noarch

%description sensors-plugin
GLXOSD plugin for CPU temperatures and other temperatures available through lm-sensors.

%prep
%setup -q
cp %{SOURCE2} third-party/
sed -i 's|2\.0\.4|2.1.0-beta3|' third-party/BuildLuaJIT.cmake
%ifarch aarch64
sed -i 's|__x86_64__|__aarch64__|' src/elfhacks/elfhacks.h
%endif
sed -i 's|lua_setfield(L, LUA_GLOBALSINDEX,|lua_setglobal(L,|' src/glinject/glinject.c
cd src/freetype-gl-glxosd/freetype-gl
%patch 0 -p1

%build
export CFLAGS=-Wl,--allow-multiple-definition
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} \
      -DCMAKE_BUILD_TYPE=RelWithDebInfo \
      -G "Unix Makefiles"
make %{?_smp_mflags} all

%install
%make_install

%files nvidia-plugin
%{_datadir}/%{name}/%{name}/plugins/OSD/dataproviders/NVMLDataProvider.lua
%{_datadir}/%{name}/%{name}/ffi/nvml.lua
%config(noreplace) %{_sysconfdir}/%{name}/OSD/dataproviders/NVMLDataProvider

%files sensors-plugin
%{_datadir}/%{name}/%{name}/plugins/OSD/dataproviders/LibsensorsDataProvider.lua
%{_datadir}/%{name}/%{name}/ffi/libsensors.lua
%config(noreplace) %{_sysconfdir}/%{name}/OSD/dataproviders/LibsensorsDataProvider

%files
%doc README.md AUTHORS
%license LICENSE
%attr(755, root, root) %{_bindir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}
%{_datadir}/%{name}
%{_libdir}/%{name}
%exclude %{_datadir}/%{name}/%{name}/conf
%exclude %{_datadir}/%{name}/%{name}/ffi/nvml.lua
%exclude %{_sysconfdir}/%{name}/OSD/dataproviders/NVMLDataProvider
%exclude %{_datadir}/%{name}/%{name}/plugins/OSD/dataproviders/NVMLDataProvider.lua
%exclude %{_datadir}/%{name}/%{name}/plugins/OSD/dataproviders/LibsensorsDataProvider.lua
%exclude %{_datadir}/%{name}/%{name}/ffi/libsensors.lua
%exclude %{_sysconfdir}/%{name}/OSD/dataproviders/LibsensorsDataProvider

%changelog
* Wed Dec 20 2017 Wei-Lun Chao <bluebat@member.fsf.org> - 3.2.2
- Rebuilt for Fedora
* Sun Oct 15 2017 pousaduarte@gmail.com
- specfile cleanup
* Sun Feb 12 2017 pousaduarte@gmail.com
- Update to version 3.2.2:
  * fix lib paths for non-debian distros
  * use 'exec' in glxosd launcher
  * Hopefully fix crashes by replacing glXQueryContext with GL_VIEWPORT queries
  * Remove generated files
  * Bump version numbers
  * Fix install setting incorrect launcher permissions
  * Fix libsensors data not showing when there are multiple chips
  * Bump version number
* Wed Sep 21 2016 pousaduarte@gmail.com
- streamline specfile (lib paths were fixed upstream)
* Wed Sep 21 2016 mailaender@opensuse.org
- update to version 3.2.1
* Sat Aug 27 2016 mailaender@opensuse.org
  * spec file cleanup
  * build with debug symbols
* Thu Aug 25 2016 pousaduarte@gmail.com
  * initial packaging of version 3.2.0

%undefine _debugsource_packages

Name:           octaforge
Version:        0.1.9alpha10
Release:        1
Summary:        A 3D Game Engine and platform
License:        MIT
Group:          Development/Libraries
URL:            http://octaforge.org/
Source0:        http://octaforge.org/releases/0.1.9-alpha10/octaforge-engine_source.zip
BuildRequires:  SDL_image-devel SDL_mixer-devel zlib-devel libcurl-devel gcc-c++

%description
OctaForge is:
* A 3D Game Engine, with Lua scripting and an easy to use in-game editor.
* A Game Platform, where you can find multiplayer games to play
    and upload your own games to as well.
* A place to find and upload game content to, from 3D models to textures
    to sounds.
* A community of game developers.

%prep
%setup -q -n OF-Engine
sed -i '70s/SERVER_LOGFILE/ SERVER_LOGFILE /g' src/octaforge/of_localserver.cpp

%build
make -C src

%install
rm -rf ${RPM_BUILD_ROOT}
mkdir -p ${RPM_BUILD_ROOT}%{_libdir}/%{name}/

install -m 644 *.lua ${RPM_BUILD_ROOT}%{_libdir}/%{name}/
install -m 644 *.txt ${RPM_BUILD_ROOT}%{_libdir}/%{name}/
install -m 755 *.sh ${RPM_BUILD_ROOT}%{_libdir}/%{name}/

cp -a bin_unix ${RPM_BUILD_ROOT}%{_libdir}/%{name}/bin_unix
chmod 755 ${RPM_BUILD_ROOT}%{_libdir}/%{name}/bin_unix/*

cp -a data ${RPM_BUILD_ROOT}%{_libdir}/%{name}/data
chmod 644 $(find ${RPM_BUILD_ROOT}%{_libdir}/%{name}/data/* -type f)
chmod 755 $(find ${RPM_BUILD_ROOT}%{_libdir}/%{name}/* -type d)

mkdir ${RPM_BUILD_ROOT}%{_bindir}/
cat > ${RPM_BUILD_ROOT}%{_bindir}/octaforge-server << EOF
#!/bin/sh
%{_libdir}/%{name}/run_server.sh
EOF

cat > ${RPM_BUILD_ROOT}%{_bindir}/octaforge-client << EOF
#!/bin/sh
%{_libdir}/%{name}/run_client.sh
EOF
chmod 755 ${RPM_BUILD_ROOT}%{_bindir}/octaforge-*

mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/applications/
cat > ${RPM_BUILD_ROOT}%{_datadir}/applications/octaforge.desktop << EOF
[Desktop Entry]
Type=Application
Name=OctaForge
Comment=A 3D Game Engine
Exec=octaforge-client
Categories=Development;
Icon=%{_libdir}/%{name}/data/maps/empty/preview.png
EOF
chmod 644 ${RPM_BUILD_ROOT}%{_datadir}/applications/octaforge.desktop

%clean
%__rm -rf %{buildroot}

%files 
%{_libdir}/%{name}
%{_bindir}/octaforge-server 
%{_bindir}/octaforge-client
%{_datadir}/applications/octaforge.desktop

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.1.9alpha10
- Rebuilt for Fedora
* Thu Nov 15 2012 Robert Wei <robert.wei@ossii.com.tw> 0.1.9alpha10-1
- build RPM package for Fedora 17

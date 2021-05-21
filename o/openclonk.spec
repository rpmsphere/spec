Name:           openclonk
Version:        5.3.2
Release:        5.1
Summary:        Fast-paced 2d genre mix
Group:          Amusements/Games/Action/Other
License:        ISC - CC-BY
URL:            http://www.openclonk.org/
Source0:        openclonk-release-%{version}-src.tar.gz
Source1:        openclonk.png
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  make, cmake, gcc, gcc-c++
BuildRequires:  libX11-devel, mesa-libGL-devel
BuildRequires:  libXpm-devel
BuildRequires:  glew-devel, libpng-devel, openssl-devel
BuildRequires:  SDL-devel, SDL_mixer-devel
BuildRequires:  gtk2-devel, libjpeg-devel, zlib-devel, boost-devel
BuildRequires:  ImageMagick

%description
Clonks are witty and nimble human-like creatures. They build, run, dig and fight:
everything in real-time and in direct control, alone, with or versus other players.
The first release contains small scale team and all vs all melees.

%prep
%setup -q -n openclonk-release-%{version}-src

%build
export CFLAGS=$RPM_OPT_FLAGS
%ifarch %ix86
export CXXFLAGS="$RPM_OPT_FLAGS -march=i686"
%else
export CXXFLAGS=$RPM_OPT_FLAGS
%endif

cmake . -DCMAKE_INSTALL_PREFIX=/usr
make %{?_smp_mflags}

%install
# No support for that yet.
#rm -rf $RPM_BUILD_ROOT
#make install DESTDIR=$RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a planet/* $RPM_BUILD_ROOT%{_datadir}/%{name}

install -Dm755 clonk $RPM_BUILD_ROOT%{_datadir}/%{name}/clonk.bin
install -Dm755 c4group $RPM_BUILD_ROOT%{_bindir}/c4group
install -Dm755 c4group $RPM_BUILD_ROOT%{_bindir}/c4script
echo -e "#!/bin/sh\ncd %{_datadir}/%{name}\nexec ./clonk.bin" > $RPM_BUILD_ROOT%{_bindir}/clonk
install -Dm644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/clonk.png
convert src/res/oc.ico clonk.png
install -Dm644 clonk-2.png $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/clonk.png

# Generate desktop file
install -D -m 0644 clonk.desktop $RPM_BUILD_ROOT%{_datadir}/applications/clonk.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README* docs/* licenses/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/pixmaps/clonk.png
%{_datadir}/applications/clonk.desktop
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/48x48/apps/clonk.png

%changelog
* Sat Feb 09 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 5.3.2
- Rebuilt for Fedora
* Sun Mar 20 2011 bwiedemann@novell.com
- Update to version 5.1.2
* Fri Dec 10 2010 spell1337@gmail.com
  First release.

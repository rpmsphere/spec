%undefine _debugsource_packages

Name:           lenmus
Version:        5.6.2
Release:        1
Summary:        A free program for learning music
License:        GPL-3.0
Group:          Productivity/Multimedia/Sound/Midi
URL:            http://www.lenmus.org/en/noticias
Source0:        http://sourceforge.net/projects/lenmus/files/Source%20packages/%{name}-%{version}.tar.gz
Source1:        %{name}.png
Source2:        %{name}.desktop
Source3:        %{name}.sh
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  boost-devel
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gettext
BuildRequires:  gettext-devel
BuildRequires:  glibc-devel
BuildRequires:  intltool
BuildRequires:  libtool
#BuildRequires:  lomse-devel
BuildRequires:  make
BuildRequires:  portmidi-devel
BuildRequires:  sqlite-devel
BuildRequires:  unittest-cpp-devel
BuildRequires:  wxGTK3-devel
BuildRequires:  zlib-devel
BuildRequires:  fluid-soundfont-gm
Requires:       lomse
Requires:       timidity++

%description
LenMus is a free program for learning music. It allows you to focus on
specific skills and exercises, on both theory and aural training.
The different activities can be customized to meet your needs.
It includes an score editor.

%prep
%setup -q
sed -i -e 's|-Wall|-Wall -fPIC -fpermissive|' -e '272s|^#set|set|' -e 's|wx-config|wx-config-3.0|' CMakeLists.txt

%build
cmake -DCMAKE_INSTALL_PREFIX=%{_prefix} -DPortTime_LIBRARY=%{_libdir}/libportmidi.so .
make %{?_smp_mflags}

%install
make DESTDIR=%{buildroot} install
mkdir -p %{buildroot}%{_datadir}/pixmaps
mkdir -p %{buildroot}%{_datadir}/applications
install -m644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps/.
install -m644 %{SOURCE2} %{buildroot}%{_datadir}/applications/.
mv %{buildroot}%{_bindir}/%{name} %{buildroot}%{_bindir}/%{name}.bin
install -m755 %{SOURCE3} %{buildroot}%{_bindir}/%{name}

%files
%doc AUTHORS *.md LICENSE NEWS README THANKS
%{_bindir}/*
%{_datadir}/*

%changelog
* Sun Aug 15 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 5.6.2
- Rebuilt for Fedora
* Sun Dec 23 2012 joop.boonen@opensuse.org
- Don't start rctimidity automaticaly as audio playback won't work anymore
* Wed Dec 19 2012 joop.boonen@opensuse.org
- Used the lenmus provided desktop and png files
* Sun Dec 16 2012 joop.boonen@opensuse.org
- Build LenMus 5.3
- Created wrapper script and desktop file
- Added wx and make scripts
* Wed Nov 28 2012 joop.boonen@opensuse.org
- Build LenMus 5.2

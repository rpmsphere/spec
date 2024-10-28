%undefine _debugsource_packages

Name:           polyphone
Version:        1.9
#Version:       2.0
Release:        6.1
Summary:        Soundfont (SF2) Editor
Group:          Applications/Multimedia
License:        GPLv3+
URL:            https://polyphone-soundfonts.com/
Source0:        polyphone-%{version}-src.zip
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  libogg-devel
BuildRequires:  libvorbis-devel
BuildRequires:  rtmidi-devel
BuildRequires:  stk-devel
BuildRequires:  qcustomplot-qt5-devel
BuildRequires:  jack-audio-connection-kit-devel
BuildRequires:  alsa-lib-devel
BuildRequires:  portaudio-devel
BuildRequires:  desktop-file-utils

%description
Polyphone is a free software for editing Soundfonts in SF2 format. These files
contain a multitude of audio samples put together and configured so as to form
musical instruments that can be used by synthesizers such as Fluidsynth and
played using a MIDI keyboard.

The goal of Polyphone is to provide:
* a simple and efficient interface for creating and editing .sf2 files
* tools to facilitate and automate the edition of different parameters,
  making it possible to handle a large amount of data.

%prep
%setup -q -n trunk
#sed -i -e 's| rtmidi| librtmidi|' -e 's|-lqcustomplot|-lqcustomplot-qt5|' polyphone.pro
sed -i 's|-lqcustomplot|-lqcustomplot-qt5|' polyphone.pro
%ifarch aarch64
sed -i 's|-mfpmath=387||' polyphone.pro
%endif
sed -i '1i #include <QAction>' configuration/config.cpp

%build
qmake-qt5
make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_bindir}
install -m0755 RELEASE/polyphone %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/
install -m0644 ressources/icon.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/polyphone.png
mkdir -p %{buildroot}%{_datadir}/applications
cat > polyphone.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Name=Polyphone
GenericName=Polyphone
Comment=Soundfont Editor
Exec=polyphone
Icon=polyphone
Terminal=false
Type=Application
Categories=Applications;AudioVideo;
EOF
desktop-file-install \
    --dir %{buildroot}%{_datadir}/applications \
    polyphone.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :

%files
%doc README
%{_bindir}/polyphone
%{_datadir}/applications/polyphone.desktop
%{_datadir}/icons/hicolor/128x128/apps/polyphone.png

%changelog
* Thu Feb 08 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 1.9
- Rebuilt for Fedora
* Tue Jun 25 2013 LTN Packager <packager-el6rpms@LinuxTECH.NET> - 0.6-1
- initial package release

Name:           qtgain
Version:        0.9.5
Release:        6.1
Summary:        Frontend for MP3Gain, VorbisGain, AACGain and Metaflac
License:        GPL-2.0+
Group:          Productivity/Multimedia/Sound/Utilities
URL:            http://qt-apps.org/content/show.php/QtGain?content=56842
Source0:        http://qt-apps.org/CONTENT/content-files/56842-QtGain.tar.lzma
Source1:        QtGain.desktop
BuildRequires:  desktop-file-utils
BuildRequires:  qt-devel
#Recommends:     aacgain
#Recommends:     flac
#Recommends:     id3v2
#Recommends:     mp3gain
#Recommends:     vorbisgain
BuildRoot:      %{_tmppath}/%{name}-%{version}-build

%description
QtGain is a simply frontend for MP3Gain, VorbisGain, AACGain and Metaflac which
analyses and adjusts your media files so that they have the same volume without
the need to reencode the files.

%prep
%setup -q -n QtGain
chmod 644 ChangeLog.txt LICENSE

%build
qmake-qt4 QMAKE_CXXFLAGS+="%{optflags}" -config debug QtGain.pro
make %{?_smp_mflags}

%install
%make_install INSTALL_ROOT=%{buildroot}
install -Dpm 0644 qtgain.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/QtGain.png
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%files
%defattr(-,root,root)
%doc ChangeLog.txt LICENSE
%{_bindir}/qtgain
%{_datadir}/applications/QtGain.desktop
%{_datadir}/icons/hicolor/*/apps/QtGain.png

%changelog
* Wed Sep 25 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.5
- Rebuilt for Fedora
* Thu Nov 22 2012 asterios.dramis@gmail.com
- Fix desktop file Exec= entry (change QtGain to qtgain).
* Sat Jul 28 2012 asterios.dramis@gmail.com
- Initial release (version 0.9.5).
- Added a desktop file for the application.

%undefine _debugsource_packages

Name:           coquillo
URL:            https://qt-apps.org/content/show.php/Coquillo?content=141896
License:        GPL v2 or later
Group:          Productivity/Multimedia/Sound/Utilities
Summary:        An audio metadata editor
Version:        1.7
Release:        6.1
Source:         %{name}-%{version}-src.tar.gz
BuildRequires:  gcc-c++ qt4-devel taglib-devel

%description
Coquillo is a metadata editor / tagger for various audio file formats.
It is based on Qt4 and TagLib. Supported audio formats include MP3,
Ogg/Vorbis, FLAC, MP4 and MusePack. Embedded cover art support for MP3,
Ogg/Vorbis and FLAC. Current features:
- CDDB read support.
- Integrated FreeDB web search.
- Resolve tags from filenames.
- Generate filenames from tags.
- Process multiple files at once.

%prep
%setup -q
sed -i '105,106s| p| pp|' src/MetaDataWriter.cpp

%build
qmake-qt4
make %{?_smp_mflags}

%install
make INSTALL_ROOT=%{buildroot} install

%files
%doc CHANGES LICENSE TODO BUGS
%{_bindir}/coquillo
%{_datadir}/applications/coquillo.desktop
%{_datadir}/pixmaps/coquillo.png

%changelog
* Sun Dec 16 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.7
- Rebuilt for Fedora
* Wed Sep 7 2011 giacomosrv@gmail.com
- packaged Coquillo version 1.7
* Sat Aug 13 2011 giacomosrv@gmail.com
- packaged Coquillo version 1.6
* Sat Jul 30 2011 giacomosrv@gmail.com
- packaged Coquillo version 1.5
* Fri Jun 3 2011 giacomosrv@gmail.com
- packaged Coquillo version 1.3

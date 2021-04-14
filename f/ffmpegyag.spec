Name:              ffmpegyag
Version:           0.7.6.git20170908
Release:           7.1
Summary:           Advanced GUI for ffmpeg
License:           MIT
Group:             Productivity/Multimedia/Video/Editors and Convertors
URL:               http://sourceforge.net/projects/ffmpegyag
Source:            ffmpegyag-code-%{version}.zip
Patch0:            ffmpegyag.patch
BuildRequires:     pkgconfig(alsa)
BuildRequires:     pkg-config
BuildRequires:     compat-ffmpeg28-devel
BuildRequires:     gcc-c++
BuildRequires:     unzip
BuildRequires:     wxGTK3-devel

%description
FFmpegYAG is an advanced GUI for the popular FFmpeg audio/video encoding tool.
To use all features (split/concat, x264 10 bit, HE-AAC) it is recommend to use
the FFmpeg Hi (http://sourceforge.net/projects/ffmpeg-hi/) build.

Main features:
* batch encoding for multiple tasks
* interactive video preview, real-time video/audio playback
* multiple streams processing for video/audio/subtitles
* trim file to segments (with optional fade in/out filters) and concatenate them

%prep
%setup -q -n ffmpegyag-code
%patch0 -p1

%build
chmod a-x CHANGELOG LICENSE README.md
%configure
sed -i 's|include/ffmpeg|include/compat-ffmpeg28|' Makefile
make %{?_smp_mflags}

%install
%make_install
# remove debian stuff
rm -rf %{buildroot}%{_datadir}/{doc,menu}/ffmpegyag

%files
%doc CHANGELOG LICENSE README.md
%{_bindir}/ffmpegyag
%{_datadir}/applications/ffmpegyag.desktop
%{_datadir}/icons/hicolor/*/apps/ffmpegyag.png
%{_datadir}/pixmaps/ffmpegyag.xpm

%changelog
* Thu Jun 14 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.7.6.git20170908
- Rebuilt for Fedora
* Tue May  9 2017 joerg.lorenzen@ki.tng.de
- Update to version 0.7.6.git20170503
- Build against current ffmpeg libraries.
* Fri May 20 2016 joerg.lorenzen@ki.tng.de
- Update to version 0.7.6.git20151111
* Tue Sep 22 2015 olaf@aepfle.de
- Use pkgconfig for ffmpeg BuildRequires
* Sun Apr 12 2015 fisiu@opensuse.org
- Initial package, 261.

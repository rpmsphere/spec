%global debug_package %{nil}

Name:           freej
Version:        0.10
Release:        30.4
Summary:        A vision mixer
Group:          Applications/Multimedia
License:        GPLv2
URL:            http://freej.org/
Source0:        ftp://ftp.dyne.org/freej/releases/%{name}-%{version}.tar.gz
Source1:        ipernav.png
Patch1:         freej-0.8.1-VIDIOCGTUNER_non_fatal.diff
BuildRequires:  gcc-c++, nasm, chrpath, flex
BuildRequires:  jack-audio-connection-kit-devel, libogg-devel
BuildRequires:  libpng-devel, libpng10-devel, libjpeg-devel
BuildRequires:  libshout-devel, fftw-devel, cwiid-devel
BuildRequires:  pulseaudio-libs-devel, esound-devel, arts-devel
BuildRequires:  libtheora-devel, speex-devel 
BuildRequires:  libsmbclient-devel
#BuildRequires:  libfame-devel, libmad-devel, faac-devel, a52dec-devel, directfb-devel
BuildRequires:  flac-devel, libmpcdec-devel, gsm-devel
BuildRequires:  SDL-devel, SDL_ttf-devel, slang-devel 
BuildRequires:  perl perl(HTML::Template)

%description
FreeJ is a digital instrument for realtime video
manipulation used in the fields of dance teather, veejaying, medical
visualisation and TV.

It runs a video engine in which multiple layers can be filtered thru
effect chains and then mixed together with images, movies, live
cameras, particle generators, text scrollers and more.  All the
resulting video mix can be shown on multiple and remote screens,
encoded into a movie and streamed live to the internet.

FreeJ can be controlled locally or remotely, also from multiple places
at the same time, using its slick console interface; can be automated
via javascript and operated via MIDI and Joystick.

%prep
%setup -q
%patch1 -p0 -b .freej-0.8.1-VIDIOCGTUNER_non_fatal
sed -i '1i #include <sys/stat.h>' src/vimo_ctrl.cpp
sed -i 's|hci_remote_name|hci_read_remote_name|' lib/cwiid/bluetooth.c
sed -i -e 's|ffmpeg/avcodec.h|libavcodec/avcodec.h|' -e 's|ffmpeg/avformat.h|libavformat/avformat.h|' src/include/video_layer.h

%build
export CPPFLAGS="-I%{_includedir}/compat-ffmpeg -I%{_includedir}/slang -I%{_includedir}/libpng10 -fpermissive -fPIC -DHAVE_SYS_UIO_H"
export LDFLAGS="-lz"
%configure --enable-joystick --enable-v4l --enable-jack
make 
# generate documentation
cd doc/scripting
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
%ifarch x86_64 aarch64
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64
%endif
mkdir -p %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/pixmaps
cp %SOURCE1 %{buildroot}/%{_datadir}/pixmaps/ipernav.png
chrpath -d %{buildroot}%{_bindir}/%{name}
sed -i -e's,/usr/local/bin,%{_bindir},g' %{buildroot}/%{_datadir}/freej/pan.js

cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=Freej
Comment=Freej is a Vision Mixer
Exec=freej
Icon=ipernav.png
Categories=Application;AudioVideo;Multimedia;
Terminal=true
Type=Application
EOF

%clean
rm -rf %{buildroot}

%files 
%{_datadir}/doc/%{name}-%{version}
%{_bindir}/%{name}
%{_includedir}/%{name}*.h
%{_libdir}/%{name}/*.la
%{_libdir}/%{name}/*.so
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/ipernav.png
%{_mandir}/man1/%{name}*

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.10
- Rebuild for Fedora
* Fri Aug 08 2008 Paulo Roma <roma@lcg.ufrj.br> - 0.10-4
- Updated to 0.10
- Added BR fftw-devel.
* Mon Mar 24 2008 Paulo Roma <roma@lcg.ufrj.br> - 0.9.1-3
- Fixed doc generation.
- Removed rpath from binary.
- Fixed pan.js script path.
* Sun Jan 13 2008 Paulo Roma <roma@lcg.ufrj.br> - 0.9.1-2
- Updated to 0.9.1
* Tue Oct 16 2007 Paulo Roma <roma@lcg.ufrj.br> - 0.9-1
- Updated to 0.9
- Removed gcc-4.1 patch.
- Using CPPFLAGS for slang.
* Wed Jan 17 2007 Paulo Roma <roma@lcg.ufrj.br> - 0.8.1-1
- Initial spec file
- Created patch for compiling in gcc-4.1

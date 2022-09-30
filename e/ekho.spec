Name: ekho
License: GPL
Group: Application/Multimedia
Summary: A text-to-speech (TTS) software
Version: 7.7.1
Release: 1
Source: http://downloads.sourceforge.net/e-guidedog/%{name}-%{version}.tar.xz
URL: http://e-guidedog.sourceforge.net/ekho.php
BuildRequires: libsndfile-devel, portaudio-devel, libvorbis-devel, lame-devel
BuildRequires: soundtouch-devel, espeak-devel

%description
eGuideDog TTS (Ekho) supports Cantonese, Mandarin, Zhaoan Hakka and Korean
(in trial). It can also speak English through Festival.

%package devel
Group: Development/Libraries
Summary: A text-to-speech (TTS) software
Requires: %{name}

%description devel
Development files for ekho.

%prep
%setup -q
#sed -i '1i #include <cstring>' soundtouch/source/example/SoundStretch/WavFile.cpp *_symbol_pcm.cpp
#sed -i 's|<soundtouch/SoundTouch.h>|"soundtouch/include/SoundTouch.h"|' ekho.h
sed -i 's|pause") > 0|pause") != NULL|' src/libekho_impl.cpp
sed -i -e '899s|pause") >|pause") !=|' -e '900s|0|NULL|' src/ekho_dict.cpp

%build
%configure
#sed -i -e 's/#\(.cp -aLf\)/\1/' -e 's/ \$(datadir)/ $(DESTDIR)$(datadir)/' Makefile
#sed -i 's|./lib/libSoundTouch.a|-lSoundTouch|' Makefile
sed -i 's|-Wall|-Wall -fPIC|' Makefile libmusicxml/linux/Makefile
rm -f libmusicxml/src/*/*.o
make

%install
rm -rf %{buildroot}
make DESTDIR=%{buildroot} install

%clean
rm -rf %{buildroot}

%files
%doc AUTHORS README COPYING ChangeLog
%{_bindir}/*
##%{_libdir}/lib%{name}.so.*
%{_datadir}/ekho-data

%files devel
%{_includedir}/*.h
##%{_libdir}/lib%{name}.*a
##%{_libdir}/lib%{name}.so

%changelog
* Mon Sep 10 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 7.7.1
- Rebuilt for Fedora

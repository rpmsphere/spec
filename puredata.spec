%global debug_package %{nil}
%define        majver %(echo %version | cut -d. -f1-2)
%define        minver %(echo %version | cut -d. -f3)

Name:          puredata
Version:       0.50.0
Release:       1
Summary:       A real-time graphical programming environment for media processing
Group:         Graphical Desktop/Applications/Multimedia
URL:           http://puredata.info
Source0:       http://switch.dl.sourceforge.net/project/pure-data/pure-data/%{version}/pd-%{majver}-%{minver}.src.tar.gz
Source1:       %{name}.png
License:       GPL
BuildRequires: glibc-devel
BuildRequires: alsa-lib-devel
BuildRequires: portaudio-devel
##BuildRequires: libjack-devel >= 0.103.0
BuildRequires: tcl-devel
BuildRequires: tk-devel
Provides: pd

%description
PD (aka Pure Data) is a real-time graphical programming environment for audio, video, and graphical processing. It is the third major branch of the family of patcher programming languages known as Max (Max/FTS, ISPW Max, Max/MSP, jMax, etc.) originally developed by Miller Puckette and company at IRCAM. The core of Pd is written and maintained by Miller Puckette and includes the work of many developers, making the whole package very much a community effort.
Pd was created to explore ideas of how to further refine the Max paradigm with the core ideas of allowing data to be treated in a more open-ended way and opening it up to applications outside of audio and MIDI, such as graphics and video. 
It is easy to extend Pd by writing object classes ("externals") or patches ("abstractions"). The work of many developers is already available as part of the standard Pd packages and the Pd developer community is growing rapidly. Recent developments include a system of abstractions for building performance environments; a library of objects for physical modeling; and a library of objects for generating and processing video in realtime.
Pd is free software and can be downloaded either as an OS-specific package, source package, or directly from CVS. Pd was written to be multi-platform and therefore is quite portable; versions exist for Win32, IRIX, GNU/Linux, BSD, and MacOS X running on anything from a PocketPC to an old Mac to a brand new PC. It is possible to write externals and patches that work with Max/MSP and Pd using flext and cyclone.

%prep
%setup -q -n pd-%{majver}-%{minver}

%build
export CFLAGS="-DUSE_INTERP_RESULT -lm"
./autogen.sh
./configure --prefix=/usr --enable-jack --enable-alsa
make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall MANINSTDIR=$RPM_BUILD_ROOT/%{_mandir}
ln -sf %{_bindir}/pd $RPM_BUILD_ROOT%{_libdir}/pd/bin/pd
#rm $RPM_BUILD_ROOT%{_includedir}/portaudio.h $RPM_BUILD_ROOT%{_libdir}/libportaudio*

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications

install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps

cat > $RPM_BUILD_ROOT%{_datadir}/applications/puredata.desktop << EOF
[Desktop Entry]
Encoding=UTF-8
Type=Application
Name=PureData
GenericName=Sound Editor
Comment=Synth
Icon=puredata
Exec=pd
Terminal=false
Categories=Application;AudioVideo;Synthesis;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/pd*
%{_datadir}/pixmaps/puredata.png
%{_datadir}/applications/puredata.desktop
%{_includedir}/*
%{_libdir}/pd
%{_libdir}/pkgconfig/*
%{_mandir}/man1/pd.1.gz
%{_mandir}/man1/pdreceive.1.gz
%{_mandir}/man1/pdsend.1.gz

%changelog
* Tue Oct 22 2019 Wei-Lun Chao <bluebat@member.fsf.org> - 0.50.0
- Rebuild for Fedora
* Mon Jul 27 2009 Automatic Build System <autodist@mambasoft.it> 0.42.5-1mamba
- update to 0.42.5
* Mon Jul 27 2009 Automatic Build System <autodist@mambasoft.it> 0.42-1mamba
- automatic update by autodist
* Thu Oct 02 2008 gil <puntogil@libero.it> 0.41-2mamba
- changed configure options, added: enable-jackenable-alsa
* Wed Oct 01 2008 gil <puntogil@libero.it> 0.41-1mamba
- update to 0.41
- added desktop file
* Fri Jan 06 2006 Silvan Calarco <silvan.calarco@mambasoft.it> 1-1qilnx
- package created by autospec

%define kver %(uname -r)

Summary:    WebcamStudio - Creates your own webcam TV Studio
Name:	    webcamstudio
Version:    0.56
Release:    1
URL:	    http://code.google.com/p/webcamstudio/
Source0:    WebcamStudio_%{version}.tar.gz
Source1:    %{name}.png
License:    GPL
Group:      Applications/Multimedia
Requires:   jre => 1.6
Requires:   gstreamer-plugins-base
Requires:   gstreamer-plugins-good
Requires:   gstreamer-plugins-ugly
Requires:   %{name}-kmod
BuildRequires: kernel-devel, kernel-headers

%description
WebcamStudio is a virtual webcam software that you can use with Skype or flash
website like UStream or Stickam to create a professional looking broadcast,
including banners, animations, transitnimations and ions, etc...

This tool is not meant as a video editor but as a live video mixer giving you
the possibilities to change the look of the broadcast on the fly.

    * Switch webcams on a single click
    * Show that IRC channel in your video broadcast
    * Broadcast your desktop for nice HOWTO's
    * Be creative and put animations and banners
    * Display what song is currently played by Rhythmbox
    * Co-host a remote friend show his webcam inside your output (PicInPic)
    * Connect to WeatherBug and display your current meteo
    * Apply some fancy effects on each source
    * Have a green wall, then why not use the ChromaKey effect to do the same as the weather man on the news network
    * Use all kinds of devices as webcamera like a MiniDV, your iPhone, etc....

%package kmod
Summary:    A video4linux driver providing video pipes
Requires:   kernel = %kver

%description kmod
This is a modfied version of the vloopback driver from
Jeroen Vreeken et al.
Modifications consist in:
1) You can choose minor numbers of input and output devices
2) Write is made block when nobody is reading the other
end of the pipe.

-Olivier Debon	(olivier@debon.net)

------------------------------------------------------
With the driver you can use the output of a user program to feed a program that
would normally communicate with a video4linux device.To achieve this a video pipe 
consists out of two video4linux devices:one for the generating program to write its 
data to and one for a normal video4linux program to read from. At the moment there 
are only few programs that can feed the input of the pipe: invert and resize, 
the example programs with the driver and motion, my motion detection program.

%prep
%setup -q -n %{name}

%build
# kmod
cd usr/share/webcamstudio/webcamstudio-src
make

%install
rm -rf $RPM_BUILD_ROOT
install -dm 755 %{buildroot}%{_libdir}/%{name}
cp -a lib *.jar %{buildroot}%{_libdir}/%{name}

install -dm 755 %{buildroot}%{_datadir}/%{name}
cp -a microphone %{buildroot}%{_datadir}/%{name}

#launcher
install -dm 755 %{buildroot}%_bindir/
cat > %buildroot%{_bindir}/%{name} <<EOF
#!/bin/bash
# WebcamStudio for GNU/Linux Launcher
# Patrick Balleux 2008
# Version 0.38a

cd %{_libdir}/%{name}
java -jar WebcamStudio.jar
EOF

# menu-entry
mkdir -p %buildroot%{_datadir}/applications/
cat > %buildroot%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Encoding=UTF-8
Name=WebcamStudio
Comment=WebcamStudio for GNU/Linux
Exec=%{name}
Icon=%{name}
StartupNotify=true
Terminal=false
Type=Application
Categories=AudioVideo;
EOF

# icon
install -dm 755 %{buildroot}%{_datadir}/pixmaps
install -m 644 %{SOURCE1} %{buildroot}%{_datadir}/pixmaps

# kmod
install -Dm 744 usr/share/webcamstudio/webcamstudio-src/%{name}.ko %{buildroot}/lib/modules/%{kver}/kernel/drivers/misc/%{name}.ko

%post kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%postun kmod
depmod -a > /dev/null 2> /dev/null
exit 0

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc README.TXT
%attr(755,root,root)%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/%{name}.desktop

%files kmod
%doc usr/share/webcamstudio/webcamstudio-src/COPYING usr/share/webcamstudio/webcamstudio-src/README
/lib/modules/%{kver}/kernel/drivers/misc/%{name}.ko

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 
- Rebuild for Fedora
* Mon Mar 28 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 0.56
- Rebuild for OSSII

* Mon Dec 06 2009 tigger-gg <rpm@mandrivauser.de> 0.52-1mud2010.0
- initial package for Mandriva 2010.0 based on a mandrakeclubnl spec

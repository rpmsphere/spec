%bcond_without audiofile
%bcond_without jack
%bcond_without mikmod
%bcond_without nas
%bcond_without opengl
%define flac_ver %(rpm -q --qf %{VERSION} flac-devel)
#define prever         rc4
#define prever_dot    .%{prever}

Summary: Audio player for systems using the Advanced Linux Sound Architecture
Name:    alsaplayer
Version: 0.99.81
Release: 1
License: GPLv2
Group:   Applications/Multimedia
URL:     https://www.alsaplayer.org/
Source0: https://www.alsaplayer.org/alsaplayer-%{version}%{?prever}.tar.bz2
Source1: alsaplayer.png
Source2: alsaplayer-small.png
Source3: alsaplayer-large.png
Patch0:  max_path.patch
BuildRequires: gcc-c++, gettext
BuildRequires: doxygen, gtk2-devel, gtk+-devel
BuildRequires: alsa-lib-devel, esound-devel
BuildRequires: flac-devel
BuildRequires: libid3tag-devel
BuildRequires: libmad-devel 
BuildRequires: libsndfile-devel
BuildRequires: libstdc++-devel
BuildRequires: libvorbis-devel
BuildRequires: xosd-devel
BuildRequires: zlib-devel
%{?with_audiofile:BuildRequires: audiofile-devel}
%{?with_jack:BuildRequires: pipewire-jack-audio-connection-kit-devel}
%{?with_mikmod:BuildRequires: mikmod-devel, libmikmod} 
%{?with_nas:BuildRequires: nas-devel}
%{?with_opengl:BuildRequires: mesa-libGL-devel}
%{?with_oss:BuildRequires: alsa-oss-devel}

%package devel
Summary:        Development files for %{name}
Group:          Applications/Multimedia
Requires:       %{name} = %{version}-%{release}

%description
AlsaPlayer is a new type of PCM player. 
It is heavily multi-threaded, and tries to excercise the 
ALSA library and driver quite a bit. It has some very interesting 
features unique to Linux/Unix players. The goal is to create a fully 
pluggable framework for playing back all sort of media with focus 
on PCM audio data. 

It is also a versitile audio player with a rich plugin system. 
The Input Plugins include: Audiofile, CDDA, FLAC, MAD, MikMod, MPEG, 
OGG and WAV. 
The Output Plugins include: ALSA, Esound, JACK, NAS, OSS, SGI, and
Sparc (tested on UltraSparc).
There are also a few scope plugins included.

Install AlsaPlayer if you want a versatile audio player.

%description devel
This package contains development files for %{name}.

%prep
%setup -q -n %{name}-%{version}%{?prever}
##%patch0 -p1 -b .max_path
for i in ./AUTHORS ./ChangeLog; do
        iconv -f iso-8859-1 -t utf-8 < "$i" > "${i}_"
        mv "${i}_" "$i"
done

# Avoid standard rpaths on lib64 archs:
sed -i -e 's|"/lib /usr/lib\b|"/%{_lib} %{_libdir}|' configure

%if "%{flac_ver}" >= "1.1.3"
grep -rl unsigned ./input/flac | xargs sed -i -e's,unsigned \* bytes,size_t \* bytes,g'
%endif

%build
%configure %{?with_audiofile:--enable-audiofile} \
           %{!?with_jack:--disable-jack} \
           %{!?with_mikmod:--disable-mikmod} \
           %{!?with_nas:--disable-nas} \
           %{!?with_opengl:--disable-opengl} \
           %{!?with_oss:--disable-oss}
           
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR=%{buildroot}
# Install icons
%{__mkdir_p} %{buildroot}%{_datadir}/pixmaps
%{__install} -p -m644 %{SOURCE1} %{SOURCE2} %{SOURCE3} \
    %{buildroot}%{_datadir}/pixmaps/

%{__mkdir_p} %{buildroot}%{_datadir}/applications
# System menu entry
%{__cat} << EOF > %{buildroot}%{_datadir}/applications/%{name}.desktop
[Desktop Entry]
Name=ALSA Player
Comment=Audio player for the Advanced Linux Sound Architecture
Icon=alsaplayer.png
Exec=alsaplayer
Terminal=false
Type=Application
Encoding=UTF-8
Categories=Application;AudioVideo;
EOF

%find_lang %{name}

# Clean up for the docs
%{__rm} -f examples/Makefile*
%{__rm} -rf %{buildroot}%{_docdir}/%{name}

%clean
%{__rm} -rf %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files devel
%doc examples
%{_includedir}/%{name}
%{_libdir}/libalsaplayer.so
%{_libdir}/pkgconfig/%{name}.pc

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING INSTALL README TODO docs/reference/html
%{_bindir}/%{name}
%{_libdir}/%{name}
#{_libdir}/libalsaplayer.la
%{_libdir}/libalsaplayer.so.*
%{_mandir}/man1/%{name}.1*
%{_datadir}/applications/*%{name}.desktop
%{_datadir}/pixmaps/%{name}*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.99.81
- Rebuilt for Fedora
* Sat Aug 02 2008 Paulo Roma <roma@lcg.ufrj.br> 0.99.80-3
- Added bcond_without mikmod. libmikmod-3.2.0 beta2 crashes on F9.
- Requires libmikmod_2 for pushing the appropriate mikmod-devel package.
* Tue Jul 22 2008 Paulo Roma <roma@lcg.ufrj.br> 0.99.80-2
- Patched for building on F9.
- Using %%find_lang.
- Converted AUTHORS and ChangeLog to utf8.
- Removed rpath.
* Mon Nov 20 2007 Paulo Roma <roma@lcg.ufrj.br> 0.99.80-1
- Update to 0.99.80
* Sun Oct 21 2007 Paulo Roma <roma@lcg.ufrj.br> 0.99.80-rc4.3
- Update to 0.99.80-rc4
- Using %%prever.
* Mon Jul 26 2007 Paulo Roma <roma@lcg.ufrj.br> 0.99.80-rc2.2
- Update to 0.99.80-rc2
* Mon Jul 02 2007 Paulo Roma <roma@lcg.ufrj.br> 0.99.80-rc1.2
- Update to 0.99.80-rc1
- Added missing BRs.
- Removed desktop-vendor.
- Created devel package.
- Changed description.
- Using bcond jack, oss, nas, opengl for RHEL.
- Patched flac input plugin (flac >= 1.1.3) for building on x86_64 
* Mon Aug 30 2004 Matthias Saou <https://freshrpms.net/> 0.99.76-2
- Added ldconfig calls since there are libs included.
* Wed May 19 2004 Matthias Saou <https://freshrpms.net/> 0.99.76-2
- Rebuilt for Fedora Core 2.
* Fri Nov  7 2003 Matthias Saou <https://freshrpms.net/> 0.99.76-1
- Update to 0.99.76.
- Rebuilt for Fedora Core 1.
- Added missing gcc-c++ build dependency.
* Fri May  2 2003 Matthias Saou <https://freshrpms.net/>
- Update to 0.99.75.
* Mon Mar 31 2003 Matthias Saou <https://freshrpms.net/>
- Rebuilt for Red Hat Linux 9.
- Fix build order.
* Sat Feb  8 2003 Matthias Saou <https://freshrpms.net/>
- Update to 0.99.74.
- Added xosd support.
* Mon Jan 13 2003 Matthias Saou <https://freshrpms.net/>
- Update to 0.99.73.
* Fri Sep 27 2002 Matthias Saou <https://freshrpms.net/>
- Rebuilt for Red Hat Linux 8.0.
- New desktop entry.
* Wed Sep 18 2002 Matthias Saou <https://freshrpms.net/>
- Update to 0.99.72.
- Further spec file changes and fixes.
* Thu Sep  5 2002 Matthias Saou <https://freshrpms.net/>
- Spec file cleanup to match freshrpms.net habits :-)
* Sat Jul 6 2002 Angles <angles@aminvestments.com>
- version 0.99.71
* Thu May 30 2002 Angles <angles@aminvestments.com>
- version 0.99.70
- updated summary and description to highlight the apps increased versitility
- minor spec file cleanup and desktop link update to latest usage
* Sun May 5 2002 Angles <angles@aminvestments.com>
- version 0.99.60
- package now has include files
- package has 4 files in libdir that actually belong there, not in a subdir
- made patch so rpm installs docs, not the app make install
* Sat Apr 6 2002 Angles <angles@phpgroupware.org>
- version 0.99.58
* Wed Mar 20 2002 Angles <angles@phpgroupware.org>
- version 0.99.57
* Sat Mar 02 2002 Angles <angles@phpgroupware.org>
- version 0.99.54
* Sat Feb 23 2002 Angles <angles@phpgroupware.org> 0.99.53-aap4
- customize for RedHat 7.2
* Sat Feb 16 2002 Yves Duret <yduret@mandrakesoft.com> 0.99.53-1mdk
- version 0.99.53
- %%makeinstall_std
* Sat Jan 26 2002 Yves Duret <yduret@mandrakesoft.com> 0.99.52-1mdk
- version 0.99.52
- build against mad
- png icons
* Sat Dec 22 2001 Stefan van der Eijk <stefan@eijk.nu> 0.99.50-3mdk
- fix BuildRequires
* Fri Dec  7 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.50-2mdk
- s|Copyright|License|;
* Fri Sep 28 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.50-1mdk
- 0.99.50.
- Add --enable-alsa --enable-esd --disable-debug --enable-oggvorbis.
* Fri Aug 24 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.36-1mdk
- 0.99.36.
* Sat Jun 16 2001 Stefan van der Eijk <stefan@eijk.nu> 0.99.33-0.2mdk
- BuildRequires: gtk+-devel
* Fri Jun 15 2001 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.33-0.1mdk
- 0.99.33-pre3.
* Fri Feb  9 2001 Jeff Garzik <jgarzik@mandrakesoft.com> 0.99.32-13mdk
- Do not exclude alpha from build.
* Thu Dec  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-12mdk
- Recompile with alsa-0.5.10.
* Tue Nov 28 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-11mdk
- Add icons.
* Sat Nov 18 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-10mdk
- fix gcc2.96 compilation.
* Thu Oct 24 2000 David BAUDENS <baudens@mandrakesoft.com> 0.99.32-9mdk
- EcludeArch: ppc
* Thu Aug 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-8mdk
- remove some debugging messages
* Thu Aug 24 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-7mdk
- build against latest alsa-lib
- fix requires
* Sun Aug 13 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.99.32-6mdk
- disabled the use of makeinstall macro in order to have the libraries installed
  in the correct place (reported by Anton Graham <darkimage@bigfoot.com>)
- cleaner specfile
- more menu dir macros
* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.99.32-5mdk
- automatically added BuildRequires
* Mon Jul 17 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-4mdk
- fix macros
* Tue Jun 27 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.32-3mdk
- macroszifications.
- build against latest alsa-lib
- Use macros for update-menus.
* Mon Jun 26 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-2mdk
- build against latest alsa-lib
- add url
* Thu Jun 08 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.99.32-1mdk
- new release
* Fri May 19 2000 Francis Galiegue <fg@mandrakesoft.com> 0.99.31-2mdk
- ExcludeArch: alpha sparc sparc64
* Sun Apr 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.99.31-1mdk
- Add menu entry.
- Fix Requires.
- Fix titi sucks.
- Build again latest alsa-lib and libmikmod.
* Thu Apr 20 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.99.31-2mdk
- fixed group
* Thu Mar 09 2000 Thierry Vignaud <tvignaud@mandrakesoft.com>
- update to 99.31
- compiled against alsa-lib-0.5.5
* Tue Aug 24 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- initial spec

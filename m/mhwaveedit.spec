Name:           mhwaveedit
Version:        1.4.24
Release:        1
Summary:        Sound editing program        
Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://gna.org/projects/mhwaveedit
Source:         https://codeload.github.com/magnush/mhwaveedit/tar.gz/v%{version}#/%{name}-%{version}.tar.gz
Requires:       pulseaudio
Requires:       hicolor-icon-theme
BuildRequires:  pulseaudio-libs-devel alsa-lib-devel jack-audio-connection-kit-devel
BuildRequires:  libsndfile-devel libsamplerate-devel ladspa-devel
BuildRequires:  desktop-file-utils
BuildRequires:  gtk2-devel
BuildRequires:  gettext

%description
mhWaveEdit is a graphical program for editing sound files. It is completely
free (GPL).

%prep
%setup -q
sed -i '24i #include "int_box.h"' src/sound-pulse.c

%build
%configure

iconv -f iso-8859-1 -t utf-8 AUTHORS > AUTHORS.conv && mv -f AUTHORS.conv AUTHORS
make %{?_smp_mflags} 

%install
#removal of buildroot is no longer necassary, except for EPEL5
make install DESTDIR=%{buildroot}

%find_lang %{name}
desktop-file-install    \
    --dir %{buildroot}%{_datadir}/applications \
     share/applications/%{name}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [$1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache -f %{_datadir}/icons/hicolor &>/dev/null || :

%files -f %{name}.lang
#Upstream has been contacted about incorrect fsf address 2012-08-07
%doc AUTHORS COPYING README BUGS NEWS TODO HACKING ChangeLog
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_mandir}/man1/%{name}.1.*

%changelog
* Fri Feb 07 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 1.4.24
- Rebuild for Fedora
* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.4.22-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild
* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild
* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild
* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.22-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild
* Tue Aug 07 2012 Jørn Lomax <northlomax@gmail.com> 1.4.22-3
- Convert AUTHORS to utf8m upstream notified about incorrect fsf address
* Tue Aug 07 2012 Jørn Lomax <northlomax@gmail.com> 1.4.22-2
- added BUGS, NEWS, TODO, HACKING and changelog. Shortned desciption
* Mon Jul 30 2012 Jørn Lomax <northlomax@gmail.com> 1.4.22-1
- inital package

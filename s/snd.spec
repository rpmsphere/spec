Name:		snd
Version:	24.3
Release:	1
Summary:	Sound file editor
License:	BSD
Group:		Sound/Editors and Converters
URL:		https://ccrma.stanford.edu/software/snd/
Source0:	ftp://ccrma-ftp.stanford.edu/pub/Lisp/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
# Math
BuildRequires:	gmp-devel
BuildRequires:	pkgconfig(fftw3)
BuildRequires:  libmpc-devel
# Output audio
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(jack)
#BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(samplerate)
# GUI stuff
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(glu)
BuildRequires:	pkgconfig(gsl) >= 1.0
#BuildRequires:	pkgconfig(gtk+-3.0)
# Encoders & Co.
Requires:	flac
Requires:	mpg123
#Requires:	mpg321
Requires:	speex
Requires:	timidity++
#Requires:	ttaenc
Requires:	vorbis-tools
Requires:	wavpack

%description
Snd is a free sound editor modelled loosely after Emacs and an old,
sorely-missed PDP-10 sound editor named Dpysnd.

%files
%doc README.Snd HISTORY.Snd NEWS
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_mandir}/man1/%{name}.1*

%prep
%setup -q
#sed -i 's|^LIBS = |LIBS = -lportaudio |' makefile.in
chmod 0644 s7.c

%build
%configure \
	--with-gsl \
	--with-gmp \
	--with-fftw \
	--with-alsa \
	--without-pulseaudio \
	--without-portaudio \
	--with-jack \
	--with-ladspa \
	--without-gui

%make_build

%install
%make_install

# Provide a menu item
mkdir -p %{buildroot}%{_datadir}/applications
install -m 0644 %{SOURCE1} %{buildroot}%{_datadir}/applications/

# Fix perms
chmod +x %{buildroot}%{_datadir}/%{name}/grani.rb

%changelog
* Sun Apr 14 2024 Wei-Lun Chao <bluebat@member.fsf.org> - 24.3
- Rebuilt for Fedora
* Thu Feb 20 2020 umeabot <umeabot> 20.1-2.mga8
+ Revision: 1547240
- Mageia 8 Mass Rebuild
* Fri Feb 07 2020 daviddavid <daviddavid> 20.1-1.mga8
+ Revision: 1487730
- new version: 20.1
+ wally <wally>
- replace deprecated %%configure2_5x
* Thu Jan 02 2020 daviddavid <daviddavid> 20.0-1.mga8
+ Revision: 1475442
- new version: 20.0
* Wed Nov 20 2019 daviddavid <daviddavid> 19.9-1.mga8
+ Revision: 1461759
- new version: 19.9
* Mon Oct 14 2019 daviddavid <daviddavid> 19.8-1.mga8
+ Revision: 1453065
- new version: 19.8
* Thu Sep 12 2019 daviddavid <daviddavid> 19.7-1.mga8
+ Revision: 1440073
- new version: 19.7
* Tue Aug 27 2019 daviddavid <daviddavid> 19.6-2.mga8
+ Revision: 1433788
- rebuild for new gsl 2.6
* Wed Jul 31 2019 daviddavid <daviddavid> 19.6-1.mga8
+ Revision: 1426127
- new version: 19.6
* Sun Jun 30 2019 daviddavid <daviddavid> 19.5-1.mga8
+ Revision: 1416270
- new version: 19.5
* Mon Apr 15 2019 daviddavid <daviddavid> 19.3-1.mga7
+ Revision: 1390629
- new version: 19.3
* Mon Mar 11 2019 daviddavid <daviddavid> 19.2-1.mga7
+ Revision: 1373909
- new version: 19.2
* Wed Feb 06 2019 daviddavid <daviddavid> 19.1-1.mga7
+ Revision: 1363621
- new version: 19.1
* Wed Jan 02 2019 daviddavid <daviddavid> 19.0-1.mga7
+ Revision: 1348549
- new version: 19.0
* Tue Nov 27 2018 daviddavid <daviddavid> 19-1.mga7
+ Revision: 1335931
- new version: 19
* Thu Nov 22 2018 daviddavid <daviddavid> 18.9-2.mga7
+ Revision: 1333372
- initial package snd

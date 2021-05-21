Name: xoscope
Version: 2.3
Release: 1
Summary: Digital Oscilloscope for PC
Source: %{name}-%{version}.tar.gz
URL: http://xoscope.sourceforge.net/
Group: Engineering
License: GPL
BuildRequires: libICE-devel alsa-lib-devel fftw-devel gtkdatabox-devel comedilib-devel

%description
xoscope is a digital oscilloscope that uses a sound card (via ALSA or EsounD)
and/or a data acquisition card (via COMEDI) as the signal input.

%prep
%setup -q

%build
export LDFLAGS=-Wl,--allow-multiple-definition
%configure
%make_build

%install
%make_install
sed -i 's|Network;||' %{buildroot}%{_datadir}/applications/net.sourceforge.xoscope.desktop

%files
%{_bindir}/xoscope
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*
%{_datadir}/metainfo/*
%{_datadir}/pixmaps/*
%doc README AUTHORS NEWS TODO

%changelog
* Sun Apr 18 2021 Wei-Lun Chao <bluebat@member.fsf.org> - 2.3
- Rebuid for Fedora
* Fri Dec 29 2017 Vitaly Lipatov <lav@altlinux.ru> 2.2-alt1
- initial build for ALT Sisyphus

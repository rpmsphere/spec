Name:           qarecord
Summary:        QT based ALSA recording interface
Version:        0.5.0
Release:        10
Source0:        https://dl.sf.net/alsamodular/%{name}-%{version}.tar.bz2
Patch0:         qarecord-0.5.0-upstream1.patch
Patch1:         qarecord-0.5.0-rus.patch
URL:            https://alsamodular.sourceforge.net/
License:        GPLv2
Group:          Sound
BuildRequires:  qt4-devel alsa-lib-devel
BuildRequires:	pkgconfig(jack)

%description
QARecord is a simple multithreaded stereo recording tool. It can record both
16 bit and 32 bit WAVs. By using a large ringbuffer for the captured data,
buffer overruns are avoided. QARecord can also be used as JACK client. 

%prep
%setup -q
%patch0 -p1
%patch1 -p1
iconv -f=latin1 -t=utf8 man/de/%{name}.1 -o man/de/%{name}.1
iconv -f=latin1 -t=utf8 man/fr/%{name}.1 -o man/fr/%{name}.1

%build
%configure
%make_build

%install
%make_install

install -D -m 0644 src/pixmaps/%{name}_48.xpm %{buildroot}%{_datadir}/pixmaps/%{name}.xpm

mkdir -p %{buildroot}/etc/modules-load.d
echo "snd_seq" > %{buildroot}/etc/modules-load.d/%{name}.conf

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=QARecord
Name[ru]=QARecord
Comment=ALSA recording GUI
Comment[ru]=Запись звука
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;Recorder;
EOF

%post
modprobe snd_seq

%files
%doc README NEWS COPYING AUTHORS 
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.xpm
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%{_datadir}/applications/mandriva-%{name}.desktop
/etc/modules-load.d/%{name}.conf

%changelog
* Tue Sep 29 2020 Wei-Lun Chao <bluebat@member.fsf.org> - 0.5.0
- Rebuilt for Fedora
* Fri Feb 17 2017 Andrey Bondrov <andrey.bondrov@rosalab.ru> 0.5.0-10
- (1cc4199) MassBuild#1257: Increase release tag

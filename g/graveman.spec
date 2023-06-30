%define realver %{version}-5

Summary:	Simple frontend for CD creation
Name:		graveman
Version:	0.3.12
Release:	17.1
License:	GPLv2+
Group:		Archiving/Cd burning
URL:		https://graveman.tuxfamily.org/index-e.php
Source0:	https://graveman.tuxfamily.org/sources/%{name}-%{realver}.tar.bz2
Patch0:		graveman-0.3.12-5-cdrkit.patch
BuildRequires:	desktop-file-utils
BuildRequires:	ghostscript-core ImageMagick
BuildRequires:	perl-XML-Parser
BuildRequires:	libmng-devel
BuildRequires:	pkgconfig(flac)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(id3tag)
BuildRequires:	pkgconfig(libglade-2.0)
#BuildRequires:	pkgconfig(mad)
BuildRequires:	pkgconfig(vorbis)
BuildRequires:  libmng-devel
Requires:	cdrdao
Requires:	cdrkit
Requires:	cdrkit-genisoimage
Requires:	dvd+rw-tools
Requires:	sox

%description
Another frontend for cdrecord, mkisofs, readcd and sox!
With graveman you can burn audio cds (wav, ogg, mp3), data cds,
and duplicate cds.

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS THANKS README*
%{_bindir}/%{name}
%{_datadir}/applications/*
%{_datadir}/%{name}/
%{_datadir}/pixmaps/*
%{_mandir}/man1/*
%{_mandir}/fr/man1/*

%prep
%setup -q -n %{name}-%{realver}
%patch0 -p1 -b .cdrkit

%build
%configure
make CFLAGS+="-fPIC -Wno-format-security"

%install
mkdir -p %{buildroot}%{_mandir}/man1
cp man/%{name}.man %{buildroot}%{_mandir}/man1/%{name}.1
mkdir -p %{buildroot}%{_mandir}/fr/man1
cp man/%{name}.fr.man %{buildroot}%{_mandir}/fr/man1/%{name}.1
perl -p -i -e 's/install\:/none\:/g' man/Makefile
%make_install

#menu
desktop-file-install --vendor="" \
	--remove-category="Application" \
	--add-category="X-MandrivaLinux-System-Archiving-CDBurning" \
	--dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

%find_lang %{name}

%changelog
* Tue Apr 19 2016 Wei-Lun Chao <bluebat@member.fsf.org> - 0.3.12
- Rebuilt for Fedora
* Fri Jul 25 2014 Denis Silakov <denis.silakov@rosalab.ru> 0.3.12-15
+ Revision: 4628bee
- MassBuild#464: Increase release tag

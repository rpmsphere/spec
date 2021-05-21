%define _disable_ld_as_needed 1
%define _disable_ld_no_undefined 1

# To fix paths, Racket performs direct ELF surgery during install. D'oh!
# (see collects/setup/unixstyle-install.rkt)
# That's why we end up with slightly different executables that share the same
# build ID, and this breaks debuginfo extraction.
%define debug_package %{nil}
%define __spec_install_post %{nil}

Name:		racket
Version:	6.2.1
Release:	7.1
Summary:	A Scheme implementation
License:	LGPLv2+
Group:		Development/Other
URL:		http://www.racket-lang.org
Source0:	http://mirror.racket-lang.org/installers/%{version}/%{name}-%{version}-src.tgz
Source1:	racket.png
BuildRequires:	ghostscript-core ImageMagick
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
%define libname lib%{name}
%define develname lib%{name}-devel
Requires:	%{libname} = %{version}

%description
Racket is a Scheme implementation. It implements
the language as described in the Revised^5 Report on the
Algorithmic Language Scheme and adds numerous extensions.

%package -n	%{libname}
Summary:	Main library for %{name}
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
This package contains the library needed to run programs dynamically
linked with %{name}.

%package -n	%{develname}
Summary:	Headers for developing programs that will use %{name}
Group:		Development/Other
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use %{name}.

%package -n	g%{name}
Summary:	Racket graphical Scheme implementation
Group:		Development/Other
Requires:	%{name} = %{version}

%description -n	g%{name}
GRacket is the Racket's graphical Scheme implementation. It embeds and
extends Racket with a graphical user interface (GUI) toolbox.

%package -n	dr%{name}
Summary:	Racket graphical development environment
Group:		Development/Other
Requires:	g%{name} = %{version}

%description -n	dr%{name}
DrRacket is the graphical development environment for creating 
Racket and GRacket applications.

%prep
%setup -q

%build
cd src
%configure --enable-shared
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir $RPM_BUILD_ROOT
cd src
export LD_LIBRARY_PATH=$RPM_BUILD_ROOT%{_libdir}
export PLT_SETUP_OPTIONS="-j 1"
make DESTDIR=$RPM_BUILD_ROOT install

# correct installation
install -d -m 755 $RPM_BUILD_ROOT%{_datadir}
install -d -m 755 $RPM_BUILD_ROOT%{_libdir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/drracket.desktop << EOF
[Desktop Entry]
Name=DrRacket
Comment=Scheme IDE
Exec=drracket
Icon=drracket
Terminal=false
Type=Application
StartupNotify=true
Categories=Development;IDE;
EOF
sed -i 's|%{buildroot}||' $RPM_BUILD_ROOT%{_datadir}/applications/slideshow.desktop

mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
mkdir -p $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/{16x16,32x32,48x48,64x64}/apps
convert -scale "48x48" %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/drracket.png
convert -scale "16x16" %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/16x16/apps/drracket.png
convert -scale "32x32" %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/32x32/apps/drracket.png
convert -scale "48x48" %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/48x48/apps/drracket.png
convert -scale "64x64" %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/64x64/apps/drracket.png

%files
%doc src/*.txt README
%{_libdir}/%{name}
%{_datadir}/%{name}
%{_sysconfdir}/%{name}
%{_bindir}/*
%{_mandir}/man1/*
%{_datadir}/doc/%{name}
%exclude %{_bindir}/gracket
%exclude %{_bindir}/drracket
%exclude %{_mandir}/man1/gracket.1*
%exclude %{_mandir}/man1/drracket.1*
#exclude %{_libdir}/%{name}/collects/mred
#exclude %{_libdir}/%{name}/collects/drracket
#exclude %{_datadir}/%{name}/doc/drracket

%files -n %{libname}
%{_libdir}/libracket3m-%{version}.so

%files -n %{develname}
%{_libdir}/libracket3m.so
%{_libdir}/*.la
%{_libdir}/*.a
%{_includedir}/*

%files -n gracket
#{_libdir}/%{name}/collects/mred
%{_bindir}/gracket
%{_mandir}/man1/gracket.1*

%files -n drracket
#{_libdir}/%{name}/collects/drracket
%{_bindir}/drracket
%{_mandir}/man1/drracket.1*
#{_datadir}/%{name}/doc/drracket
%{_datadir}/pixmaps/drracket.png
%{_datadir}/icons/hicolor/16x16/apps/drracket.png
%{_datadir}/icons/hicolor/32x32/apps/drracket.png
%{_datadir}/icons/hicolor/48x48/apps/drracket.png
%{_datadir}/icons/hicolor/64x64/apps/drracket.png
%{_datadir}/applications/*.desktop

%changelog
* Mon Aug 17 2015 Wei-Lun Chao <bluebat@member.fsf.org> - 6.2.1
- Rebuilt for Fedora
* Sat May 05 2012 mitya <mitya> 5.2.1-1.mga2
+ Revision: 234779
- Update to 5.2.1
* Sat May 05 2012 mitya <mitya> 5.2-1.mga2
+ Revision: 234767
- Fix build
- Import Racket 5.2
- Created package structure for racket.

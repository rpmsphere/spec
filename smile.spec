%global debug_package %{nil}

Name:		smile
Summary:	Slideshow Maker In Linux Environnement
Version:	1.0
Release:	6.1
Source0:	http://download.tuxfamily.org/smiletool/%{name}-%{version}.tar.gz
Source1:	%{name}.png
URL:		http://smile.tuxfamily.org/
Group:		Applications/Graphics
License:	GPLv2+
BuildRequires:  libpng-devel
BuildRequires:	gcc-c++, qt4-devel, qt-webkit-devel, mesa-libGL-devel
Requires:	netpbm-progs, sox, mjpegtools, vorbis-tools, ImageMagick, mencoder, mplayer

%description
Smile is a slideshow creation application which makes it easy to
produce attractive slideshows with optional background music.

%prep
%setup -q -n %{name}
rm -f BIB_ManSlide/Eff_sup/licence.txt~ BIB_ManSlide/Help/doc_en.html~

%build
qmake-qt4
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_bindir}

install -m 755 smile $RPM_BUILD_ROOT%{_datadir}/%{name}/%{name}
install -m 755 fake.pl $RPM_BUILD_ROOT%{_datadir}/%{name}/
install -m 644 *.qm $RPM_BUILD_ROOT%{_datadir}/%{name}/
cp -R Interface $RPM_BUILD_ROOT%{_datadir}/%{name}/
cp -R BIB_ManSlide $RPM_BUILD_ROOT%{_datadir}/%{name}/
ln -s %{_datadir}/%{name}/%{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -Dm 644 %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/pixmaps/%{name}.png

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
cat > $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=Smile
Comment=Slideshow generator
Comment[de]=Ein Werkzeug für das Erzeugen von Slideshows
Comment[fr]=Générateur de diaporamas
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=AudioVideo;AudioVideoEditing;
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png

%changelog
* Wed May 04 2011 Wei-Lun Chao <bluebat@member.fsf.org> - 1.0
- Rebuild for Fedora

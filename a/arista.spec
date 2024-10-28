%undefine _debugsource_packages
Name:           arista
Version:        0.9.6
Release:        1
Summary:        Multimedia transcoder
License:        GPLv2
Group:          Applications/Multimedia
URL:            https://programmer-art.org/projects/arista-transcoder
Source:         https://programmer-art.org/media/releases/arista-transcoder/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  python2-setuptools, python2-devel
Requires: python2-gstreamer, gstreamer-plugins-base, gstreamer-plugins-good, gstreamer-plugins-bad, gstreamer-plugins-ugly, gstreamer-ffmpeg

%description
A simple preset-based transcoder for the GNOME Desktop and a small script for 
terminal-based transcoding. Settings are chosen based on output device and 
quality preset.

Features
--------
 * Presets for Android, iPod, computer, DVD player, PSP, and more
 * Live preview to see encoded quality
 * Automatically discover available DVD drives and media
 * Rip straight from DVD media easily
 * Automatically discover and record from Video4Linux devices
 * Support for H.264, WebM, FLV, Ogg, DivX and more
 * Batch processing of entire directories easily
 * Simple terminal client for scripting
 * Nautilus extension for right-click file conversion

%prep 
%setup -q
sed -i 's|sys.prefix|"%{buildroot}", "usr"|' setup.py

%build
python2 setup.py build

%install
rm -rf $RPM_BUILD_ROOT
python2 setup.py install --skip-build --root %{buildroot}

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_bindir}/arista-*

%files
%{_bindir}/%{name}*
%{_datadir}/applications/%{name}.desktop 
%{_datadir}/%{name}
%{_datadir}/doc/%{name}
%{python2_sitelib}/%{name}*
%{_datadir}/locale/*/LC_MESSAGES/%{name}.mo
%exclude %{_datadir}/locale/templates/arista.pot
/usr/lib/nautilus/extensions-2.0/python/arista-nautilus.py*

%changelog
* Tue Mar 20 2018 Wei-Lun Chao <bluebat@member.fsf.org> - 0.9.6
- Rebuilt for Fedora
* Mon Mar 29 2010 Egner Quero <legnerquero [AT] gmail.com> - 0.9.3
- Packaged to Mandriva (Blogdrake Repository)

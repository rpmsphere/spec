Name:           pytube
Version:        0.0.11.5
Release:        6.1
Summary:        Graphical multimedia converter
Group:          Video
License:        GPLv3+
URL:            https://www.bashterritory.com/%{name}/
Source:        https://www.bashterritory.com/%{name}/releases/%{name}-%{version}.tar.bz2
BuildRequires:  python2
Requires: sox
Requires: ffmpeg
Requires: mplayer 
Requires: notify-python 
Requires: pygtk2
Requires: mencoder
BuildArch:      noarch

%description
PyTube is a graphical multimedia converter written in Python.
It is mainly a GUI for various command line tools.

%prep
%setup -q

%install
mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -m 755 -p %{name}.py $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 -p %{name}gui.glade $RPM_BUILD_ROOT%{_datadir}/%{name}
install -m 644 -p %{name}.png $RPM_BUILD_ROOT%{_datadir}/pixmaps
cp -pr atom gdata $RPM_BUILD_ROOT%{_datadir}/%{name}

mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/stream2hdd
install -m 755 -p stream2hdd/{*.py,*.pyc} $RPM_BUILD_ROOT%{_datadir}/%{name}/stream2hdd
install -m 755 -p %{name} $RPM_BUILD_ROOT%{_bindir}

# Desktop file
mkdir -p %buildroot%{_datadir}/applications
cat > %buildroot%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
Name=PyTube
GenericName=PyTube
Comment=Graphical multimedia converter
Exec=pytube
Icon=pytube
Terminal=false
Type=Application
Categories=AudioVideo;Player;X-MandrivaLinux-Multimedia-Video;
GenericName=PyTube
EOF

sed -i 's|/usr/bin/python$|/usr/bin/python2|' %{buildroot}%{_datadir}/pytube/*/*.py %{buildroot}%{_datadir}/pytube/*/*/*.py
sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/pytube/*.py %{buildroot}%{_datadir}/pytube/*/*.py %{buildroot}%{_datadir}/pytube/*/*/*.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%doc LICENSE.txt
%{_datadir}/%{name}
%{_bindir}/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/applications/*.desktop

%changelog
* Tue Oct 15 2013 Wei-Lun Chao <bluebat@member.fsf.org> - 0.0.11.5
- Rebuilt for Fedora
* Fri Sep 03 2010 Texstar <texstar at gmail.com> 0.0.11.5-3pclos2010
- rebuild
* Sun May 24 2009 Texstar <texstar@gmail.com> 0.0.11.5-2pclos2009
- fix rpm group
* Sun Mar 15 2009 Slick50 <slick50@linuxgator.org> 0.0.11.5-1pclos2007
- 0.0.11.5
* Wed Jul 25 2008 Slick50 <slick50@linuxgator.org> 0.0.11.4-1pclos2007
- 0.0.11.4
* Wed Jul 23 2008 Slick50 <slick50@linuxgator.org> 0.0.11.2-1pclos2007
- Import to PCLinuxOS

%undefine _debugsource_packages
Name:           tunesviewer
Version: 1.5git.1330009572
Release: 11.1
License:        ASL-2.1+
Summary:        Easy podcast access in Linux
URL:            https://sourceforge.net/projects/tunesviewer
Group:          Productivity/Networking/Web/Frontends
Source:         %{name}-%{version}.tar.bz2
BuildRequires:  libpng-devel
BuildRequires:  pygtk2-devel
#BuildRequires: notify-python notification-daemon
BuildRequires:  python2-devel
#BuildRequires: pywebkitgtk
BuildRequires:  python-lxml
BuildRequires:  librsvg2-devel
BuildRequires:  librsvg2-tools
#BuildRequires:  webkitgtk-devel
BuildRequires:  desktop-file-utils
BuildRequires:  sane-backends-libs
#Requires:      pywebkitgtk
#Requires:      notify-python
BuildArch:      noarch

%description
TunesViewer is a small, easy to use program to access iTunes-university media
and podcasts in Linux.

%prep
%setup -q

%build

%install
rm -f -r $RPM_BUILD_ROOT
%{__mkdir} -pv $RPM_BUILD_ROOT%{_datadir}/%{name}/
%{__mkdir} -pv $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/
%{__mkdir} -pv $RPM_BUILD_ROOT%{_datadir}/applications/
%{__mkdir} -pv $RPM_BUILD_ROOT%{_bindir}

%{__cp} -r src/* $RPM_BUILD_ROOT%{_datadir}/%{name}/
%{__cp} -r resources/tunesview.svg $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{__cp} -r resources/TunesViewer.desktop $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
ln -sf %{_datadir}/%{name}/TunesViewer.py $RPM_BUILD_ROOT%{_bindir}/%{name}

#fix icon
pushd resources
mv tunesview.svg %{name}.svg
ICONSIZE="16 22 24 32 48 64 128 256"
for i in $ICONSIZE; do
        rsvg-convert -h $i -w $i %{name}.svg -o %{name}.png
        mkdir -pv ${i}x${i}/apps/
        mv %{name}.png ${i}x${i}/apps/
        cp -r ${i}x${i} $RPM_BUILD_ROOT%{_datadir}/icons/hicolor/
done
popd

sed -i "5d" $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
echo "Icon=tunesviewer" >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

#fix desktopfile
sed -i "6d" $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop
echo "Categories=Utility;WebUtility;" >> $RPM_BUILD_ROOT%{_datadir}/applications/%{name}.desktop

sed -i 's|/usr/bin/env python$|/usr/bin/python2|' %{buildroot}%{_datadir}/%{name}/*.py

%files
%{_bindir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.*
%{_datadir}/%{name}/
%{_datadir}/applications/%{name}.desktop

%changelog
* Thu Mar 15 2012 Wei-Lun Chao <bluebat@member.fsf.org> - 1.5git.1330009572
- Rebuilt for Fedora
* Fri Jan 27 2012 i@marguerite.su
- initial package 1.5
